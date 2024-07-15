from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsNotMember(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied("You are not authenticated.")

        if request.user.is_member():
            raise PermissionDenied("You are not authorized to perform this action.")

        return not request.user.is_member()

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            raise PermissionDenied("You are not authenticated.")

        if request.user.is_member():
            raise PermissionDenied("You are not authorized to perform this action.")

        return not request.user.is_member()
