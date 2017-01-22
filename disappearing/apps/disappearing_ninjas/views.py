from django.shortcuts import render, redirect

# All views redirect to index.html and are dynamically adjusted


def no_ninjas(request):  # This handles the / page and shows no ninjas here
    to_template = {
        'title': "No Ninjas Here!"
    }
    return render(request, 'disappearing_ninjas/index.html', to_template)


def index(request):  # this handles the main index page
    to_template = {
        'title': 'disappearing_ninjas aka TMNT!!!',
        'img': '../../static/disappearing_ninjas/images/tmnt.png'
    }
    return render(request, 'disappearing_ninjas/templates/disappearing_ninjas/index.html', to_template)


def ninjas(request, ninja_id):
    # print(ninja_id)
    if ninja_id == 'red':
        to_template = {
            'title': 'Raphael',
            'img': '../../static/disappearing_ninjas/images/raphael.jpg'
        }
        return render(request, 'disappearing_ninjas/index.html', to_template)
    elif ninja_id == 'orange':
        to_template = {
            'title': 'Michelangelo',
            'img': '../../static/disappearing_ninjas/images/michelangelo.jpg'
        }
        return render(request, 'disappearing_ninjas/index.html', to_template)
    elif ninja_id == 'purple':
        to_template = {
            'title': 'Donatello',
            'img': '../../static/disappearing_ninjas/images/donatello.jpg'
        }
        return render(request, 'disappearing_ninjas/index.html', to_template)
    elif ninja_id == 'blue':
        to_template = {
            'title': 'Leonardo',
            'img': '../../static/disappearing_ninjas/images/leonardo.jpg'
        }
        return render(request, 'disappearing_ninjas/index.html', to_template)
    else:
        to_template = {
            'title': 'Megan Fox eww!',
            'img': '../../static/disappearing_ninjas/images/notapril.jpg'
        }
        return render(request, 'disappearing_ninjas/index.html', to_template)

