from django.db import models


class ToDoItem(models.Model):
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'ToDo Item'
        verbose_name_plural = 'ToDo Items'

    def __str__(self):
        return self.title
