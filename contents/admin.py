from django.contrib import admin
from contents.models import ShoppableContents, YoutubeContents, Creator, Item, Look

admin.site.register(ShoppableContents)
admin.site.register(Creator)
admin.site.register(Item)

class LookInline(admin.StackedInline):
    model = Look
    readonly_fields = ('like',)

@admin.register(YoutubeContents)
class YoutubeContentsAdmin(admin.ModelAdmin):
    inlines = [LookInline]