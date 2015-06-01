import random

from django import forms
from django.forms import ModelForm

from jokes.models import Joke, JokeRating

from jokes.widgets import SliderWidget

class JokeRatingForm(ModelForm):
	CHOICES = (('0', 'Male',), ('1', 'Female',), ('2', 'Other',))
	joke = forms.ModelChoiceField(queryset=Joke.objects.all(),
            widget=forms.HiddenInput())
	gender = forms.TypedChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False, empty_value=None)
	age = forms.IntegerField(required=False)

	class Meta:
		model = JokeRating
		fields = ['joke', 'humor_score', 'taboo_score', 'taboo_rating_score', 'gender', 'age']
		labels = {
			'humor_score' : 'How FUNNY is this Joke?',
			'taboo_score' : 'How OFFENSIVE is this Joke?',
			'taboo_rating_score' : 'How TABOO is this subject?'
		}
		widgets = {
			'humor_score' : SliderWidget(attrs={'min_value':0, 'max_value':5, 'step': 1}),
			'taboo_score' : SliderWidget(attrs={'min_value':0, 'max_value':5, 'step': 1}),
			'taboo_rating_score' : SliderWidget(attrs={'min_value':0, 'max_value':5, 'step': 1})
		}