from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import messages

import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASSWORD_REGEX = re.compile(r'((?=.+\d)(?=.+[a-z])(?=.+[A-Z]).{8,})', re.MULTILINE)
name_regex = re.compile(r'[a-zA-Z]+', re.MULTILINE)
# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    username = models.CharField(max_length=75, blank=True, null=True, unique=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    dob_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    user_level = models.IntegerField(max_length=1, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


def validation_handler(first_name, last_name, username, email, dob_date, description):
    """Because of the way messages are handled we will not be using this"""
    pass


def add_user(first_name, last_name, username, email, dob_date):
    """This will check if a user is valid and return an error message if user is in the DB already"""
    #  TODO set user_level by default. first user max all others low
    try:
        Users.objects.get(user_level=9)
        print("this worked")
        try:
            Users.objects.create(first_name, last_name, username, email, dob_date)
            return Users.objects.filter(username=username)
        except:  # TODO Figure out the error type and input that here
            return False
    except ObjectDoesNotExist:
        try:
            Users.objects.create(first_name, last_name, username, email, dob_date, user_level=9)
            return Users.objects.filter(username=username)
        except:  # TODO Figure out the error type and input that here
            return False


def name_validate(name):
    """This function validates a name with a simple regex for letter only and length greater then 2"""
    if len(name) > 2 and name_regex.match(name):
        return True
    return False  # TODO finish validation


def user_login(username, password):
    """This validates the username and password returning a true value AND user info in a dictionary for session use"""
    if password is True:  # TODO this needs to check if authenticated then return the dictionary from the user object
        user_object = Users.objects.get(username=username)
        user_dictionary ={
            'first_name': user_object.first_name,
            'last_name': user_object.last_name,
            'username': user_object.username,
            'email': user_object.email,
            'user_id': user_object.id
        }
        return user_dictionary
    else:
        return False
