from django.shortcuts import render
from datetime import datetime
import models
# Create your views here.


#  created an index page TODO

def index(request):
    the_time = datetime.now()
    print (models.day_format(the_time.day))
    time_break_down = {
        'day': models.day_format(the_time.day),
        'month': models.month_format(the_time.month),
        'year': the_time.year,
        'hour': the_time.hour + 16,
        'minute': the_time.minute
    }
    print (the_time.day)
    print (the_time.strftime('%Y-%m-%d %H:%M:%S'))
    return render(request, 'display_time_app/templates/show_time/index.html', time_break_down)