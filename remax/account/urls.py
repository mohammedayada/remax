from django.urls import path, include
from .views import AccountList, AccountDetail, logedInAccount

urlpatterns = [

    path('accounts/', AccountList.as_view()),
    path('accounts/<int:pk>/', AccountDetail.as_view()),
    path('currentuser/', logedInAccount.as_view()),

]