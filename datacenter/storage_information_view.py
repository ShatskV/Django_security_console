from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.format_utils import format_duration
from datacenter.models import Passcard, Visit


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at=None)
    serialized_visits = []
    for visit in unclosed_visits:
        entered_time = localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M')
        duration = format_duration(visit.duration)
        
        visit_to_add = {
                        'who_entered': visit.passcard.owner_name,
                        'entered_at': entered_time,
                        'duration': duration,
                        'is_strange': visit.is_visit_long
                       }
        serialized_visits.append(visit_to_add)
   
    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
