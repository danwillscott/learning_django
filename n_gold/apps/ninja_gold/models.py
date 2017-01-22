from __future__ import unicode_literals
import random
from django.shortcuts import render, redirect

# Create your models here.


# TODO farm 10-20 gold val is 1
# TODO cave 5-10 gold val is 2
# TODO house 2-5 gold val is 3
# TODO casino takes 0-50 or gives 0-50 gold val is 4
def find_gold(val):
    if val == 1:  # farm
        return random.randint(10, 20)
    elif val == 2:  # cave
        return random.randint(5, 10)
    elif val == 3:  # house
        return random.randint(2, 5)
    elif val == 4:  # casino
        good_bad = random.randint(1, 2)
        if good_bad == 2:
            return random.randint(-50, 0)
        elif good_bad == 1:
            return random.randint(0, 50)
    return


def message(val, won):
    if val == 1:  # farm
        return 'Earned {} gold from the farm'.format(won)
    elif val == 2:  # cave
        return 'You minded and got {} gold!'.format(won)
    elif val == 3:  # house
        return 'You found {} gold while doing house work'.format(won)
    elif val == 4:  # casino
        if won > 0:
            return 'Earned {} at the casino! Lets do it again!'.format(won)
        elif won < 0:
            return 'You lost {} at the casino. you might have a problem....'.format(won)
        elif won == 0:
            return 'you broke even earning {} gold at the casino'.format(won)
    return


def day_setter(val):
    if val > 5:  # farm
        return val + 1
    elif val == 5:  # cave
        return 0
