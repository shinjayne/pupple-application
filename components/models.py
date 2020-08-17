from django.db import models
from model_utils.managers import InheritanceManager
from contents.models import ShoppableContents

def vote_img_upload_path(instance):
    return "component/vote/{}".format(instance.title)

def vote_choice_img_upload_path(instance):
    return "component/vote/{}".format(instance.vote_component.title)

class Component(models.Model):
    shoppable_contents = models.ForeignKey(ShoppableContents, on_delete=models.CASCADE, related_name="component_set")
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)
    want_to_promote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InheritanceManager()

class LookItemInfoComponent(Component):
    pass

class ItemCategoryInfoComponent(Component):
    pass

class VoteComponent(Component):
    img = models.ImageField(upload_to=vote_img_upload_path, blank=True)

class VoteChoice(models.Model):
    vote_component = models.ForeignKey(VoteComponent, on_delete=models.CASCADE, related_name="vote_choice_set")
    name = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to=vote_choice_img_upload_path, blank=True)
    vote = models.PositiveIntegerField(default=0)
