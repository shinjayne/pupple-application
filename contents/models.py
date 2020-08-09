from django.db import models

ITEM_CATEGORY = [('Top', '상의'), ('Bottom', '하의'), ('etc', '기타')]

class ShoppableContents(models.Model):
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민

class Creator(models.Model):
    name = models.CharField(max_length=20)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민

class YoutubeContents(models.Model):
    shoppable_contents = models.ForeignKey(ShoppableContents)
    creator = models.ForeignKey(Creator)
    link = models.URLField()

class Item(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(choices=ITEM_CATEGORY, default='none' , max_length=10)
    explain = models.TextField(blank=True)
    price = models.PositiveInteger(default=0)
    link = models.URLField()

class Look(models.Model):
    youtube_contents = models.ForeignKey(YoutubeContents)
    title = models.CharField(max_length=100)
    items = models.ManyToMany(Item)
    votes = models.PositiveInteger(default=0)
