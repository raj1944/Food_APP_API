from django.urls import include, path
from rest_framework import routers
from .views import FoodList, FoodRetrieve, FoodUpdate, FoodDelete, FoodCreate
from .views import MenuList, MenuRetrieve, MenuUpdate, MenuDelete, MenuCreate

urlpatterns = [
    path('get/', FoodList.as_view()),
    path('create/', FoodCreate.as_view()),
    path('get/<int:pk>', FoodRetrieve.as_view()),
    path('update/<int:pk>', FoodUpdate.as_view()),
    path('delete/<int:pk>', FoodDelete.as_view()),
    path('menu/get/', MenuList.as_view()),
    path('menu/create/', MenuCreate.as_view()),
    path('menu/get/<int:pk>', MenuRetrieve.as_view()),
    path('menu/update/<int:pk>', MenuUpdate.as_view()),
    path('menu/delete/<int:pk>', MenuDelete.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]