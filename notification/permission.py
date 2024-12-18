from rest_framework import permissions

from notification.models import CustomUser


class IsAdminOrEditor(permissions.BasePermission):
    """
    Разрешает доступ только администратору и редакторам.
    """

    def has_permission(self, request, view):
        # Проверяем, есть ли у пользователя аутентификация
        if request.user.is_authenticated:
            # Проверяем, является ли пользователь staff (администратором)
            if request.user.is_staff:
                return True

            # Проверяем, есть ли у пользователя роль редактора
            try:
                custom_user = (
                    request.user.customuser
                )  # Предполагаем, что связь OneToOne с CustomUser
                return custom_user.role and custom_user.role.name == "Editor"
            except CustomUser.DoesNotExist:
                return (
                    False  # Если у пользователя нет соответствующей записи в CustomUser
                )
        return False  # Если пользователь не аутентифицирован


class IsAdmin(permissions.BasePermission):
    """
    Разрешает доступ только пользователям с ролью администратора.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        if request.user and request.user.is_authenticated:
            # Получаем связанного пользователя CustomUser
            try:
                custom_user = request.user.customuser
                # Проверяем, является ли роль пользователя 'Администратор'
                return custom_user.role.name == "Admin"
            except CustomUser.DoesNotExist:
                return False

        return False
