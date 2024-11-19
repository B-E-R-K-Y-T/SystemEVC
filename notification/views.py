from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    WorkStatus, WorkPriority, Work, Service, Server, ServerType,
    Location, OperatingSystem, ServiceType, ServiceDependency,
    WorkLog, Notification
)
from .permission import IsAdminOrEditor, IsAdmin
from .serializers import (
    WorkStatusSerializer, WorkPrioritySerializer, WorkSerializer,
    ServiceSerializer, ServerSerializer, ServerTypeSerializer,
    LocationSerializer, OperatingSystemSerializer, ServiceTypeSerializer,
    ServiceDependencySerializer, WorkLogSerializer, NotificationSerializer
)


class WorkStatusViewSet(viewsets.ModelViewSet):
    queryset = WorkStatus.objects.all()
    serializer_class = WorkStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class WorkPriorityViewSet(viewsets.ModelViewSet):
    queryset = WorkPriority.objects.all()
    serializer_class = WorkPrioritySerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class ServerTypeViewSet(viewsets.ModelViewSet):
    queryset = ServerType.objects.all()
    serializer_class = ServerTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class ServiceDependencyViewSet(viewsets.ModelViewSet):
    queryset = ServiceDependency.objects.all()
    serializer_class = ServiceDependencySerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()


class WorkLogViewSet(viewsets.ModelViewSet):
    queryset = WorkLog.objects.all()
    serializer_class = WorkLogSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST']:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrEditor]
        return super().get_permissions()
