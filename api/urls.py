from django.urls import path
from . import views

urlpatterns=[
    path('',views.api_overview,name='overview'),
    path('task-list/',views.task_list,name='task-list'),
    path('task-details/<str:pk>',views.detail_view,name='task-details'),
    path('task-create/',views.task_create,name='task-create'),
    path('task-update/<str:pk>',views.task_update,name='task-update'),
    path('task-delete/<str:pk>',views.task_delete,name='task-delete'),
]

#main urls
# path('api/',include("api.urls"))