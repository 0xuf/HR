from rest_framework import permissions


class IsTargetOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if obj.user.id == request.user.id else False

