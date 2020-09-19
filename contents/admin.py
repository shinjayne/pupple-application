from django.contrib import admin

from components.models import VoteComponent, LookItemInfoComponent, QuoteComponent, ModelInfoComponent
from contents.models import ShoppableContents, YoutubeContents, Creator, Item, ItemTag, Look

admin.site.register(Creator)
admin.site.register(ItemTag)


class VoteComponentInline(admin.TabularInline):
    model = VoteComponent
    ordering = ('order', )


class LookInfoComponentInline(admin.TabularInline):
    model = LookItemInfoComponent
    ordering = ('order',)


class QuoteComponentInline(admin.TabularInline):
    model = QuoteComponent
    ordering = ('order',)


class ModelInfoComponentInline(admin.TabularInline):
    model = ModelInfoComponent
    ordering = ('order', )


@admin.register(ShoppableContents)
class ShoppableContentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'explain' , 'background_img']
    inlines = [VoteComponentInline, LookInfoComponentInline, QuoteComponentInline, ModelInfoComponentInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ['category',]

    list_display = ['id', 'name', 'category', 'main_img', 'price', 'link']
    list_display_links = ['id']
    list_editable = ['name', 'category', 'main_img', 'price', 'link']

class LookInline(admin.TabularInline):
    model = Look
    readonly_fields = ('like',)

@admin.register(YoutubeContents)
class YoutubeContentsAdmin(admin.ModelAdmin):
    inlines = [LookInline]
    list_display = ['shoppable_contents', 'title', 'creator', 'link' ]
    list_display_links = ['title']