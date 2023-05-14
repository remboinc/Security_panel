from django.shortcuts import get_object_or_404
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()
    this_passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=this_passcard)
    passcard_history = []
    for visit in this_passcard_visits:
        this_visit = {
            'entered_at': visit.entered_at,
            'duration': Visit.format_duration(Visit.get_duration(visit)),
            'is_strange': visit.is_visit_long()
        }
        passcard_history.append(this_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_history
    }
    return render(request, 'passcard_info.html', context)
