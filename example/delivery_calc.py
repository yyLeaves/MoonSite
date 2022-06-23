from moon_utils import random_sample
from django.shortcuts import render
import numpy as np
from moon_utils import *
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import pandas as pd
from delivery import *
import base64
from io import BytesIO
from distance import find_shortest
import gmplot

def calc(request):
    ctx = {}
    if request.POST:
        country = request.POST['c']
        n = int(request.POST['s'])
        id = range(1, n+1)

        # get random stores
        stores = random_sample(country=country, n=n)
        lat = [e[0] for e in stores]
        lon = [e[1] for e in stores]
        coords = zip(id, lat, lon)
        ctx['coords'] = coords

        # get center
        fs = find_shortest(stores)
        center = fs[0]
        ctx["center"] = center
        ctx["dist"] = f"{fs[1]:.2f}"

        # draw figure
        fig1 = plt.figure()
        plt.scatter(lon, lat, color='g')
        plt.ylabel('latitude')
        plt.xlabel('longitude')
        print(center)
        plt.scatter([center[1]], [center[0]], s=200, color='orange', marker='*')
        plt.title('Stores')
        plt.savefig("stores.png")

        # write img into html
        tmpfile = BytesIO()
        fig1.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

        html =  '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

        with open('templates/app/stores.html', 'w') as f:
            f.write(html)

        # get distance matrix
        distence_matrix = np.zeros([n, n])
        for i in range(0, n):
            for j in range(n):
                dist = get_distance(stores[i], stores[j])
                distence_matrix[i][j] = dist

        # solve using dynamic planning
        S = Solution(distence_matrix, 0)
        # print("Shortest Path: " + str(S.tsp()) + "km")
        ctx["shortest"] = f"{S.tsp():.2f}"
        res = ""
        M = S.array
        lists = list(range(len(S.X)))
        start = S.start_node
        store_order = []


        res = f"{S.start_node+1} "
        while len(lists) > 0:
            lists.pop(lists.index(start))
            m = S.transfer(lists)
            next_node = S.array[start][m]
            res += f"---> {next_node+1}\n"
            store_order.append(stores[start])
            start = next_node


        ctx["res"] = res
        print(res)
        # plot
        x1 = []
        y1 = []
        for store in store_order:
            x1.append(store[0])
            y1.append(store[1])


        x1.append(store_order[0][0])
        y1.append(store_order[0][1])

        fig2 = plt.figure()
        plt.plot(y1, x1, label='path', linewidth=2, color='g') # , marker='o'
        plt.scatter([center[1]], [center[0]], s=200, color='orange', marker='*')
        plt.ylabel('latitude')
        plt.xlabel('longitude')
        plt.title('TSP path')
        plt.legend()
        plt.savefig("path.png")

        # save image to html

        tmpfile = BytesIO()
        fig2.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

        html =  '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

        with open('templates/app/simple.html', 'w') as f:
            f.write(html)

        # draw store map
        gmap1 = gmplot.GoogleMapPlotter(center[0],
                                       center[1],
                                       5)
        x2 = [x2 for x2 in x1 if x2!=center[0]]
        y2 = [y2 for y2 in y1 if y2!=center[1]]

        gmap1.scatter(x2, y2, size=50, color='green')
        gmap1.scatter([center[0]], [center[1]], size=50, color='orange')
        gmap1.draw("templates/app/smap.html")

        # draw path map
        gmap2 = gmplot.GoogleMapPlotter(center[0],
                                       center[1],
                                       5)

        gmap2.scatter(x2, y2, size=50)
        gmap2.scatter([center[0]], [center[1]], size=50, color='orange')
        gmap2.plot(x1, y1, "cornflowerblue", edge_width=2.5)
        gmap2.draw("templates/app/pmap.html")


        return render(request, "app/delivery.html", ctx)