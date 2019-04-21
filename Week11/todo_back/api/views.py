from django.shortcuts import render
from .models import TaskList, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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