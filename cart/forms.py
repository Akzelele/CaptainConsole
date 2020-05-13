from django import forms
from django.forms import widgets
from django_countries.fields import CountryField


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    country = CountryField().formfield()
    street_name = forms.CharField(max_length=255)
    house_number = forms.IntegerField(min_value=0, max_value=100000)  # thank you UK for min and Brazil for max
    city = forms.CharField(max_length=255)
    zip = forms.CharField(max_length=10)


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
    cardholder_name = forms.CharField(max_length=255)
    card_number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Card Number'}))
    expiration_date_month = forms.ChoiceField(choices=MONTHS)
    expiration_date_year = forms.CharField(max_length=4)
    CVC = forms.CharField(max_length=3)

    # widgets numberinput
