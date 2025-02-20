#app/urls.py
from django.urls import path, include
from django.contrib import admin

from tenant.admin import tenant_admin_site
from .views import custom_404

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tenants/', tenant_admin_site.urls),
    path('', include('core.urls')),
]
