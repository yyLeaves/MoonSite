from django.urls import path
import country, sentiment, delivery_calc, prob
from app.views import (
    HomePageView,
    SentimentAnalysis,
    CountryView,
    PickCountryView,
    ArticleView,
    BarGraphView,
    RankGraphView,
    DeliveryView,
    SimpleView,
    StoreView,
    PMapView,
    SMapView,
    ProbView,
    PChartView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("sentiment", SentimentAnalysis.as_view(), name='sentiment'),
    path(r'sentiment.html', sentiment.analyse),
    path(r'country-sentiment.html', sentiment.analyse),
    path("country", CountryView.as_view(), name='country'),
    path(r"country.html", sentiment.analyse_countries),
    path(r'pick-country', PickCountryView.as_view(), name='pick-country'),
    path(r'pick-country.html', country.pick_countries),
    path(r'article', ArticleView.as_view(), name='article'),
    path(r'article.html', ArticleView.as_view(), name='article'),
    path(r'Bar.html', BarGraphView.as_view()),
    path(r'Rank.html', RankGraphView.as_view()),
    path(r'delivery', DeliveryView.as_view(), name='delivery'),
    path(r'delivery.html', delivery_calc.calc),
    path(r'prob', ProbView.as_view(), name='prob'),
    path(r'prob.html', prob.get_prob, name='prob'),
    path(r'simple.html', SimpleView.as_view(), name='simple'),
    path(r'stores.html', StoreView.as_view(), name='stores'),
    path(r'pmap.html', PMapView.as_view(), name='pmap'),
    path(r'smap.html', SMapView.as_view(), name='smap'),
    path(r'pchart.html', PChartView.as_view(), name='pchart'),
]
