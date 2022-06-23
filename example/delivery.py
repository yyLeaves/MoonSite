from moon_utils import random_sample
from django.shortcuts import render
def calc(request):
    ctx = {}
    if request.POST:
        country = request.POST['c']
        num = int(request.POST['s'])
        id = range(1, num+1)
        coords = random_sample(country=country, n=num)
        lat = [e[0] for e in coords]
        lon = [e[1] for e in coords]
        coords = zip(id, lat, lon)
        ctx['coords'] = coords
        return render(request, "app/delivery.html", ctx)