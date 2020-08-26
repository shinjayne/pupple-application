from django.urls import path
from accounts import views

urlpatterns = [
    path('ip/', views.get_ip_user, name='get_ip_user')
]