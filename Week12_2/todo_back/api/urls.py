
from django.contrib import admin
from django.urls import path, include
from .views import taskList_list, taskList_detail, task_list, task_detail
urlpatterns = [
    path('task_lists/', taskList_list),
    path('task_lists/<int:pk>', taskList_detail),
    path('task_lists/<int:pk>/tasks/', task_list),
    path('tasks/<int:pk>/', task_detail)
]