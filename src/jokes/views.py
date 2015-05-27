import random

from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from jokes.models import Joke, JokeRating
from jokes.forms import JokeRatingForm

class JokeCreateView(CreateView):
    
    model = Joke
    fields = ['text']
    template_name_suffix = '_create'

    def form_valid(self, form):
        return super(JokeCreateView, self).form_valid(form)

class JokeRatingCreateView(CreateView):
    
    model = JokeRating
    form_class = JokeRatingForm
    template_name_suffix = '_create'

    def get_object(self, queryset=None):
        obj = Joke.objects.get(pk=self.kwargs['joke_id'])
        return obj

    def get_initial(self):
        return { 'joke': self.get_object() }

    def get_context_data(self, **kwargs):
        # # Call the base implementation first to get a context
        context = super(JokeRatingCreateView, self).get_context_data(**kwargs)
        context['joke'] = self.get_object()
        return context

class JokeDetailView(DetailView):
    
    model = Joke
    
    def get_object(self, queryset=None):
        obj = Joke.objects.get(pk=self.kwargs['joke_id'])
        print type(obj)
        return obj
          
    def get_context_data(self, **kwargs):
        # # Call the base implementation first to get a context
        context = super(JokeDetailView, self).get_context_data(**kwargs)
        context['joke'] = self.get_object()
        return context

class RandomJokeDetailView(DetailView):
    
    model = Joke
    
    def get_object(self, queryset=None):
        random_idx = random.randint(0, Joke.objects.count() - 1)
        obj = Joke.objects.all()[random_idx]
        return obj
          
    def get_context_data(self, **kwargs):
        # # Call the base implementation first to get a context
        context = super(RandomJokeDetailView, self).get_context_data(**kwargs)
        context['joke'] = self.get_object()
        return context

class RandomizedStudy(CreateView):

    model = JokeRating
    form_class = JokeRatingForm
    template_name_suffix = '_create'
    print "hey"

    def get_object(self, queryset=None):
        random_idx = random.randint(0, Joke.objects.count() - 1)
        obj = Joke.objects.all()[random_idx]
        return obj

    def get_initial(self):
        return { 'joke': self.get_object() }

    def get_context_data(self, **kwargs):
        # # Call the base implementation first to get a context
        context = super(RandomizedStudy, self).get_context_data(**kwargs)
        CHOICES_SETS = [['humor_score', 'taboo_score', 'punchline'], ['humor_score', 'punchline'], ['taboo_score', 'punchline']]
        context['field_list'] = random.choice(CHOICES_SETS)
        context['joke'] = self.get_object()
        return context

    def get_success_url(self): 
            return reverse('survey') 

class TestView(TemplateView):
    template_name = "jokes/slider.html"

# Create your views here.
