from django.db import models

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=100)
    task_list = models.ForeignKey('TaskList', on_delete= models.CASCADE)

    def __str__(self):
        return self.name