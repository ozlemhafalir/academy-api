from rest_framework import serializers
from .models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'name',
            'surname',
            'title',
            'slug',
            'short_bio',
            'full_bio',
            'email',
            'profile_image',
        ]
