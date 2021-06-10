from django.urls import include, path
from rest_framework import routers
from .views import RestaurantList, RestaurantRetrieve, RestaurantUpdate, RestaurantDelete, RestaurantCreate

urlpatterns = [
    path('get/', RestaurantList.as_view()),
    path('create/', RestaurantCreate.as_view()),
    path('get/<int:pk>', RestaurantRetrieve.as_view()),
    path('update/<int:pk>', RestaurantUpdate.as_view()),
    path('delete/<int:pk>', RestaurantDelete.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]