from celery import shared_task
from datetime import datetime
from apps.library.models import BookBorrow


@shared_task
def create_borrow_object(book_id, user_id):
    print("Triggered")
    BookBorrow.objects.create(
        book_id=book_id,
        user_id=user_id,
        borrow_date=datetime.now(),
        deliver_date=None,
        is_delivered=False,
    )
    return 'Created successfully'

print(len(BookBorrow.objects.all()))