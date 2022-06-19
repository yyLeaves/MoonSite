from Trie import *
from moon_utils import pick_country
# 表单
def search_form(request):
    return render(request, './app/sentiment.html')


from django.shortcuts import render


# get post
def pick_countries(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['country']
        number = int(request.POST['country'])
        countries = pick_country(number)

        ctx['countries'] = countries

        ctx['n'] = number

        return render(request, "app/country.html", ctx)