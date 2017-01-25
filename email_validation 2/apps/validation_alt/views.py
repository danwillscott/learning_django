from django.shortcuts import render, redirect
from django.contrib import messages
from ..validation.models import validation, all_emails, delete_email, add_email
# Create your views here.


def index_alt(request):
    print('alt index')
    return render(request, 'validation_alt/templates/validation_alt/index_alt.html')


def add_alt(request):
    print("alt add")
    if request.method == 'POST':
        email = request.POST['email']
        if validation(email):
            add_email(email)
            messages.success(request, 'You add your email successfully!')
            return redirect('/alt/users_alt')
        else:
            messages.warning(request, 'Please Enter A Valid Email.')
            return redirect('/alt')
    else:
        return redirect('/alt')


def users_alt(request):
    print("alt users")
    context = {
        'users': all_emails()
    }
    return render(request, 'validation_alt/templates/validation_alt/users.html', context)


def delete_alt(request, email_id):
    print("alt delete")
    messages.success(request, 'You successfully removed your email address!')
    delete_email(email_id)
    return redirect('/alt/users_alt')
