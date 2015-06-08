from django.contrib import admin
from jokes.models import Joke, JokeRating
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class JokeResource(resources.ModelResource):

	class Meta:
		model = Joke

class JokeAdmin(ImportExportModelAdmin):
    list_display = ('text', 'approved', 'get_avg_humor_score', 'get_avg_taboo_score')
    resource_class = JokeResource
    pass

class JokeRatingResource(resources.ModelResource):

	class Meta:
		model = JokeRating

class JokeRatingAdmin(ImportExportModelAdmin):
    list_display = ('joke', 'humor_score', 'taboo_score')
    resource_class = JokeRatingResource
    pass

admin.site.register(Joke, JokeAdmin)
admin.site.register(JokeRating, JokeRatingAdmin)
