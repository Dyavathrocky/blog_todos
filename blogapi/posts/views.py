from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics  , viewsets
# permissions need to add

from .models import Post
from .serializers import PostSerializer , UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

""" class PostList(generics.ListAPIView):
    #permission_class = (permissions.IsAuthenticated , )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly , )
    #permission_class = (permissions.IsAuthenticated , )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer """


class PostView(viewsets.ModelViewSet):
    permission_class = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    #added routers