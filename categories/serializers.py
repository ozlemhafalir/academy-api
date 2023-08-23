from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
            'icon',
            'parent',
            'slug',
            'featured',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
