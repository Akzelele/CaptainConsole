from django import forms
from django_countries.fields import CountryField


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    country = CountryField().formfield()
    street_name = forms.CharField()
    house_number = forms.CharField()
    city = forms.CharField()
    zip = forms.CharField()
