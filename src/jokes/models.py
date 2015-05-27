from django.db import models
from django.core.urlresolvers import reverse


class TimeStampBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Joke(TimeStampBaseModel):
    text = models.TextField()

    def get_avg_humor_score(self):
        score = float(0)
        ratings_set = self.jokerating_set.exclude(humor_score__isnull=True)
        ratings_set_length = len(ratings_set)
        for rating in ratings_set:
            score += rating.humor_score
        if ratings_set_length > 0:
            return score/len(ratings_set)
        else:
            return 0

    def get_avg_taboo_score(self):
        score = float(0)
        ratings_set = self.jokerating_set.exclude(taboo_score__isnull=True)
        ratings_set_length = len(ratings_set)
        for rating in ratings_set:
            score += rating.taboo_score
        if ratings_set_length > 0:
            return score/len(ratings_set)
        else:
            return 0

    def get_absolute_url(self):
        return reverse('joke_detail', args=[self.id])

    def __unicode__(self):
        return self.text

class JokeRating(TimeStampBaseModel):
    joke = models.ForeignKey('Joke')
    humor_score = models.PositiveSmallIntegerField(blank=True, null=True)
    taboo_score = models.PositiveSmallIntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('joke_detail', args=[self.joke.id])

    def __unicode__(self):
        return "{0} - h:{1} t:{2}".format(self.joke, self.humor_score, self.taboo_score)

# Create your models here.
