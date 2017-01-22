from django.shortcuts import render, redirect

from models import find_gold, message, day_setter

# Create your views here.


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'message' not in request.session:
        request.session['message'] = ['welcome', 'next value', "one more"]


    return render(request, 'ninja_gold/ninja_gold.html')


def gold(request):
    if request.method == 'POST':
        if 'day' not in request.session:
            request.session['day'] = 0
            request.session['day1'] = ''
            request.session['day2'] = ''
            request.session['day3'] = ''
            request.session['day4'] = ''
            request.session['day5'] = ''
        request.session['day'] = day_setter(request.session['day'])
        value = int(request.POST.get('gold'))
        golds = find_gold(value)
        request.session['message'] = message(value, gold)
        request.session['gold'] += golds

        context = {
            'day1': request.session['day1'],
            'day2': request.session['day2'],
            'day3': request.session['day3'],
            'day4': request.session['day4'],
            'day5': request.session['day5']

        }
        return render(request, 'ninja_gold/ninja_gold.html', context)
    return redirect('/')


