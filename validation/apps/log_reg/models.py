from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
import bcrypt
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASSWORD_REGEX = re.compile(r'((?=.+\d)(?=.+[a-z])(?=.+[A-Z]).{8,})', re.MULTILINE)
name_regex = re.compile(r'[a-zA-Z]+', re.MULTILINE)

# NAME_REGEX     = re.compile(r'^[a-zA-Z -\']{3,}$')  # Other Regex to test
# PASSWORD_REGEX = re.compile(r'^([A-Z])+([a-z])+([0-9])+$')
# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    username = models.CharField(max_length=75, blank=True, null=True, unique=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    dob_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    user_level = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Registration(models.Model):  # TODO

    @staticmethod
    def register(fn, ln, un, email, dob, des, pw):
        hash_pw = bcrypt.hashpw(pw, bcrypt.gensalt(14))
        Users.objects.create(first_name=fn, last_name=ln, username=un, email=email, dob_date=dob, description=des, password=hash_pw)

    @staticmethod
    def add_user(first_name, last_name, username, email, dob_date):
        return_dictionary = {
            'truth': False,
            'alert': ''
        }
        """This will check if a user is valid and return an error message if user is in the DB already"""
        #  TODO set user_level by default. first user max all others low
        try:
            Users.objects.get(user_level=9)
            try:
                Users.objects.create(first_name, last_name, username, email, dob_date)
                return Users.objects.filter(username=username)
            except IntegrityError:
                return False
        except ObjectDoesNotExist:
            try:
                Users.objects.create(first_name, last_name, username, email, dob_date, user_level=9)
                return Users.objects.filter(username=username)
            except IntegrityError:
                return False

    @staticmethod
    def name_validate(name):
        """This function validates a name with a simple regex for letter only and length greater then 2"""
        if len(name) > 2 and name_regex.match(name):
            return True
        return False


class LogInLogOut(models.Model):

    @staticmethod
    def login_validate(username, password):
        print('***** models.py login_validate start *****')  # TOD
        try:
            print('***** login_validate TRY is run *****')  # TODO
            password_hash = Users.objects.get(username=username)
            password_hash = password_hash.password
        except ObjectDoesNotExist:
            print('***** login_validate EXCEPT is run *****')
            to_return = {
                'truth': False,
                'alert': "User name and password are incorrect"
            }
            return to_return
            # checked_password = check_password(password, password_hash)  #TODO use hashed password
            # print(checked_password)
            # if checked_password:
        if password == password_hash:
            user_object = Users.objects.get(username=username)
            user_dictionary = {
                'truth': True,
                'alert': "Login Complete!",
                'first_name': user_object.first_name,
                'last_name': user_object.last_name,
                'username': user_object.username,
                'email': user_object.email,
                'user_id': user_object.id
            }
            return user_dictionary
        else:
            return False


class GET(models.Manager):

    @staticmethod
    def ui(user_id):
        return Users.objects.get(id=user_id)


class Set(models.Manager):

    @staticmethod
    def new_user(fn, ln, un, email, dob, des, pw):
        """This makes a new user"""
        hash_pw = bcrypt.hashpw(pw, bcrypt.gensalt(14))
        Users.objects.create(first_name=fn, last_name=ln, username=un, email=email, dob_date=dob, description=des, password=hash_pw)

    @staticmethod
    def update(where, user, new_val):
        """The where is the column name to be updated
            The user is the user name to update
            The new_val is the value to be passed in"""
        user_instances = Users.objects.filter(username=user)
        if where == 'first_name':
            user_instances.update(first_name=new_val)  # Updates first name
        if where == 'last_name':
            user_instances.update(last_name=new_val)
        if where == 'username':
            user_instances.update(username=new_val)
        if where == 'email':
            user_instances.update(email=new_val)
        if where == 'description':
            user_instances.update(description=new_val)
        if where == 'password':
            hash_pw = bcrypt.hashpw(new_val, bcrypt.gensalt(14))
            user_instances.update(password=hash_pw)


class NewUser(models.Model):

    message_dict = {
        'truth': True,
        'first': '',
        'last': '',
        'user': '',
        'email': '',
        'password': '',
        'dob': '',
        'add_fail': ''
    }

    user_dict = {
        'first_name': '',
        'last_name': '',
        'username': '',
        'email': '',
        'password': '',
        'dob_date': ''
    }

    add_dict = {
        'truth': False,
        'alert': ''
    }

    def new_user(self, fn, ln, un, em, pw, cpw, dob):  # TODO untested
        if len(fn) < 3 or not name_regex.match(fn):
            print('*****in len first name under 3 and regex fail*****')  # TODO
            self.message_dict['truth'] = False
            self.message_dict['first'] = 'Name must be 2 or more letters and letters only'
        if len(ln) < 3 or not name_regex.match(ln):
            print('*****in len last name under 3 and regex fail*****')  # TODO
            self.message_dict['truth'] = False
            self.message_dict['last'] = 'Name must be 2 or more letters and letters only'
        if Users.objects.filter(username=un).exists(): # works!
            self.message_dict['truth'] = False
            self.message_dict['user'] = 'User name is already used please select a new one'
        if not re.match(EMAIL_REGEX, em):
            self.message_dict['truth'] = False
            self.message_dict['email'] = 'Please enter a valid email'
        if pw != cpw:
            self.message_dict['truth'] = False
            self.message_dict['password'] = 'Passwords do not match'
        elif pw < 9:
            self.message_dict['truth'] = False
            self.message_dict['password'] = 'Your password must be 8 characters or longer'
        elif not re.match(PASSWORD_REGEX, pw):
            self.message_dict['truth'] = False
            self.message_dict['password'] = 'Password must have 1 Number 1 Capital, 1 lowercase letter'
        if dob:  # Test PASSED
            if int(dob[0:4]) > 2004:
                self.message_dict['truth'] = False
                self.message_dict['dob'] = 'You must have been born before 2004 to register'
        if self.message_dict['truth']:
            self.user_dict = {
                'first_name': fn,
                'last_name': ln,
                'username': un,
                'email': em,
                'password': bcrypt.hashpw(pw, bcrypt.gensalt()),
                'dob_date': dob,
                'user_level': 9 if not Users.objects.filter(user_level=9).exists() else 1,  # test PASSED

            }

    def add_user(self):  # TODO untested
        if self.message_dict['truth']:
            try:
                Users.objects.create(self.user_dict)
                self.add_dict['truth'] = True
                self.add_dict['alert'] = 'Registration Complete!'
            except IntegrityError:
                self.add_dict['truth'] = False
                self.add_dict['alert'] = 'Registration Failed Please try again'
        else:
            self.add_dict['truth'] = False
            self.add_dict['alert'] = "You are outside the normal realm of errors. Lets just start over"
        return self

    def add_dec(self, dec, username):
        if dec < 1:  # TODO
            self.add_dict['truth'] = False
            self.add_dict['alert'] = "You have to actually type something if you want us to save it!"
        if Users.objects.filter(username=username).exists():  # works!
            self.add_dict['truth'] = True
            self.add_dict['alert'] = 'You have added a description of yourself! Thanks!'
        else:
            self.add_dict['truth'] = False
            self.add_dict['alert'] = 'Something went wrong on our end. Please try again'
