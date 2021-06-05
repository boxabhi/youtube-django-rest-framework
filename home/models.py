from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, TextField

# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    address = models.TextField(null=True , blank=True)
    father_name = models.CharField(max_length=100)
    


    
