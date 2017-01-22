from django.shortcuts import render

# Create your views here.


def index(request):
    print(request.get_raw_uri())  # this prints the full path to this page when loaded
    return render(request, 'first_app/index.html')


def show(request):
    print(request.get_raw_uri())  # this prints the full path to this page when loaded
    return render(request, 'first_app/show_user.html')