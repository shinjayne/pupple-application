from django.http import JsonResponse
from django.shortcuts import render

from components.models import Component, LookItemInfoComponent, ItemCategoryInfoComponent, VoteComponent, VoteChoice

from contents.views import looks_to_response


def component_to_response(pk):
    component_class = Component.objects.get_subclass(pk=pk)
    component = Component.objects.get(pk=pk)
    component_class_name = component_class.get_component_class()

    if component_class_name == "LookItemInfoComponent":
        component_info = look_item_info_component_to_response(component)
    elif component_class_name == "VoteComponent":
        component_info = vote_component_to_response(component)
    else:
        component_info = basic_info_component_to_response(component)

    response = {
        "type": component_class_name,
        "fields": component_info,
    }

    return response

def basic_info_component_to_response(component):
    response = {
        "title": component.title,
        "explain": component.explain,
        "want_to_promote": component.want_to_promote,
    }

    return response

def look_item_info_component_to_response(component):
    look_item_info_component = component.lookiteminfocomponent
    look = look_item_info_component.look
    response = basic_info_component_to_response(component)
    add_info = {
        "look": looks_to_response(look),
    }
    response.update(add_info)

    return response

def vote_component_to_response(component):
    vote_component = component.votecomponent
    choices = vote_component.vote_choice_set.all()
    response = basic_info_component_to_response(component)
    add_info = {
        "img_url": vote_component.img.url if vote_component.img else None,
        "img_aspect_ratio": vote_component.img_aspect_ratio,
        "allowed_choice_num": vote_component.allowed_choice_num,
        "choices": [
            vote_component_choice_to_response(choice) for choice in choices
        ]
    }
    response.update(add_info)

    return response

def vote_component_choice_to_response(choice):
    voted_users = choice.ipuserprofile_set.all()

    response = {
        "pk": choice.pk,
        "name": choice.name,
        "img_url": choice.img.url,
        "vote": choice.vote,
        "voted_users_pk_list": [
            voted_user.pk for voted_user in voted_users
        ],
    }

    return response


def get_component(request, pk):
    return JsonResponse(component_to_response(pk))

def vote_component_choice_increase(pk):
    choice = VoteChoice.objects.get(pk=pk)
    choice.vote += 1
    choice.save()

    return choice.vote

