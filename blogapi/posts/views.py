from django.shortcuts import render
from rest_framework import generics  
# permissions need to add

from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListAPIView):
    #permission_class = (permissions.IsAuthenticated , )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_class = (permissions.IsAuthenticated , )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
