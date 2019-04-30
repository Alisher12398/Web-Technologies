from django.db import models
from django.contrib.auth.models import User


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class TaskList(models.Model):
    name = models.CharField('Name', max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = TaskListManager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Task(models.Model):
    name = models.CharField('Name', max_length=200)
    created_at = models.DateTimeField('Created', auto_now_add=True, null=False)
    due_on = models.DateTimeField('Due on', null=False)
    status = models.CharField('Status', max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = TaskManager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json_list(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }