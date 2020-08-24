from django.db import models
from model_utils.managers import InheritanceManager
from contents.models import ShoppableContents

class Component(models.Model):
    shoppable_contents = models.ForeignKey(ShoppableContents, on_delete=models.CASCADE, related_name="component_set")
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)
    want_to_promote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InheritanceManager()

class LookItemInfoComponent(Component):

    def get_component_class(self):
        return "LookItemInfoComponent"

class ItemCategoryInfoComponent(Component):

    def get_component_class(self):
        return "ItemCategoryInfoComponent"

class VoteComponent(Component):
    img = models.ImageField(upload_to="component/vote/", blank=True)
    img_aspect_ratio = models.FloatField(default=1.0)
    allow_multi_choices = models.BooleanField(default=False)

    def get_component_class(self):
        return "VoteComponent"

class VoteChoice(models.Model):
    vote_component = models.ForeignKey(VoteComponent, on_delete=models.CASCADE, related_name="vote_choice_set")
    name = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to="component/vote/choice/", blank=True)
    vote = models.PositiveIntegerField(default=0)
