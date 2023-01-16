from datetime import datetime,timedelta
from books.models import BookRequest



def disable_read(request):
    curr_time = datetime.now()
    queryset = BookRequest.objects.filter(is_deleted=False,is_accepted=True,is_completed=False).search_related('book')
    for i in queryset:
        start_time = i.start_time
        time_interval = i.time_interval
        interval_in = i.interval_in
        if interval_in == 'hours':
            time = start_time + timedelta(hours=int(time_interval))

        else:
            time = start_time + timedelta(minutes=int(time_interval))

        if curr_time >= time:
            i.is_completed = True
            i.save()               
