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

    def get_object(self, queryset=None):
        jokes = Joke.objects.filter(approved=True) #only get approved jokes
        random_idx = random.randint(0, jokes.count() - 1)
        obj = jokes[random_idx]
        return obj

    def get_initial(self):
        self.joke = self.get_object()
        return { 'joke': self.joke }

    def post(self, request, **kwargs):
        self.request.POST = request.POST.copy()
        if 'gender' in self.request.session:
            self.request.POST['gender'] = self.request.session['gender']
            self.request.POST['age'] = self.request.session['age']
        return super(RandomizedStudy, self).post(request, **kwargs)

    def form_valid(self, form):
        if 'gender' in form.cleaned_data:
            self.request.session['gender'] = form.cleaned_data['gender']
            self.request.session['age'] = form.cleaned_data['age']
        return super(RandomizedStudy, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # # Call the base implementation first to get a context
        context = super(RandomizedStudy, self).get_context_data(**kwargs)
        CHOICES_SETS = [['humor_score', 'taboo_score', 'taboo_rating_score'], ['humor_score', 'taboo_score'], ['humor_score', 'taboo_rating_score'], ['taboo_score', 'taboo_rating_score'], ['taboo_rating_score'], ['humor_score'], ['taboo_score']]
        context['field_list'] = random.choice(CHOICES_SETS)
        context['joke'] = self.joke
        return context

    def get_success_url(self): 
            return reverse('survey') 

class TestView(TemplateView):
    template_name = "jokes/slider.html"

# Create your views here.
