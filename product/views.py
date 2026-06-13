from django.shortcuts import render
from django.views.generic import DetailView
from product.models import Product
# |=========================================================|
from .models import Product, Size, Color
from .serializers import PrDetailSerializer, ColorSerializer, SizeSerializer
from .permissions import IsPublisherOrReadOnly
from .paginations import StandardResulteSetPagination
# |=========================================================|
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
# |=========================================================|
                            # APIDetail
class ProductApiDeView(APIView):
    serializer_class = PrDetailSerializer
    permission_classes =(IsAuthenticated, IsPublisherOrReadOnly)
    parser_classes = (MultiPartParser,)

    def get_object(self):
        obj = get_object_or_404(Product.objects.all(), id = self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
                
    def get(self, request, pk):
        obj = self.get_object()
        serializer = PrDetailSerializer(instance=obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        obj = self.get_object()
        serializer = PrDetailSerializer(data = request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        obj = self.get_object()
        obj.delete()
        return Response({'response':'done'}, status=status.HTTP_200_OK)
    
                        # AllProductViewSetAPI
class AllProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PrDetailSerializer
    pagination_class = StandardResulteSetPagination
# |===============================================================|
                        # APIColor

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
# |===============================================================|
                        # APISize

class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
# |================================================================|
                        # ProductDetailView

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
