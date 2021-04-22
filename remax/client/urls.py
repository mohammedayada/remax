from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientGetList,
    ClientPostList,
    ClientDetail,
    ClientPhoneGetList,
    ClientPhonePostList,
    ClientPhoneDetail,
    GetAllClientPhonesById,
    ClientLocationGetList,
    ClientLocationPostList,
    ClientLocationDetail,
    GetAllClientLocationsById,
)



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('getclients/', ClientGetList.as_view()),
    path('postclients/', ClientPostList.as_view()),
    path('clients/<int:pk>/', ClientDetail.as_view()),

    path('getclientphones/', ClientPhoneGetList.as_view()),
    path('postclientphones/', ClientPhonePostList.as_view()),
    path('clientphones/<int:pk>/', ClientPhoneDetail.as_view()),
    path('clientphonesbyid/<int:pk>/', GetAllClientPhonesById.as_view()),

    path('getclientlocations/', ClientLocationGetList.as_view()),
    path('postclientlocations/', ClientLocationPostList.as_view()),
    path('clientlocations/<int:pk>/', ClientLocationDetail.as_view()),
    path('clientlocationsbyid/<int:pk>/', GetAllClientLocationsById.as_view()),
]
