from django.contrib.auth.models import User
from django.db import models

from categories.models import Category


class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    short_bio = models.TextField(max_length=1000, null=True, default=None)
    full_bio = models.TextField(max_length=10000, null=True, default=None)
    email = models.EmailField(null=True, default=None)
    profile_image = models.ImageField(
        upload_to='instructor-images/', default='../default-instructor', blank=True
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    def __str__(self):
        return f"{self.title}"


class InstructorSpeciality(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="specialities"
    )
    description = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
