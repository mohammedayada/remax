from django.urls import path, include
from .views import ItemDetail, ItemGetList, BrandPostList

urlpatterns = [
    path('getitems/', ItemGetList.as_view()),
    path('postitems/', BrandPostList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
]