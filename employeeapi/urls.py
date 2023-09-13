from django.urls import path
from . import views

urlpatterns =[
    path('emp-list/',views.employeeList,name='employeeList'),
    path('empDetail/<str:pk>/',views.empDetails,name='empDetails'),
    path('empCreate/',views.empCreate,name='empCreate'),
    path('empUpdate/<str:pk>/',views.empUpdate,name='empUpdate'),
    path('empDelete/<str:pk>/',views.empDelete,name='empDelete'),
]