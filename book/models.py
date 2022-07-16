from django.db import models
from author.models import Author
from django.utils.translation import ugettext_lazy as _

class Book(models.Model):
    name = models.TextField( help_text=_('The title of the Book'),)
    isbn = models.TextField( help_text=_('The ISBN of the Book'),)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text=_('The author of the Book; this is a foreignkey to the author table'),)
    
    def __str__(self):
        return f"{self.name} - {self.author}"
