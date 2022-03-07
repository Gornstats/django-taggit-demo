from django.contrib import admin
from core.models import Film

# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'get_tags',)
    list_filter = ('tags', 'director',)
    search_fields = ('name', 'director',)
    
    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())

