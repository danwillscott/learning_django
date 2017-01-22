from django.shortcuts import render, redirect
import models
# Create your views here.


def index(request):
    random_word = {
        'random': "REMOVED RANDOM"
    }

    print(request.get_raw_uri())  # this prints the full path to this page when loaded
    return render(request, 'survey/index.html', random_word)


def survey(request):
    return render(request, 'survey/survey.html')


def new_user(request):
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('location') and request.POST.get('language') and request.POST.get('comment'):
            print ('passed test')
            request.session['user'] = request.POST.get('user')
            request.session['location'] = request.POST.get('location')
            request.session['language'] = request.POST.get('language')
            request.session['comment'] = request.POST.get('comment')
            if 'count' not in request.session:
                request.session['count'] = 1
            elif 'count' in request.session:
                request.session['count'] += 1
            return redirect('/survey')
        else:
            return redirect('/')
