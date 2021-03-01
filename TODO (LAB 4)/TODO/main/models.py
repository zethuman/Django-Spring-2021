from django.db import models
from django.utils import timezone


# Create your models here.
class Lists(models.Model):
    name = models.CharField('Lists', max_length=250)

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Tasks(models.Model):
    task = models.CharField('Tasks', max_length=250, blank=True)
    created = models.DateField('Created at', default=timezone.now)
    due = models.DateField('Due to', default=timezone.now)
    owner = models.CharField('Owner', max_length=300, default='admin')
    mark = models.BooleanField('Mark', default=False)
    lists = models.ForeignKey(Lists, on_delete=models.CASCADE, null=True, default=3, related_name="tasks")

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task

    def to_json(self):
        return {
            'id': self.id,
            'task': self.task,
            'created': self.created,
            'due': self.due,
            'owner': self.owner,
            'mark': self.mark
        }
