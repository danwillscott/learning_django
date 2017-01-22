from django.shortcuts import render, redirect
import models
# Create your views here.


def index(request):
    # redirect('/')
    random_word = {
        'random': models.random_char(14)
    }
    if 'attempt' in request.session:
        request.session['attempt'] += 1
        print("attempt not in session")
    elif 'attempt' not in request.session:
        print ('not in session')
        request.session['attempt'] = 1
    print(request.get_raw_uri())  # this prints the full path to this page when loaded
    return render(request, 'random_words/index.html', random_word)


def new_word(request):
    if request.method == "POST":
        print('test')
    # request.session.attempt += 1
    return redirect('/')
