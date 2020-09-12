from django.db import models


class IPUserProfile(models.Model):
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address

class RandomNickName(models.Model):
    user = models.OneToOneField(IPUserProfile, on_delete=models.CASCADE, related_name="get_random")
    nickname = models.CharField(max_length=30)
