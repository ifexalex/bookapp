from django.db import models

class Book(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
