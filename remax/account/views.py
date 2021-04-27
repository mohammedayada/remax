from .serializer import Account, AccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
# To get and post all Accounts
class AccountList(APIView):
    """
    List all Accounts, or create a new Account.
    """
    permission_classes = [IsAdminUser]



    def get(self, request, format=None):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            if 'password' in request.data:
                password = make_password(request.data['password'])
                is_active = True
                is_staff = True
                serializer.save(password=password, is_active=is_active, is_staff=is_staff)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Account instance.
class AccountDetail(APIView):
    """
    Retrieve, update or delete a Account instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if request.user.id != account.id and not request.user.is_superuser:
            raise Http404
        if serializer.is_valid():
            if 'password' in request.data:
                password = make_password(request.data['password'])
                serializer.save(password=password)
                return Response(serializer.data)
            else:
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if not request.user.is_superuser:
            raise Http404

        account = self.get_object(pk)
        logout(request)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
