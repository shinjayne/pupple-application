from django.urls import path
from contents import views

urlpatterns = [
    path('shoppable/<int:pk>/', views.shoppable_contents_to_response, name='shoppable_contents_to_response'),
    path('item/<int:pk>/', views.items_to_response, name='items_to_response'),
    path('item/related/<int:pk>/', views.related_items_to_response, name='related_items_to_response'),
    path('look/like/<int:pk>/', views.look_like_increase, name='look_like_increase'),
]