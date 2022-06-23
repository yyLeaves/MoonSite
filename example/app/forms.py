from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import BaseFormSet, TextInput, formset_factory

from django_bootstrap5.widgets import RadioSelectButtonGroup

RADIO_CHOICES = (("1", "Radio 1"), ("2", "Radio 2"))

MEDIA_CHOICES = (
    ("Audio", (("vinyl", "Vinyl"), ("cd", "CD"))),
    ("Video", (("vhs", "VHS Tape"), ("dvd", "DVD"))),
    ("unknown", "Unknown"),
)


class SentimentForm(forms.Form):
    message = forms.CharField(required=True,
                              help_text="<i>Please paste your article here</i>",
                              widget=forms.Textarea,
                              )


class CountryForm(forms.Form):
    message = forms.CharField(required=True,
                              help_text="<i>Please paste your number here</i>",
                              widget=forms.Textarea,
                              )

class PickCountryForm(forms.Form):
    message = forms.CharField(required=True,
                              help_text="<i>Please paste your number here</i>",
                              widget=forms.Textarea,
                              )

class ArticleForm(forms.Form):
    message = forms.CharField(required=True,
                              help_text="<i>Please paste your number here</i>",
                              widget=forms.Textarea,
                              )
class GraphForm(forms.Form):
    # class ArticleForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )

class DeliveryForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )

class SimpleForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )

class StoreForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )
class PMapForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )

class SMapForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )


class ProbForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )

class PChartForm(forms.Form):
    message = forms.CharField(required=True,
                                  help_text="<i>Please paste your number here</i>",
                                  widget=forms.Textarea,
                                  )