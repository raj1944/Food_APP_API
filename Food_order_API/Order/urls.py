from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet

urlpatterns = [
    path('get/<int:id>', OrderViewSet.as_view()),
    path('create/', OrderViewSet.as_view()),
    path('get/', OrderViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]