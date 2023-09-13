from django.urls import path
from . import views

urlpatterns = [
    path('items/',views.read_items,name='read_items'),
    path('items/create/',views.create_item,name='create_item'),
    path('items/update/<int:item_id>/',views.update_item,name='update_item'),
    path('items/retrieve/<int:item_id>/',views.retreive_item,name='retreive_item'),
    path('items/delete/<int:item_id>/',views.delete_item,name='delete_item'),
]