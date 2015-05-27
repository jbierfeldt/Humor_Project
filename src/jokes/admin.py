from django.contrib import admin
from jokes.models import Joke, JokeRating

class JokeAdmin(admin.ModelAdmin):
    pass
class JokeRatingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Joke, JokeAdmin)
admin.site.register(JokeRating, JokeRatingAdmin)
