from django.shortcuts import render, redirect
from ..log_reg.models import name_validate, user_login
# Create your views here.


def index(request):
    if 'user' in request.session:  # TODO this needs to redirect to the logged IN page if user in session
        return render(request, 'log_reg/templates/log_reg/index.html')  # TODO make this route to the other app
    return render(request, 'log_reg/templates/log_reg/index.html')


def register(request):
    if request.method == 'POST':
        if name_validate(request.POST['first_name']) and name_validate(request.POST['last_name']):
            pass  # This validates user name with only letters and greater then 2
        pass  # TODO pass dated to models.py for validation and then login.
    # TODO Return user ID and save in session
    return redirect('/login')  # TODO make this route go to the other app


def user_login(request):
    if request.method == 'POST':
        user_is = user_login(request.POST['username'], request.POST['password'])
        if user_is:
            request.session

    # TODO pass data to models.py for validation and login
    # TODO Return user ID and save in session
    return redirect('/login')  # TODO make this route go to the other app


def user_logout(request):
    # TODO .flush session on user_logout
    return redirect('/login')  # This takes you back to login page on logout


def edit(request, user_name):  # This allows for editing of the user
    # TODO Pass edited information based on selected HTML value to the right models.py function
    # TODO ensure any updated values are stored in session after request for edit
    print(user_name)
    return render(request, 'log_reg/templates/log_reg/edit.html')
