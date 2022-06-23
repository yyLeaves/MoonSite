from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from .forms import SentimentForm, CountryForm, PickCountryForm, ArticleForm, \
    GraphForm, DeliveryForm, SimpleForm, StoreForm, PMapForm, SMapForm, ProbForm, PChartForm


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField:
    storage = default_storage


fieldfile = FieldFile(None, FakeField, "dummy.txt")


class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.success(self.request, "Hello Coffee Lovers! Hello WIA2005!")
        return context


class GetParametersMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", None)
        context["size"] = self.request.GET.get("size", None)
        return context

class PMapView(GetParametersMixin, FormView):
    template_name = "app/pmap.html"
    form_class = PMapForm

class SMapView(GetParametersMixin, FormView):
    template_name = "app/smap.html"
    form_class = SMapForm

class SentimentAnalysis(GetParametersMixin, FormView):
    template_name = "app/sentiment.html"
    form_class = SentimentForm

class CountryView(GetParametersMixin, FormView):
    template_name = "app/country.html"
    form_class = CountryForm

class PickCountryView(GetParametersMixin, FormView):
    template_name = "app/pick-country.html"
    form_class = PickCountryForm

class ArticleView(GetParametersMixin, FormView):
    template_name = "app/article.html"
    form_class = ArticleForm

class BarGraphView(GetParametersMixin, FormView):
    template_name = "app/Bar.html"
    form_class = GraphForm

class RankGraphView(GetParametersMixin, FormView):
    template_name = "app/Rank.html"
    form_class = GraphForm

class DeliveryView(GetParametersMixin, FormView):
    template_name = "app/delivery.html"
    form_class = DeliveryForm

class SimpleView(GetParametersMixin, FormView):
    template_name = "app/simple.html"
    form_class = SimpleForm

class StoreView(GetParametersMixin, FormView):
    template_name = "app/stores.html"
    form_class = StoreForm

class ProbView(GetParametersMixin, FormView):
    template_name = "app/prob.html"
    form_class = ProbForm

class PChartView(GetParametersMixin, FormView):
    template_name = "app/pchart.html"
    form_class = PChartForm