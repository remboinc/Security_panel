from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in not_leaved:
        entered_at = visit.entered_at
        visit_duration = visit.get_duration()
        format_duration = Visit.format_duration(visit_duration)
        is_strange = visit.is_visit_long(minutes=60)
        owner_name = visit.passcard.owner_name

        visit_info = {
            'who_entered': owner_name,
            'entered_at': entered_at,
            'duration': format_duration,
            'is_strange': is_strange,
        }

        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
