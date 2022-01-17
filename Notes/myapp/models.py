from django.contrib.auth.models import User
from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    user = models.ForeignKey(to=User, related_name='Notes', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notes"
