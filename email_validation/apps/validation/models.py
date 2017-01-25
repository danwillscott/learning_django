from __future__ import unicode_literals
from django.core.validators import validate_email
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Email(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def validation(username):
    try:
        validate_email(username)
        valid_email = True
    except ValidationError:
        valid_email = False
    return valid_email


def add_email(email):
    Email.objects.create(email=email)


def delete_email(email_id):
    Email.objects.get(id=email_id).delete()


def all_emails():
    return Email.objects.all()
