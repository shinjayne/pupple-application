from django.urls import path
from components import views

urlpatterns = [
    path('<int:pk>/', views.component_to_response, name='component_to_response'),
]