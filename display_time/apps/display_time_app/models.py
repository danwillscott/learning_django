from __future__ import unicode_literals

from django.db import models

# Create your models here.


def day_format(day):
    # if day is 1 or 21 or 31:
    #     return str(day) + 'st'
    if day is 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21:
        return str(day) + 'th'


def month_format(month):
    if month is 1:
        return "January"
    elif month is 2:
        return "February"
    elif month is 3:
        return "March"
    elif month is 4:
        return "April"
    elif month is 5:
        return "May"
    elif month is 6:
        return "June"
    elif month is 7:
        return "July"
    elif month is 8:
        return "August"
    elif month is 9:
        return "September"
    elif month is 10:
        return "October"
    elif month is 11:
        return "November"
    elif month is 12:
        return "December"


def time_format(current_time):
    pass
