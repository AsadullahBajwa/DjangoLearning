from django.urls import path
from . import views

urlpatterns = [
    path('blogs/create/',views.create_blog,name='create_blog'),
    path('blogs/delete/<int:pk>/',views.delete_blog,name='delete_blog'),
    path('blogs/update/<int:pk>/',views.update_blog,name='update_blog'),
    path('blogs/',views.show_blogs,name='show_blogs')
]