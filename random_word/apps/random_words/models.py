from __future__ import unicode_literals
import random
import string
# from django.db import models

# Create your models here.


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


