from apps.user.api.views import register_api
from django.urls import path

urlpatterns = [
    path('register/', register_api)
]
