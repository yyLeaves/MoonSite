from Trie import *
from moon_utils import pick_country
import pycountry

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
        country_names = [pycountry.countries.get(alpha_2=c).name for c in countries]
        ctx['countries'] = country_names
        ctx['n'] = number

        return render(request, "app/pick-country.html", ctx)