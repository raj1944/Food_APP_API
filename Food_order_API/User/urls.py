from django.urls import include, path
from rest_framework import routers
from .views import UserList, UserRetrieve, UserUpdate, UserDelete, UserCreate

urlpatterns = [
    path('get/', UserList.as_view()),
    path('create/', UserCreate.as_view()),
    path('get/<int:pk>', UserRetrieve.as_view()),
    path('update/<int:pk>', UserUpdate.as_view()),
    path('delete/<int:pk>', UserDelete.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]