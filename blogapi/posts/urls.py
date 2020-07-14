from django.urls import path , include
from rest_framework.routers import SimpleRouter

#from .views import PostList  , PostDetail , UserDetail , UserList

from .views import PostView , UserView
#urlpatterns = [
    #path('users/' , UserList.as_view()),
    #path('users/<int:pk>/' , UserDetail.as_view()),
    #path('<int:pk>/' , PostDetail.as_view()),
    #path('', PostList.as_view()),
    #path('api-auth/' , include('rest_framework.urls')),
#]

router = SimpleRouter()

router.register('users' , UserView , base_name='users')
router.register('',PostView , base_name='posts')

urlpatterns = router.urls
