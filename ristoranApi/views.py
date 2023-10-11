# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import models

# Create your views here.

def index(_):
    return JsonResponse({"message":"Hello, world. You're at the index."},)

@require_POST
def create_user(request):
    if request.method != 'POST':
        return JsonResponse({"message":"Method no ALLOWED"},)
    data = request.body
    data_json = json.loads(data)
    email = data_json.pop("email")
    password = data_json.pop("password")

    try:
        user_created = models.UserAPI.objects.create_user(email,password,**data_json)
        user_created.save()
    except Exception as e:
        return JsonResponse({"message":str(e)},)
    return JsonResponse({"message":"User created"},)
