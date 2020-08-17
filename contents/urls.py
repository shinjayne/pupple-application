from django.urls import path
from contents import views

urlpatterns = [
    path('<int:pk>/', views.shoppable_contents_to_response, name='shoppable_contents_to_response'),
    path('youtube/<int:pk>/', views.youtube_contents_to_response, name='youtube_contents_to_response'),
    path('look/<int:pk>/', views.look_to_response, name='look_to_response'),
    path('item/<int:pk>/', views.item_to_response, name='item_to_response'),
]