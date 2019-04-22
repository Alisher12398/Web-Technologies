from rest_framework import serializers
from .models import Task, TaskList
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'created_at', 'due_on', 'status', 'task_list']

class TaskListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['name']

class TaskListDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'status']