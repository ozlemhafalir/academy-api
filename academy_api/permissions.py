from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin
