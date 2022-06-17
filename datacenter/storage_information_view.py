from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit


def format_duration(seconds):
    duration = '%02d:%02d:%02d' % (seconds // 3600, 
                                   (seconds % 3600) // 60,
                                   seconds  % 60)
    return duration


def storage_information_view(request):
    current_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in current_visits:
        entered_time = localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M')
        duration = format_duration(visit.duration)
        
        visit_to_add = {
                        'who_entered': visit.passcard.owner_name,
                        'entered_at': entered_time,
                        'duration': duration,
                        'is_strange': visit.is_visit_long
                       }
        non_closed_visits.append(visit_to_add)
   
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
