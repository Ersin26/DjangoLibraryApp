from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from apps.user.models import User
from apps.library.models import Book, BookBorrow
from django.views.decorators.csrf import csrf_exempt
from apps.library.tasks import create_borrow_object


@csrf_exempt
@require_http_methods(["POST"])
def create_borrow(request):
    data = request.POST

    # Control params
    params = ["book_id", "user_id"]
    for p in params:
        if p not in data.keys():
            return JsonResponse({"status": False, "message": f"{p} is required", "data": None})

    # Control book is exists
    book = Book.objects.filter(id=data.get("book_id"))
    if not book:
        return JsonResponse({"status": False, "message": "Book does not exists", "data": None})

    # Control user is exists
    user = User.objects.filter(id=data.get("user_id"))
    if not user:
        return JsonResponse({"status": False, "message": "User does not exists", "data": None})

    # Control book is already borrowed
    if BookBorrow.objects.filter(book_id=data.get("book_id"), is_delivered=False):
        return JsonResponse({"status": False, "message": "Book is already borrowed", "data": None})

    # Create borrow object
    create_borrow_object.delay(data.get("book_id"), data.get("user_id"))
    return JsonResponse({"status": True, "message": "Successfully created"})


@csrf_exempt
@require_http_methods(["POST"])
def create_book(request):
    book_name = request.POST.get("name", None)
    if not book_name:
        return JsonResponse({"status": False, "message": "Book name is required"})

    book = Book.objects.create(
        name=book_name
    )
    return JsonResponse({"status": True, "message": "Successfully created", "data": {"id": str(book.pk)}})
