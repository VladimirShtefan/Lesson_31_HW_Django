from rest_framework.permissions import BasePermission


class AdOwnerPermission(BasePermission):
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.role in ('admin', 'moderator')
