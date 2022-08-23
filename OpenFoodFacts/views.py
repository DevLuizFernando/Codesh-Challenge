from rest_framework import viewsets, filters
from OpenFoodFacts.models import Produto
from .serializer import ProdutoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibe todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['id', 'product_name', 'barcode', 'code']
