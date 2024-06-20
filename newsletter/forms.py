# newsletter/forms.py
from django import forms


class NewsletterSignupForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    default_email = forms.EmailField(widget=forms.HiddenInput(), initial='default@example.com')
