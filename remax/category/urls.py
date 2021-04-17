from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Category, CategoryPostList, CategoryGetList, CategoryDetail
urlpatterns = [
    path('getcategories/', CategoryGetList.as_view()),
    path('postcategories/', CategoryPostList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
]