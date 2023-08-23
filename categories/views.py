from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions

from academy_api.permissions import IsAdminOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    List all Categories.
    No create view as Category creation is handled by django signals.
    """
    queryset = Category.objects.order_by('-created_at')
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'featured',
    ]


class CategoryDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a Category if you're the owner.
    """
    queryset = Category.objects.order_by('-created_at')
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
