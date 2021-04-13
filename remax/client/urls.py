from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientLocationViewSet, ClientPhoneViewSet
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'client-location', ClientLocationViewSet, basename='client-location')
router.register(r'client-phone', ClientPhoneViewSet, basename='client-phone')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]