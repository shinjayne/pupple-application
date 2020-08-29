from django.contrib import admin
from components.models import LookItemInfoComponent, ItemCategoryInfoComponent, ModelInfoComponent, VoteComponent, VoteChoice

admin.site.register(LookItemInfoComponent)
admin.site.register(ItemCategoryInfoComponent)
admin.site.register(ModelInfoComponent)

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