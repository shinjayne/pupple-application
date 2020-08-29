from django.db import models

from contents.models import Look
from components.models import VoteChoice


class IPUserProfile(models.Model):
    ip_address = models.GenericIPAddressField()
    liked_looks = models.ManyToManyField(Look, blank=True)
    voted_choices = models.ManyToManyField(VoteChoice, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address