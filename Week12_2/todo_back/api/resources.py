from tastypie.resources import ModelResource
from api.models import Task, TaskList
from tastypie.authorization import Authorization

class TaskListsResource(ModelResource):
    class Meta:
        queryset = TaskList.objects.all()
        resource_name = 'task_lists'
        authorization = Authorization()

class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'tasks'
        authorization = Authorization()