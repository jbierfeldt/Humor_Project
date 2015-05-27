import random

from django import forms
from django.forms import ModelForm

from jokes.models import Joke, JokeRating

from jokes.widgets import SliderWidget

class JokeRatingForm(ModelForm):
	joke = forms.ModelChoiceField(queryset=Joke.objects.all(),
            widget=forms.HiddenInput())
	punchline = forms.CharField(label="What is the Punchline?", required=False)

	class Meta:
		model = JokeRating
		fields = ['joke', 'humor_score', 'taboo_score']
		labels = {
			'humor_score' : 'How funny is this Joke?',
			'taboo_score' : 'How offensive is this Joke?',
		}
		widgets = {
			'humor_score' : SliderWidget(attrs={'min_value':0, 'max_value':5, 'step': 1}),
			'taboo_score' : SliderWidget(attrs={'min_value':0, 'max_value':5, 'step': 1})
		}