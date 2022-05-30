from mongoengine import Document, fields


class User(Document):
    username = fields.StringField()
    password = fields.StringField()

    first_name = fields.StringField()
    last_name = fields.StringField()
