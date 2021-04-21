from django.urls import path, include
from .views import (
    ItemDetail,
    ItemGetList,
    ItemPostList,
    ItemImgPostList,
    ItemImgGetList,
    ItemImgForItem,
)

urlpatterns = [
    path('getitems/', ItemGetList.as_view()),
    path('postitems/', ItemPostList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
    path('getitemsimgs/', ItemImgGetList.as_view()),
    path('postitemsimgs/', ItemImgPostList.as_view()),
    path('itemimgs/<int:pk>/',  ItemImgForItem.as_view()), #get all imgs for pk of item

]