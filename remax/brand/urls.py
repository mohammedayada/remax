from django.urls import path, include
from .views import BrandGetList, BrandPostList, BrandDetail

urlpatterns = [

    path('getbrands/', BrandGetList.as_view()),
    path('postbrands/', BrandPostList.as_view()),
    path('brands/<int:pk>/', BrandDetail.as_view()),

]