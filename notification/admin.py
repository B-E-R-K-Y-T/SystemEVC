from django.contrib import admin
from .models import Work, WorkStatus, WorkPriority, Service, Server, ServerType, Location, OperatingSystem, ServiceType, ServiceDependency, WorkLog, Notification

admin.site.register(Work)
admin.site.register(WorkStatus)
admin.site.register(WorkPriority)
admin.site.register(Service)
admin.site.register(Server)
admin.site.register(ServerType)
admin.site.register(Location)
admin.site.register(OperatingSystem)
admin.site.register(ServiceType)
admin.site.register(ServiceDependency)
admin.site.register(WorkLog)
admin.site.register(Notification)
