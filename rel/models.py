from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.BinaryField(null=True)
    icon_info = models.CharField(max_length=64,null=True)

    def __str__(self):
        return f"Profile of {self.user.get_full_name()}"

class ShoppingList(models.Model):
    item = models.CharField(max_length=32)
    qnty = models.IntegerField()

    class Meta:
        db_table = "shop_list"
        #order_with_respect_to = 'qnty'

    def __str__(self):
        return "Shopping list"

class Student(models.Model):
    name = models.CharField(max_length=32)
    id0 = models.IntegerField()
    ### course_set = models.ManyToManyField(Course)
    #courses = models.TextField(max_length=1024)
    #courses = models.ManyToManyField(Course)

    class Meta:
        db_table = 'students'
        ordering = ['name']

    def __str__(self):
        return f"student {self.name}"

class Professor(models.Model):
    prefix = [
        ("Dr","Doctor"),
        ("Prof", "Doctor"),
    ]
    full_name = models.CharField(max_length=64)
    degree = models.CharField(max_length=4, choices=prefix, default="Dr")

    class Meta:
        db_table = 'profs'

    def __str__(self):
        return f"Teacher {self.degree} {self.full_name}"

class Course(models.Model):
    title = models.CharField(max_length=32)
    id0 = models.IntegerField()
    #students = models.TextField(max_length=1024)
    students = models.ManyToManyField(Student)
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"course {self.title}"

class Diploma(models.Model):
    title = models.CharField(max_length=32)
    student = models.OneToOneField(Student,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    class Meta:
        db_table = 'diploma'

    def __str__(self):
        return f"Diploma {self.title}"