from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions

from academy_api.permissions import IsAdminOrReadOnly
from .models import Instructor
from .serializers import InstructorSerializer


class InstructorList(generics.ListCreateAPIView):
    """
    List all Instructors.
    No create view as Instructor creation is handled by django signals.
    """
    queryset = Instructor.objects.order_by('-created_at')
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = InstructorSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'featured',
    ]


class InstructorDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update an Instructor if you're the owner.
    """
    queryset = Instructor.objects.order_by('-created_at')
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = InstructorSerializer
