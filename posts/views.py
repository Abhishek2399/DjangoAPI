from .serializers import PostSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Post
# Create your views here.
# Creating class based views


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    