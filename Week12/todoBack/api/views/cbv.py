from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer


class TaskListList(APIView):
    def get(self, request):
        lists = TaskList.objects.for_user(self.request.user)
        serializer = TaskListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListDetail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.for_user(self.request.user).get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data)

    def put(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_list = self.get_object(pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TasksList(APIView):
    def get_task_list(self, pk):
        try:
            return TaskList.objects.for_user(self.request.user).get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_task_list(pk)
        tasks = task_list.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        task_list = self.get_task_list(pk)
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user, task_list=task_list)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.for_user(self.request.user).get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskListSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
