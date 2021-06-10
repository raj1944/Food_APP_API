from django.urls import include, path
from rest_framework import routers
from .views import RestaurantViewSet, BranchViewSet, FoodViewSet, MenuViewSet, OrderViewSet, UserViewSet


urlpatterns = [
    path('menu/add/', MenuViewSet.as_view()),
    path('menu/update/<id>', MenuViewSet.as_view()),
    path('order/', OrderViewSet.as_view()),
    path('order/<id>', OrderViewSet.as_view()),

    path('user/', UserViewSet.as_view()),
    path('user/<id>', UserViewSet.as_view()),
    path('restaurant/', RestaurantViewSet.as_view()),
    path('restaurant/<id>', RestaurantViewSet.as_view()),
    path('branch/', BranchViewSet.as_view()),
    path('branch/<id>', BranchViewSet.as_view()),
    path('food/', FoodViewSet.as_view()),
    path('food/<id>/', FoodViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]