from django.http import request
from datetime import datetime
import pytz


def time_now(request):
    waw = pytz.timezone('Europe/Warsaw')
    local_time = datetime.now().astimezone(waw)
    ctx = {
        'now': local_time,
        # 'now': datetime.now(pytz.timezone('Europe/Warsaw'))
    }
    return ctx

