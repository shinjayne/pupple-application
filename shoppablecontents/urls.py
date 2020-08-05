from django.urls import path
from shoppablecontents import views

urlpatterns = [
    path('', views.test_contents),
]