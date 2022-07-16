from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.TextField(help_text=_('The first name of the author'),)
    last_name = models.TextField(help_text=_('The last name of the author'),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
