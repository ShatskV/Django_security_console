from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit


def format_duration(seconds):
    duration = '%02d:%02d:%02d' % (seconds // 3600, 
                                   (seconds % 3600) // 60,
                                   seconds  % 60)
    return duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = passcard.visit_set.all()
    this_passcard_visits = []
    for visit in visits:
        entered_time = localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M')
        duration = format_duration(visit.duration)
        passcard_visit = {
                'entered_at': entered_time,
                'duration': duration,
                'is_strange': visit.is_visit_long
                }
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
