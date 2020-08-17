from django.urls import path
from contents import views

urlpatterns = [
    path('<int:pk>/', views.shoppable_contents_to_response, name='shoppable_contents_to_response'),
    path('youtube/<int:pk>/', views.youtube_contents_to_response, name='youtube_contents_to_response'),
    path('look/<int:pk>/', views.looks_to_response, name='looks_to_response'),
    path('item/<int:pk>/', views.items_to_response, name='items_to_response'),
]