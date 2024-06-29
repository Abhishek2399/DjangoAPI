from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def api_home(request, *args, **kwargs):
    api_response = {
        'message' : 'this is the api response'
    }
    return JsonResponse(api_response)