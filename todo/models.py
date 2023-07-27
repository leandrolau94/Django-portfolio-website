from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date created")

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=200)
    created_at = models.DateTimeField("date started")