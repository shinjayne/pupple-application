from django.http import JsonResponse
from django.shortcuts import render

from components.models import Component, LookItemInfoComponent, ItemCategoryInfoComponent, VoteComponent, VoteChoice, CommentComponent, Comment
from accounts.models import IPUserProfile, RandomNickName

from contents.views import looks_to_response
from accounts.views import generate_random_nickname


def component_to_response(pk):
    component_class = Component.objects.get_subclass(pk=pk)
    component = Component.objects.get(pk=pk)
    component_class_name = component_class.get_component_class()

    if component_class_name == "LookItemInfoComponent":
        component_info = look_item_info_component_to_response(component)
    elif component_class_name == "VoteComponent":
        component_info = vote_component_to_response(component)
    elif component_class_name == "CommentComponent":
        component_info = comment_component_to_response(component)
    elif component_class_name == "ModelInfoComponent":
        component_info = model_info_component_to_response(component)
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

def model_info_component_to_response(component):
    model_info_component = component.modelinfocomponent
    response = basic_info_component_to_response(component)
    add_info = {
        "height": model_info_component.height,
        "top": model_info_component.top,
        "bottom": model_info_component.bottom,
        "shoes": model_info_component.shoes,
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
    voted_users = choice.voted_users.all()

    response = {
        "pk": choice.pk,
        "name": choice.name,
        "img_url": choice.img.url if choice.img else None,
        "vote": choice.vote,
        "voted_users_pk_list": [
            voted_user.pk for voted_user in voted_users
        ],
    }

    return response

def comment_component_to_response(component):
    comment_component = component.commentcomponent
    comments = comment_component.comment_set.all()
    response = basic_info_component_to_response(component)
    add_info = {
        "pk" : comment_component.pk,
        "img_url": comment_component.img.url if comment_component.img else None,
        "img_aspect_ratio": comment_component.img_aspect_ratio,
        "comments": [
            comment_to_response(comment) for comment in comments
        ]
    }
    response.update(add_info)

    return response

def comment_to_response(comment):
    liked_users = comment.liked_users.all()

    response = {
        "pk": comment.pk,
        "writer": comment.writer.get_random.nickname,
        "comment": comment.comment,
        "like": comment.like,
        "liked_users_pk_list": [
            liked_user.pk for liked_user in liked_users
        ],
        "created_at": comment.created_at
    }

    return response


def get_component(request, pk):
    return JsonResponse(component_to_response(pk))


def vote_component_choice_increase(request, pk):
    choice = VoteChoice.objects.get(pk=pk)
    choice.vote += 1

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    ip_user = IPUserProfile.objects.get(ip_address=ip_address)

    choice.voted_users.add(ip_user)
    choice.save()

    return JsonResponse({
        "value": choice.vote
    })

def comment_create(request, pk):
    comment_component = CommentComponent.objects.get(pk=pk)  ## 댓글 컴포넌트의 pk

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    ip_user = IPUserProfile.objects.get(ip_address=ip_address)

    if request.method == 'POST':
        comment_contents = request.POST.get('comment')

        try:
            ip_user.get_random
        except:
            RandomNickName.objects.create(
                user = ip_user,
                nickname = generate_random_nickname(),
            )

        comment = Comment.objects.create(
            comment_component=comment_component,
            writer=ip_user,
            comment=comment_contents,
        )

        return JsonResponse(comment_to_response(comment))

def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)  ## 댓글의 pk
    comment.delete()

    return JsonResponse({
        "status": "complete"
    })

def comment_like_increase(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.like += 1

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    ip_user = IPUserProfile.objects.get(ip_address=ip_address)

    comment.liked_users.add(ip_user)
    comment.save()

    return JsonResponse({
        "value":  comment.like
    })

def comment_like_decrease(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.like -= 1

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    ip_user = IPUserProfile.objects.get(ip_address=ip_address)

    comment.liked_users.remove(ip_user)
    comment.save()

    return JsonResponse({
        "value":  comment.like
    })

