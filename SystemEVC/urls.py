"""
URL configuration for SystemEVC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from notification.views import (
    WorkStatusViewSet,
    WorkPriorityViewSet,
    WorkViewSet,
    ServiceViewSet,
    ServerViewSet,
    ServerTypeViewSet,
    LocationViewSet,
    OperatingSystemViewSet,
    ServiceTypeViewSet,
    ServiceDependencyViewSet,
    WorkLogViewSet,
    NotificationViewSet,
    CustomUserRegistrationView,
)

router = DefaultRouter()
router.register(r"work-statuses", WorkStatusViewSet)
router.register(r"work-priorities", WorkPriorityViewSet)
router.register(r"works", WorkViewSet)
router.register(r"services", ServiceViewSet)
router.register(r"servers", ServerViewSet)
router.register(r"server-types", ServerTypeViewSet)
router.register(r"locations", LocationViewSet)
router.register(r"operating-systems", OperatingSystemViewSet)
router.register(r"service-types", ServiceTypeViewSet)
router.register(r"service-dependencies", ServiceDependencyViewSet)
router.register(r"work-logs", WorkLogViewSet)
router.register(r"notifications", NotificationViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("auth/register/", CustomUserRegistrationView.as_view(), name="api_register"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
