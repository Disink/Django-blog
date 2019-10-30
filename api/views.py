from django.shortcuts import render

from blog.models import Post, Comment, Tag

from rest_framework import viewsets
from .serializers import PostSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-pk')
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
