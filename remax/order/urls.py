from django.urls import path, include
from .views import (
    OrderPostList,
    OrderGetList,
    OrderDetail,
    OrderItemPostList,
    OrderItemGetList,
    OrderItemDetail,
    GetAllOrderItemsById,
    GetAllOrdersByClientId,
)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('getorders/', OrderGetList.as_view()),
    path('postorders/', OrderPostList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('getordersbyclientid/<int:pk>/', GetAllOrdersByClientId.as_view()),

    path('getorderitems/', OrderItemGetList.as_view()),
    path('postorderitems/', OrderItemPostList.as_view()),
    path('orderitems/<int:pk>/', OrderItemDetail.as_view()),
    path('orderitemsbyid/<int:pk>/', GetAllOrderItemsById.as_view()),
]