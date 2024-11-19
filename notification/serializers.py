from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    WorkStatus,
    WorkPriority,
    Work,
    Service,
    Server,
    ServerType,
    Location,
    OperatingSystem,
    ServiceType,
    ServiceDependency,
    WorkLog,
    Notification,
    UserStatus,
    Role,
    Position,
    Department,
    CustomUser,
)


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = "__all__"  # Или укажите конкретные поля, например: ['id', 'name', 'description']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"  # Или укажите конкретные поля


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"  # Или укажите конкретные поля


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"  # Или укажите конкретные поля


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"  # Или укажите конкретные поля для вашего пользователя


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "full_name",
            "password",
            "role",
            "department",
            "position",
            "status",
        ]

    def create(self, validated_data):
        # Извлечение данных для создания User
        username = validated_data['username']
        email = validated_data['email']
        full_name = validated_data.pop('full_name')

        # Разделите full_name на first_name и last_name, как вам нужно
        first_name, *last_name = full_name.split()
        last_name = ' '.join(last_name)  # Объединение оставшихся частей в фамилию, если необходимо

        # Проверка существования пользователя с таким же username
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Пользователь с таким именем уже существует."})

        # Проверка существования пользователя с таким же email
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Пользователь с таким email уже существует."})

        # Создание объекта User
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(validated_data.pop("password"))  # Установка зашифрованного пароля
        user.save()  # Сохранение объекта User

        # Создание экземпляра CustomUser с объектом User
        custom_user = CustomUser.objects.create(user=user, full_name=full_name, **validated_data)
        return custom_user


class WorkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStatus
        fields = "__all__"


class WorkPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPriority
        fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"


class ServerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerType
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = "__all__"


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDependency
        fields = "__all__"


class WorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLog
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
