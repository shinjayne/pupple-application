from django.contrib import admin
from accounts.models import IPUserProfile, RandomNickName

admin.site.register(IPUserProfile)
admin.site.register(RandomNickName)