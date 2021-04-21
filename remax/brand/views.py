from .serializer import Brand, BrandSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# To get all brands
class BrandGetList(APIView):
    """
    List all brands, or create a new brand.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


# To post brands
class BrandPostList(APIView):
    """
    List all brands, or create a new brand.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a brand instance.
class BrandDetail(APIView):
    """
    Retrieve, update or delete a brand instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
