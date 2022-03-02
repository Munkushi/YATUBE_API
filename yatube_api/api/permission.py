from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerOrReadOnly(BasePermission):
    """Пермишн на запрос/проверку на автора."""

    def has_object_permission(self, request, view, obj):
        if (request.method in SAFE_METHODS
                or obj.author == request.user):
            return True
