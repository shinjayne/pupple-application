from django.http import JsonResponse

from accounts.models import IPUserProfile
from contents.models import ShoppableContents, Look, Item, ItemTag


def shoppable_contents_to_response(pk):
    shoppable_contents = ShoppableContents.objects.get(pk=pk)
    youtube_contents = shoppable_contents.youtube_contents_set.all()
    components = shoppable_contents.component_set.all().order_by('order')

    response = {
        "pk": shoppable_contents.id,
        "title": shoppable_contents.title,
        "explain": shoppable_contents.explain,
        "img_url": shoppable_contents.background_img.url if shoppable_contents.background_img else None,
        "youtube_contents_list": [
            youtube_contents_to_response(youtube_content) for youtube_content in youtube_contents
        ],
        "components_pk_list": [
            component.pk for component in components
        ],
    }

    return response

def youtube_contents_to_response(youtube_contents):
    creator = youtube_contents.creator

    response = {
        "title": youtube_contents.title,
        "creator": {
            "name": creator.name,
            "explain": creator.explain,
            "profile_img_url": creator.profile_img.url if creator.profile_img else None
        },
        "link": youtube_contents.link,
    }

    return response

def looks_to_response(look):
    items = look.items.all()
    liked_users = look.ipuserprofile_set.all()

    response = {
        "pk": look.pk,
        "title": look.title,
        "main_img_url": look.main_img.url if look.main_img else None,
        "main_img_aspect_ratio": look.main_img_aspect_ratio,
        "like": look.like,
        "items_pk_list": [
            items_to_response(item) for item in items
        ],
        "liked_users_pk_list": [
            liked_user.pk for liked_user in liked_users
        ],
    }

    return response

def items_to_response(item):
    tags = item.tags.all()

    response = {
        "pk" : item.id,
        "name": item.name,
        "category": item.category,
        "explain": item.explain,
        "main_img_url":  item.main_img.url if item.main_img else None,
        "price": item.price,
        "link": item.link,
        "tag_pk_list": [
            tag.pk for tag in tags
        ],
    }

    return response

def related_items_to_response(pk):
    tag = ItemTag.objects.get(pk=pk)
    related_items = tag.item_set.all()

    response = {
        "related_items": [
            items_to_response(item) for item in related_items
        ],
    }

    return response


def get_shoppable_contents(request, pk):
    return JsonResponse(shoppable_contents_to_response(pk))

def get_related_items(request, pk):
    return JsonResponse(related_items_to_response(pk))


def look_like_increase(request, pk):
    look = Look.objects.get(pk=pk)
    look.like += 1
    look.save()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    ip_user = IPUserProfile.objects.get(ip_address=ip_address)
    ip_user.liked_looks.add(look)
    ip_user.save()

    return JsonResponse({
        "value":  look.like
    })

def look_like_decrease(request, pk):
    look = Look.objects.get(pk=pk)
    look.like -= 1
    look.save()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    ip_user = IPUserProfile.objects.get(ip_address=ip_address)
    ip_user.liked_looks.remove(look)
    ip_user.save()

    return JsonResponse({
        "value":  look.like
    })

def item_hit_increase(request, pk):
    item = Item.objects.get(pk=pk)
    item.hit += 1
    item.save()

    return JsonResponse({
        "value": item.hit
    })

def get_all_shoppable_list(request):
    shoppable_ids = [shoppable_contents.id for shoppable_contents in list(ShoppableContents.objects.all())]
    return JsonResponse({
        "data" : [
            shoppable_contents_to_response(pk) for pk in shoppable_ids
        ]
    })