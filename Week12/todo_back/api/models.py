from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    due_on= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_json_task(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
        }

    def to_json_all(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'task_list': self.task_list.to_json(),
        }