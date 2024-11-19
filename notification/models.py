from django.db import models
from django.contrib.auth.models import User


# Таблица Статусы Работ
class WorkStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Таблица Приоритет Работ
class WorkPriority(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Таблица Работы
class Work(models.Model):
    title = models.CharField(max_length=255)
    work_plan = models.TextField()
    rollback_plan = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user_ids_works = models.ManyToManyField(User, related_name='works_conducted')
    user_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='works_managed')
    status = models.ForeignKey(WorkStatus, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(WorkPriority, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    duration_estimation = models.FloatField()
    dependencies = models.TextField(blank=True)  # Может быть сформатирован в JSON
    completed_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='works_last_updated')


# Таблица Сервисы
class Service(models.Model):
    name = models.CharField(max_length=255)
    internal_ip = models.GenericIPAddressField()
    port = models.IntegerField()
    url = models.URLField(blank=True)
    server = models.ForeignKey('Server', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(WorkStatus, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=255)
    service_type = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True)
    protocol = models.CharField(max_length=50)
    dependencies = models.TextField(blank=True)  # Может быть сформатирован в JSON
    health_check_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    last_maintenance_date = models.DateField(null=True, blank=True)
    version = models.CharField(max_length=50, blank=True)
    availability_zone = models.CharField(max_length=255, blank=True)


# Таблица Серверы
class Server(models.Model):
    hostname = models.CharField(max_length=255)
    server_type = models.ForeignKey('ServerType', on_delete=models.SET_NULL, null=True)
    internal_ip = models.GenericIPAddressField()
    external_ip = models.GenericIPAddressField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    os = models.ForeignKey('OperatingSystem', on_delete=models.SET_NULL, null=True)
    cpu_info = models.TextField()
    ram_size = models.CharField(max_length=50)
    disk_size = models.CharField(max_length=50)
    owner = models.CharField(max_length=255)
    notes = models.TextField(blank=True)


# Таблица Типы Серверов
class ServerType(models.Model):
    name = models.CharField(max_length=255)


# Таблица Локации Серверов
class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)


# Таблица Операционные Системы
class OperatingSystem(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)


# Таблица Типы Сервисов
class ServiceType(models.Model):
    name = models.CharField(max_length=255)


# Таблица Зависимости Сервисов
class ServiceDependency(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_dependencies')
    dependency_service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='dependent_services')
    dependency_type = models.CharField(max_length=255)


# Таблица Журнал Работ
class WorkLog(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    status = models.ForeignKey(WorkStatus, on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)


# Таблица Уведомления
class Notification(models.Model):
    message = models.TextField()
    time_long_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)
    is_read = models.BooleanField(default=False)
    external_reference = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
