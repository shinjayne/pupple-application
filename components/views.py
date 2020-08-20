from django.http import JsonResponse
from django.shortcuts import render

from components.models import Component, LookItemInfoComponent, ItemCategoryInfoComponent, VoteComponent

def component_to_response(pk):
    component_class = Components.objects.get_subclass(pk=pk)
    component = Components.objects.get(pk=pk)

    if component_class == "VoteComponent":
        component_info = vote_component_to_response(component)
    else:
        component_info = basic_info_component_to_response(component)

    response = {
        "type": component_class,
        "fields": component_info,
    }

    return JsonResponse(reponse)

def basic_info_component_to_response(component):
    response = {
        "title": component.title,
        "explain": component.explain,
        "want_to_promote": component.want_to_promote,
    }

    return response

def vote_component_to_response(component):
    choices = component.vote_choice_set.all()
    basic_info = basic_info_component_to_response(component)
    add_info = {
        "img_url": component.img.url,
        "choices": [
            vote_component_to_response(choice) for choice in vote_component_to_response
        ]
    }

    response = basic_info.update(add_info)

    return response

def vote_component_choice_to_response(choice):
    response = {
        "name": choice.name,
        "img_url": choice.img.url,
        "vote": choice.vote,
    }

    return response
