from django.urls import path , include

from .views import PostList  , PostDetail

urlpatterns = [
    path('<int:pk>/' , PostDetail.as_view()),
    path('', PostList.as_view()),
    path('api-auth/' , include('rest_framework.urls')),
]