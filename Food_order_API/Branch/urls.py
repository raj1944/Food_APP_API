from django.urls import include, path
from rest_framework import routers
from .views import BranchList, BranchRetrieve, BranchUpdate, BranchDelete, BranchCreate

urlpatterns = [
    path('get/', BranchList.as_view()),
    path('create/', BranchCreate.as_view()),
    path('get/<int:pk>', BranchRetrieve.as_view()),
    path('update/<int:pk>', BranchUpdate.as_view()),
    path('delete/<int:pk>', BranchDelete.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]