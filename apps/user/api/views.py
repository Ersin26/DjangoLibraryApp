from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from apps.user.models import User
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["POST"])
def register_api(request):
    data = request.POST
    params = ["username", "password", "first_name", "last_name"]
    for p in params:
        if p not in data.keys():
            return JsonResponse({"status": False, "message": f"{p} is required", "data": None})

    User.objects.create(
        username=data.get("username"),
        password=data.get("password"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
    )

    return JsonResponse({"status": True, "message": "Successfully created", "data": None})
