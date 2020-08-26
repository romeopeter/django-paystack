import json

from django.shortcuts import render
from django.http import HttpResponse


def cart(request):
    json_response = {}
    json_response["message"] = "This is test response"
    json_response["error"] = "This is a test for error"

    return HttpResponse(json.dump(json_response))


def checkout():
    pass
