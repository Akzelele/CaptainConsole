from django import forms
from django.forms import widgets
from django_countries.fields import CountryField


class ContactForm(forms.Form):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "First name"}), max_length=255)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Last name"}), max_length=255)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': "Email"}), max_length=255)
    country = CountryField(blank_label='Select country').formfield(label='')
    street_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Street name"}), max_length=255)
    house_number = forms.IntegerField(
        min_value=0, label="", max_value=100000, widget=forms.NumberInput(attrs={'placeholder':'House number'}))
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "City"}), max_length=255)
    zip = forms.CharField(label="", widget=forms.NumberInput(attrs={'placeholder': 'Zip code'}), max_length=10)


class PaymentForm(forms.Form):
    MONTHS = (
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    )
    cardholder_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Cardholder's name"}),
                                      max_length=255)
    card_number = forms.CharField(min_length=16, max_length=16, label="",
                                  widget=forms.NumberInput(attrs={'placeholder': 'Card number'}))
    expiration_month = forms.ChoiceField(choices=MONTHS, label="", widget=forms.Select())
    expiration_year = forms.CharField(label="", widget=forms.NumberInput(attrs={'placeholder': '2020'}), max_length=4)
    CVC = forms.CharField(label="", widget=forms.NumberInput(attrs={'placeholder': 'CVC'}), max_length=3)
