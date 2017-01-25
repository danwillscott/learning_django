from django.shortcuts import render, redirect
from django.contrib import messages
from models import add_email, all_emails, delete_email, validation
# Create your views here.


def index(request):

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
