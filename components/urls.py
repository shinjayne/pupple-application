from django.urls import path
from components import views

urlpatterns = [
    path('<int:pk>/', views.get_component, name='get_component'),
    path('vote/choice/<int:pk>/', views.vote_component_choice_increase, name='vote_component_choice_increase')
]