from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from .models import Task, TaskList


class JobResource(ModelResource):
    """
    API Facet
    """
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True