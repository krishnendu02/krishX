from django import forms
from .models import Tweet


class tweetForm(forms.ModelForm):
    class meta:
        model = tweetFormfields = ['text', 'photo']