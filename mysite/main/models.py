from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) 
    name = models.CharField (max_length=200)



    def __str__(self):
        return self.name
    
class Item (models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name="items") # default rel_name = "lowercaseClassName_set"
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    

# ForeignKey

# One object of Model A can be related to many objects of Model B,
# but each object of Model B is related to only one object of Model A.

# models.CASCADE -> delete the item if the parent list is deleted