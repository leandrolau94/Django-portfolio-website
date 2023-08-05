from django.db import models

# Create your models here.
class Professor(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Group(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50)
    academic_level = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name

class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    first_tcp_mark = models.IntegerField(blank=True)
    second_tcp_mark = models.IntegerField(blank=True)
    final_test_mark = models.IntegerField(blank=True)
    extra_test_mark = models.IntegerField(blank=True)
    mundial_test_mark = models.IntegerField(blank=True)

    def __str__(self):
        return self.subject_name