from django.urls import path
from components import views

urlpatterns = [
    path('<int:pk>/', views.get_component, name='get_component'),
    path('vote/choice/<int:pk>/', views.vote_component_choice_increase, name='vote_component_choice_increase'),
    path('comment/create/<int:pk>/', views.comment_create, name='comment_create'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('comment/like/<int:pk>/', views.comment_like_increase, name='comment_like_increase'),
    path('comment/unlike/<int:pk>/', views.comment_like_decrease, name='comment_like_decrease')
]