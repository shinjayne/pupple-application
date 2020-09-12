from django.db import models
from model_utils.managers import InheritanceManager
from contents.models import ShoppableContents, Look

class Component(models.Model):
    shoppable_contents = models.ForeignKey(ShoppableContents, on_delete=models.CASCADE, related_name="component_set")
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    want_to_promote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InheritanceManager()

class LookItemInfoComponent(Component):
    look = models.ForeignKey(Look, on_delete=models.CASCADE, related_name="component_set")

    def __str__(self):
        return "[" + self.shoppable_contents.title[:20] + "...]" + " (룩 아이템) " + self.title

    class Meta:
        verbose_name = '장면 컴포넌트'
        verbose_name_plural = '장면 컴포넌트'

    def get_component_class(self):
        return "LookItemInfoComponent"

class ItemCategoryInfoComponent(Component):

    def __str__(self):
        return "[" + self.shoppable_contents.title[:20] + "...]" + " (아이템 카테고리) " + self.title

    class Meta:
        verbose_name = '카테고리 컴포넌트'
        verbose_name_plural = '카테고리 컴포넌트'

    def get_component_class(self):
        return "ItemCategoryInfoComponent"

class ModelInfoComponent(Component):
    height = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    shoes = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '모델정보 컴포넌트'
        verbose_name_plural = '모델정보 컴포넌트'

    def __str__(self):
        return "[" + self.shoppable_contents.title[:20] + "...]" + " (모델) " + self.title



    def get_component_class(self):
        return "ModelInfoComponent"

class VoteComponent(Component):
    img = models.ImageField(upload_to="component/vote/", blank=True)
    img_aspect_ratio = models.FloatField(default=1.0, verbose_name='가로/세로비', help_text="가로길이 나누기 세로길이. 정방형이면 1.")
    allowed_choice_num = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = '투표 컴포넌트'
        verbose_name_plural = '투표 컴포넌트'

    def __str__(self):
        return "[" + self.shoppable_contents.title[:20] + "...]" + " (투표) " + self.title

    def get_component_class(self):
        return "VoteComponent"

class VoteChoice(models.Model):
    vote_component = models.ForeignKey(VoteComponent, on_delete=models.CASCADE, related_name="vote_choice_set")
    name = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to="component/vote/choice/", blank=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.vote_component.title[:20] + "... : " + self.name

class CommentComponent(Component):
    img = models.ImageField(upload_to="component/comment/", blank=True)
    img_aspect_ratio = models.FloatField(default=1.0, verbose_name='가로/세로비', help_text="가로길이 나누기 세로길이. 정방형이면 1.")

    class Meta:
        verbose_name = '댓글 컴포넌트'
        verbose_name_plural = '댓글 컴포넌트'

    def __str__(self):
        return "[" + self.shoppable_contents.title[:20] + "...]" + " (댓글) " + self.title

    def get_component_class(self):
        return "CommentComponent"

class Comment(models.Model):
    comment_component = models.ForeignKey(CommentComponent, on_delete=models.CASCADE, related_name="comment_set")
    random_writer_name = models.CharField(max_length=30)
    comment = models.TextField(max_length=500)
    like = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_component.title[:20] + "... : " + self.comment
