"""
URL configuration for prueba_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import JsonResponse
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from os import environ
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

def health_check(_):
    return JsonResponse({"status":"OK. server running", "environment": environ.get('ENV','dev')})


urlpatterns = [
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="Ristoran API",
        description="API para el manejo de restaurantes dentro de una zona geo espacial.",
        version="1.0.0"
    ), name='openapi-schema'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('ristoranApi.urls', namespace='ristoran'), name='ristoranApi'),
    path('health_check/', health_check, name='health_check'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]
