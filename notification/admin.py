from django.contrib import admin
from .models import (
    CustomUser,
    Role,
    Department,
    Position,
    UserStatus,
    Work,
    WorkStatus,
    WorkPriority,
    Service,
    Server,
    ServerType,
    Location,
    OperatingSystem,
    ServiceType,
    ServiceDependency,
    WorkLog,
    Notification,
)

# Регистрация всех моделей в админке
models = [
    CustomUser,
    Role,
    Department,
    Position,
    UserStatus,
    Work,
    WorkStatus,
    WorkPriority,
    Service,
    Server,
    ServerType,
    Location,
    OperatingSystem,
    ServiceType,
    ServiceDependency,
    WorkLog,
    Notification,
]

for model in models:
    admin.site.register(model)
