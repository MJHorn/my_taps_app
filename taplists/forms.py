from django import forms
from .models import Tap
from .models import Bar

CHOICES = (
(0, 'Two Row'),
(1, 'Little Hop'),
(2, 'Up in Smoke'),
)

class TapForm(forms.Form):

    letters = forms.MultipleChoiceField(
            choices=CHOICES, 
            label="...", 
            required=False)


class StyleForm(forms.Form):

    letters = forms.MultipleChoiceField(
            choices=CHOICES,
            label="...",
            required=False)
