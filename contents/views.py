from django.http import JsonResponse
from django.shortcuts import render

from contents.models import ShoppableContents, YoutubeContents, Look, Item

def shoppable_contents_detail(request, pk):
    return render(request, 'contents/test.html', {
        'pk': pk,
    })

def shoppable_contents_to_response(request, pk):
    shoppable_contents = ShoppableContents.objects.get(pk=pk)
    youtube_contents = shoppable_contents.youtube_contents_set.all()
    components = shoppable_contents.component_set.all()

    response = {
        "title": shoppable_contents.title,
        "explain": shoppable_contents.explain,
        "img_url": shoppable_contents.background_img.url,
        "youtube_contents_list": [
            youtube_contents_to_response(youtube_content) for youtube_content in youtube_contents
        ],
        "components_pk_list": [
            component.pk for component in components
        ],
    }

    return JsonResponse(response)

def youtube_contents_to_response(youtube_contents):
    creator = youtube_contents.creator
    looks = youtube_contents.look_set.all()

    response = {
        "title": youtube_contents.title,
        "creator": {
            "name": creator.name,
            "explain": creator.explain,
            "profile_img_url": creator.profile_img.url
        },
        "link": youtube_contents.link,
        "look_list": [
            looks_to_response(look) for look in looks
        ],
    }

    return response

def looks_to_response(look):
    items = look.items.all()

    response = {
        "pk": look.pk,
        "title": look.title,
        "main_img_url": look.main_img.url,
        "like": look.like,
        "items_pk_list": [
            item.pk for item in items
        ],
    }

    return response

def items_to_response(request, pk):
    item = Item.objects.get(pk=pk)

    response = {
        "name": item.name,
        "category": item.category,
        "explain": item.explain,
        "main_img_url": item.main_img.url,
        "price": item.price,
        "link": item.link,
    }

    return JsonResponse(response)

def look_like_increas(pk):
    look = Look.objects.get(pk=pk)
    look.like += 1
    look.save()

    return look.like

