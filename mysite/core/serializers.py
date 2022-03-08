# serialize model tags to provide to apline.js on the frontend
from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from core.models import Film


class FilmSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    tags = TagListSerializerField()
    
    class Meta:
        model = Film
        fields = ('id', 'name', 'director',)

        