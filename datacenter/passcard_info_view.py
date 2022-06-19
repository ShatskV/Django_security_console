from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.format_utils import format_duration
from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = passcard.visit_set.all()
    serialized_visits = []
    for visit in visits:
        entered_time = localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M')
        duration = format_duration(visit.duration)
        serialized_visit = {
                'entered_at': entered_time,
                'duration': duration,
                'is_strange': visit.is_visit_long
                }
        serialized_visits.append(serialized_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
