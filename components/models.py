from django.db import models
from contents.models import YoutubeContents

def vote_img_upload_path(instance):
    return "component/vote/{}".format(instance.title)

def vote_choice_img_upload_path(instance):
    return "component/vote/{}".format(instance.vote_component.title)

class LookItemInfoComponent(models.Model):
    youtube_contents = models.ForeignKey(YoutubeContents, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ItemCategoryInfoComponent(models.Model):
    youtube_contents = models.ForeignKey(YoutubeContents, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VoteComponent(models.Model):
    youtube_contents = models.ForeignKey(YoutubeContents, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민
    img = models.ImageField(upload_to=vote_img_upload_path, blank=True)

class VoteChoice(models.Model):
    vote_component = models.ForeignKey(VoteComponent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to=vote_choice_img_upload_path, blank=True)
