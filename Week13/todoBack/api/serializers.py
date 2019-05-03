from rest_framework import serializers
from api.models import TaskList, Task
from auth_.serializers import UserSerializer


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list = TaskListSerializer(read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

