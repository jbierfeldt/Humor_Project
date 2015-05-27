from django.conf.urls import include, url
from django.contrib import admin

from jokes.views import TestView, RandomJokeDetailView, JokeDetailView, JokeCreateView, JokeRatingCreateView, RandomizedStudy

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RandomJokeDetailView.as_view(), name='home'),
    url(r'^joke/(?P<joke_id>\d+)/$', JokeDetailView.as_view(), name='joke_detail'),
    url(r'^joke/(?P<joke_id>\d+)/rate/$', JokeRatingCreateView.as_view(), name='jokerating_create'),
    url(r'^joke/create/$', JokeCreateView.as_view(), name='joke_create'),
    url(r'^survey/$', RandomizedStudy.as_view(), name='survey'),
]
