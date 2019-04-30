"""todo_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.resources import TaskResource, TaskListsResource
from api.views import task_list
# note_resource = NoteResource()
# task_resource =  TaskResource()'
# taskList_resource =  TaskListsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(taskList_resource.urls)),
    # path('api/', include(task_resource.urls)),
    # path('api/', include(note_resource.urls)),
    # path('api/task_lists/<int:pk>/tasks/', task_list)
    path('api/', include('api.urls'))
]
