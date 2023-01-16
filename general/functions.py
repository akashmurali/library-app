import string
import random
from random import randint





def get_auto_id(model):
    auto_id = 1
    latest_auto_id =  model.objects.all().order_by("-date_added")[:1]
    if latest_auto_id:
        for auto in latest_auto_id:
            auto_id = auto.auto_id + 1
    return auto_id


def generate_unique_id(size=8, chars=string.ascii_lowercase + string.digits):
    
    return ''.join(random.choice(chars) for _ in range(size))

def randomnumber(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)