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
        plt.scatter(lat, lon, color='g')
        plt.xlabel('latitude')
        plt.ylabel('longitude')
        print(center)
        plt.scatter([center[0]], [center[1]])
        plt.title('Stores')
        plt.savefig("stores.png")


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
            # print(start, "--->", next_node)
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

        x2 = []
        y2 = []
        x2.append(store_order[-1][0])
        x2.append(store_order[0][0])
        y2.append(store_order[-1][1])
        y2.append(store_order[0][1])

        fig2 = plt.figure()
        plt.plot(x1, y1, label='path', linewidth=2, marker='o')
        plt.plot(x2, y2, label='path', linewidth=2, color='g', marker='o')
        plt.xlabel('latitude')
        plt.ylabel('longitude')
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


        return render(request, "app/delivery.html", ctx)