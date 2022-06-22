from django.urls import path
import country, sentiment
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
    BarGraphView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # path("formset", DefaultFormsetView.as_view(), name="formset_default"),
    # path("form", DefaultFormView.as_view(), name="form_default"),
    # path("form_by_field", DefaultFormByFieldView.as_view(), name="form_by_field"),
    # path("form_horizontal", FormHorizontalView.as_view(), name="form_horizontal"),
    # path("form_inline", FormInlineView.as_view(), name="form_inline"),
    # path("form_with_files", FormWithFilesView.as_view(), name="form_with_files"),
    # path("pagination", PaginationView.as_view(), name="pagination"),
    # path("misc", MiscView.as_view(), name="misc"),
    path("sentiment", SentimentAnalysis.as_view(), name='sentiment'),
    path(r'sentiment.html', sentiment.analyse),
    path(r'country-sentiment.html', sentiment.analyse),
    path("country", CountryView.as_view(), name='country'),
    path(r"country.html", sentiment.analyse_countries),
    path(r'pick-country', PickCountryView.as_view(), name='pick-country'),
    path(r'pick-country.html', country.pick_countries),
    path(r'article', ArticleView.as_view(), name='article'),
    path(r'article.html', ArticleView.as_view(), name='article'),
    path(r'Bar.html', BarGraphView.as_view())
]
