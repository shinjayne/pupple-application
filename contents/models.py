from django.db import models

ITEM_CATEGORY = [('Top', '상의'), ('Bottom', '하의'), ('etc', '기타')]

# def item_img_upload_path(instance):
#     return "contents/item/{}".format(instance.item.name)

# def look_img_upload_path(instance):
#     return "contents/look/{}".format(instance.look.title)

class ShoppableContents(models.Model):
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민
    background_img = models.ImageField(upload_to="contents/shoppable/background", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Creator(models.Model):
    name = models.CharField(max_length=20)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민
    profile_img = models.ImageField(upload_to="contents/creator/profile", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class YoutubeContents(models.Model):
    shoppable_contents = models.ForeignKey(ShoppableContents, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    link = models.URLField()

class Item(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(choices=ITEM_CATEGORY, default='none' , max_length=10)
    main_img = models.ImageField(upload_to="contents/item/{}".format(name), blank=True)
    # imgs = models.ForeignKey('ItemImage', on_delete=models.SET_NULL, null=True)
    explain = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class ItemImage(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to=item_img_upload_path)

class Look(models.Model):
    youtube_contents = models.ForeignKey(YoutubeContents, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    main_img = models.ImageField(upload_to="contents/look/{}".format(title), blank=True)
    # imgs = models.ForeignKey('LookImage', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(Item)
    like = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class LookImage(models.Model):
#     look = models.ForeignKey(Look, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to=look_img_upload_path)

