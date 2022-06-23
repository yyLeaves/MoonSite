from django.urls import path
import country, sentiment, delivery
from app.views import (
    DefaultFormByFieldView,
    DefaultFormsetView,
    DefaultFormView,
    FormHorizontalView,
    FormInlineView,
    FormWithFilesView,
    HomePageView,
    MiscView,
    PaginationView,
    SentimentAnalysis,
    CountryView,
    PickCountryView,
    ArticleView,
    BarGraphView,
    RankGraphView,
    DeliveryView
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
    path(r'delivery.html', delivery.calc)
]
