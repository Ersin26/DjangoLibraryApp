from mongoengine import Document, fields


class Book(Document):
    name = fields.StringField()


class BookBorrow(Document):
    book_id = fields.StringField()
    user_id = fields.StringField()

    borrow_date = fields.DateField()
    deliver_date = fields.DateField()

    is_delivered = fields.BooleanField()
