from django.urls import path
from sentiment import analyse
import country
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
    CountryView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("formset", DefaultFormsetView.as_view(), name="formset_default"),
    path("form", DefaultFormView.as_view(), name="form_default"),
    path("form_by_field", DefaultFormByFieldView.as_view(), name="form_by_field"),
    path("form_horizontal", FormHorizontalView.as_view(), name="form_horizontal"),
    path("form_inline", FormInlineView.as_view(), name="form_inline"),
    path("form_with_files", FormWithFilesView.as_view(), name="form_with_files"),
    path("pagination", PaginationView.as_view(), name="pagination"),
    path("misc", MiscView.as_view(), name="misc"),
    path("sentiment", SentimentAnalysis.as_view(), name='sentiment'),
    path(r'sentiment.html', analyse),
    path("country", CountryView.as_view(), name='country'),
    path(r'pick-country.html', country.pick_countries),
]
