from django.db import models

class ToDo(models.Model):
    name =models.CharField(max_length=30)
    completed =models.BooleanField()
    
    def __str__(self):
        return self.title
