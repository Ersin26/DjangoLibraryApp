from django.contrib import admin
from django.urls import path, include

API_PREFIX = "v1"

urlpatterns = [
    path('admin/', admin.site.urls),

    path(f'api/{API_PREFIX}/user/', include('apps.user.api.urls')),
    path(f'api/{API_PREFIX}/library/', include('apps.library.api.urls')),
]
