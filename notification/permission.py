from rest_framework import permissions


class IsAdminOrEditor(permissions.BasePermission):
    """
    Разрешает доступ только администратору и редакторам.
    """

    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name='Editor').exists())


class IsAdmin(permissions.BasePermission):
    """
    Разрешает доступ только администраторам.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
