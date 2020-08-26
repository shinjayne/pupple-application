from django.http import JsonResponse
from django.shortcuts import render

from accounts.models import IPUserProfile


def get_ip_user(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    try:
        user = IPUserProfile.objects.get(ip_address=ip_address)
    except:
        user = IPUserProfile.objects.create(ip_address=ip_address)

    return JsonResponse({"pk": user.pk})