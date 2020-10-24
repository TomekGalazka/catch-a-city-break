from django.http import request
from django.utils import timezone
from datetime import datetime
import pytz


def time_now(request):
    # waw = pytz.timezone('Europe/Warsaw')
    # local_time = datetime.now().astimezone(waw)
    ctx = {
        'now': timezone.now(),
        # 'now': datetime.now(pytz.timezone('Europe/Warsaw'))
    }
    return ctx

