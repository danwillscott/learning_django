from django.shortcuts import render, redirect
from models import User, Interest

# Create your views here.


def index(request):
    return render(request, 'user_interest_app/index.html')


def add(request):
    if request.method == 'POST':
        interest
        interest_list = Interest.objects.filter(name=request.POST['interest'])
        user_list = User.objects.filter(name=request.POST['name'])
        if not interest_list:
            interest = Interest.objects.create(name=request.POST['interest'])
        else:
            interest = interest_list[0]

        if not user_list:
        new_user = User.objects.create(name=request.POST['name'])
        new_interest = Interest.objects.create(name=request.POST['interest'])
        new_user.interest.add(new_interest)
        print(User.objects.all())
        return redirect('/interests')
    return redirect('/')


def interests(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'user_interest_app/interests.html', context=context)


def users(request, id):
    context = {
        'interests': Interest.objects.get(id=id)
    }
    return render(request, 'user_interest_app/users.html', context)
