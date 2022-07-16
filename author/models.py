from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.first_name
