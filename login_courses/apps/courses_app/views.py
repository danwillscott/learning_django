from django.shortcuts import render, redirect
from models import add_course, delete_course, get_course, show_courses
# Create your views here.


def index(request):
    context = {
        'courses': show_courses()
    }
    return render(request, 'courses_app/templates/course_app/index.html', context)


def add(request):
    add_course(request.POST['course_name'], request.POST['description'])
    return redirect('/')


def edit(request, course_id):
    request.session['course_id'] = course_id
    context = {
        'id': course_id,
        'course': get_course(course_id)
    }
    return render(request, 'courses_app/templates/course_app/edit.html', context)


def delete(request):
    delete_course(request.session['course_id'])
    return redirect('/')
