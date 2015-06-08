from django.contrib import admin
from jokes.models import Joke, JokeRating

class JokeAdmin(admin.ModelAdmin):
    list_display = ('text', 'approved', 'get_avg_humor_score', 'get_avg_taboo_score', 'get_avg_taboo_rating_score')
    pass
class JokeRatingAdmin(admin.ModelAdmin):
    list_display = ('joke', 'humor_score', 'taboo_score', 'taboo_rating_score')
    pass
admin.site.register(Joke, JokeAdmin)
admin.site.register(JokeRating, JokeRatingAdmin)
