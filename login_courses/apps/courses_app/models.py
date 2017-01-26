from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def add_course(name, description):
    Course.objects.create(name=name, description=description)


def show_courses():
    return Course.objects.all()


def delete_course(course_id):
    Course.objects.get(id=course_id).delete()
    pass


def get_course(course_id):
    return Course.objects.get(id=course_id)
