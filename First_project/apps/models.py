from django.db import models

# Create your models here.
class Student(models.Model):
        Name = models.CharField(max_length = 50)
        Reg_no = models.IntegerField(max_length = 20)
        Maths = models.IntegerField(max_length = 10)
        Physics = models.IntegerField(max_length = 10)
        Chemistry = models.IntegerField(max_length = 10)
        English = models.IntegerField(max_length = 10)


class Todo(models.Model):
        title = models.CharField(max_length = 50)
        description = models.TextField(blank=True,null=True)
        completed = models.BooleanField(default=False)

        def __str__(self):
                return self.title