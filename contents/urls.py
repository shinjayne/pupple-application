from django.urls import path
from contents import views

urlpatterns = [
    path('shoppable/', views.get_all_shoppable_list, name="get_all_shoppable_list"),
    path('shoppable/<int:pk>/', views.get_shoppable_contents, name='get_shoppable_contents'),
    path('item/related/<int:pk>/', views.get_related_items, name='get_related_items'),
    path('look/like/<int:pk>/', views.look_like_increase, name='look_like_increase'),
    path('item/hit/<int:pk>/', views.item_hit_increase, name='item_hit_increase'),
]