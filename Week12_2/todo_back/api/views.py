from django.shortcuts import render
from .models import TaskList, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
import json
from .serializers import TaskModelSerializer, TaskListModelSerializer, TaskListDetailModelSerializer

class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

    def get_object(self):
        return Task.objects.get(id=self.kwargs['pk'])

class TaskListView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListModelSerializer

class TaskListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListModelSerializer

    def get_object(self):
        return TaskList.objects.get(id=self.kwargs['pk'])

class TaskListDetailTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListDetailModelSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list=TaskList.objects.get(id=self.kwargs["fk"]))

    def perform_create(self, serializer):
        serializer.save(task_list=TaskList.objects.get(id=self.kwargs["fk"]))


@csrf_exempt
def taskList_list(request):
    if request.method == 'GET':
        taskLists = TaskList.objects.all()
        json_taskLists = [t.to_json() for t in taskLists]
        return JsonResponse(json_taskLists, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        if 'name' in body:
            taskList = TaskList(name = body['name'])
            taskList.save()
            return JsonResponse(taskList.to_json())
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def taskList_detail(request, pk):
    try:
        taskList = TaskList.objects.get(id = pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(taskList.to_json())
    elif request.method == 'PUT':
        body = json.loads(request.body)
    # if 'name' in body:
        taskList.name = body.get('name', taskList.name)
        taskList.save()
        return JsonResponse(taskList.to_json())
    return JsonResponse({'error': 'bad request'})


def task_list(request, pk):
    if request.method == 'GET':
        try:
            task_list = TaskList.objects.get(id = pk)
        except TaskList.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        tasks = task_list.task_set.all()
        json_tasks = [tk.to_json_task() for tk in tasks]
        return JsonResponse(json_tasks, safe = False)

def task_detail(request, pk):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id = pk)
        except Task.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_task = task.to_json_all()
        return JsonResponse(json_task)

def task_detail_update(request, pk):
    if request.method == 'POST':
        try:
            task = Task.objects.update(id = pk)
        except Task.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_task = task.to_json_all()
        return JsonResponse(json_task)