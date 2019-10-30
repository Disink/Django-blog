from rest_framework import serializers
from blog.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk',
                  'title',
                  'slug',
                  'author',
                  'summary',
                  'content',
                  'status',
                  'created_on')
