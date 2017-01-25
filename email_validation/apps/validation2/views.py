from django.shortcuts import render, redirect
from django.contrib import messages
from models import add_email, all_emails, delete_email, validation, Users
from django.contrib.auth import authenticate, models
from django.db import connection
# from django.db import models
from django.contrib.auth.hashers import check_password
# from email_validation import settings  # TODO this was to check on the password_hashers
from django.contrib.auth.models import User  # TODO THIS IS TO ADD A USER TO THE DB
from django.core.exceptions import ValidationError

# Create your views here.


def index(request):
    user = User.objects.get(username="danwillscott")
    print(user)
    return render(request, 'validation/templates/validation/index.html')


def add(request):
    if request.method == 'POST':
        email = request.POST['email']
        if validation(email):
            add_email(email)
            messages.success(request, 'You add your email successfully!')
            return redirect('/users')
        else:
            messages.warning(request, 'Please Enter A Valid Email.')
            return redirect('/')
    else:
        return redirect('/')


def users(request):
    context = {
        'users': all_emails()
    }
    return render(request, 'validation/templates/validation/users.html', context)


def delete(request, email_id):
    messages.success(request, 'You successfully removed your email address!')
    delete_email(email_id)
    return redirect('/users')

    # print(settings.PASSWORD_HASHERS)
    # try:
    # my_user = User.objects.create_user('bob', 'danwillscott@gmail.com', '123', first_name='Daniel', last_name='Scott')
    # except IntegrityError:
    #     pass
    # my_user = User.objects.create_user('testuser', 'testuser@email.com', 'IlUmt!9090%oe', first_name='Daniel', last_name='Scott')
    # test = models.User.objects.filter(first_name='Daniel')
    # print my_user
    # my_user.save()
    # print(my_user['last_name'])
    # full_user = []
    # try:
    #     # print(len(test))
    #     for idx in test:
    #         full_user.append(idx)
    # except IndexError:
    #     messages.error(request, "Can not complete request")
    # to_message = 'id: {} id: {} username: {} username: {}'.format(full_user[0].id, full_user[1].id,full_user[0].username, full_user[1].username)
    # messages.success(request, to_message)
    # print(authenticate(username='danwillscott', password='IlUmt!9090%oe'))  # Returns true if it works
    # my_user.objects.create(first_name="Daniel", last_name="scott")
    # print(my_user.username)
    # print (messages.error(request, 'this'))
