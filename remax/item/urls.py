from django.urls import path, include
from .views import (
    UpdateOrDeleteItemDetail,
    GetItemDetail,
    ItemGetList,
    ItemPostList,
    ItemImgPostList,
    ItemImgGetList,
    ItemImgForItem,
    DeleteItemImg,
    ItemGetListByCategoryId,
    ItemGetListByBrandId
)

urlpatterns = [
    path('getitems/', ItemGetList.as_view()),
    path('postitems/', ItemPostList.as_view()),
    path('getitembyid/<int:pk>/', GetItemDetail.as_view()),
    path('updateordeleteitembyid/<int:pk>/', UpdateOrDeleteItemDetail.as_view()),
    path('getitembycategoryid/<int:pk>/', ItemGetListByCategoryId.as_view()),
    path('getitembybrandid/<int:pk>/', ItemGetListByBrandId.as_view()),

    path('getitemsimgs/', ItemImgGetList.as_view()),
    path('postitemsimgs/', ItemImgPostList.as_view()),
    path('itemimgs/<int:pk>/',  ItemImgForItem.as_view()), #get all imgs for pk of item
    path('itemimgsdelete/<int:pk>/', DeleteItemImg.as_view()),  # delete item img by item img id

]