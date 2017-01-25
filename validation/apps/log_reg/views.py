from django.shortcuts import render, redirect
from ..log_reg.models import LogInLogOut, Users
from django.contrib import messages
import re
from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
# Create your views here.

#  TODO reverse('admin:app_list', kwargs={'app_label': 'auth'}) must declare kwargs to pass dictionary


def index(request):
    if 'username' in request.session:  # TODO this needs to redirect to the logged IN page if user in session
        return redirect('/login/logged_in')  # TODO make this route to the other app
    return render(request, 'log_reg/templates/log_reg/index.html')


# try:
#     Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
# except IntegrityError:
#     messages.warning(request, "User name already in use! Please select a new one")
#     return redirect('/login')
# registration_dictionary ={
#     'first_name': request.POST['first_name'],
#     'last_name': request.POST['last_name'],
#     'username': request.POST['username'],
#     'email': request.POST['email'],
#     'password': request.POST['password'],
#     'password_confirm': request.POST['password_confirm'],
#     'dob_date': request.POST['dob_date'],
# }


def register(request):  # TODO add reg class call and pass back dictionary and save in session
    if request.method == 'POST':
        pass
    if not validate_email('danwillscott@hotmail.com'):
        print ('email valid')
    else:
        print ('not valid')
    return redirect('/login')  # TODO make this route go to the other app


def user_login(request):
    request.session.flush()
    if request.method == 'POST':
        if request.POST['username'] > 0 and request.POST['password']:
            user_is = LogInLogOut.login_validate(request.POST['username'], request.POST['password'])
            if user_is['truth']:
                messages.success(request, user_is['alert'])
                request.session['first_name'] = user_is['first_name']
                request.session['last_name'] = user_is['last_name']
                request.session['username'] = user_is['username']
                request.session['email'] = user_is['email']
                request.session['user_id'] = user_is['user_id']
                return redirect('/login/edit/{}'.format(request.session['username']))
            else:
                messages.error(request, user_is['alert'])
    return redirect('/login')  # TODO make this route go to the other app


def is_logged_in(request):
    if 'username' in request.session:
        return redirect('/login/edit/{}'.format(request.session['username']))
    else:
        redirect('/login')


def user_logout(request):
    request.session.flush()  # This flushes the session effectively removing the user
    return redirect('/login')  # This takes you back to login page on logout


def edit(request, username):  # This allows for editing of the user
    if 'username' in request.session:
        if request.session['username'] == username:
            print(username)
            return render(request, 'log_reg/templates/log_reg/edit.html')
    else:
        request.session.flush()
        messages.warning(request, "User did not match the edit page. Please log in again.")
        return redirect('/login')
