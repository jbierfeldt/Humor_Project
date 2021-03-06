from django.db import models
from django.core.urlresolvers import reverse


class TimeStampBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Joke(TimeStampBaseModel):
    text = models.TextField()
    approved = models.BooleanField(default=False)

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
    get_avg_humor_score.short_description = 'AVG Humor'

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
    get_avg_taboo_score.short_description = 'AVG Offensive'

    def get_avg_taboo_rating_score(self):
        score = float(0)
        ratings_set = self.jokerating_set.exclude(taboo_rating_score__isnull=True)
        ratings_set_length = len(ratings_set)
        for rating in ratings_set:
            score += rating.taboo_rating_score
        if ratings_set_length > 0:
            return score/len(ratings_set)
        else:
            return 0
    get_avg_taboo_rating_score.short_description = 'AVG Taboo'

    def get_absolute_url(self):
        return reverse('joke_detail', args=[self.id])

    def __unicode__(self):
        return self.text

class JokeRating(TimeStampBaseModel):
    joke = models.ForeignKey('Joke')
    humor_score = models.PositiveSmallIntegerField(blank=True, null=True)
    taboo_score = models.PositiveSmallIntegerField(blank=True, null=True)
    taboo_rating_score = models.PositiveSmallIntegerField(blank=True, null=True)

    gender = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('joke_detail', args=[self.joke.id])

    def __unicode__(self):
        return str(self.joke_id)

# Create your models here.
