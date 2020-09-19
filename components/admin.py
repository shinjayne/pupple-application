from django.contrib import admin
from components.models import LookItemInfoComponent, ItemCategoryInfoComponent, QuoteComponent, ModelInfoComponent, VoteComponent, VoteChoice, CommentComponent, Comment

admin.site.register(LookItemInfoComponent)
admin.site.register(ItemCategoryInfoComponent)
admin.site.register(QuoteComponent)
admin.site.register(ModelInfoComponent)
admin.site.register(CommentComponent)
admin.site.register(Comment)

# class LookItemInfoComponentInline(admin.StackedInline):
#     model = LookItemInfoComponent

# class ItemCategoryInfoComponentInline(admin.StackedInline):
#     model = ItemCategoryInfoComponent

class VoteChoiceInline(admin.StackedInline):
    model = VoteChoice

@admin.register(VoteComponent)
class VoteComponentAdmin(admin.ModelAdmin):
    inlines = [VoteChoiceInline]

# class VoteComponentInline(admin.StackedInline):
#     model = VoteComponent