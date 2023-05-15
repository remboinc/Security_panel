from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)

    for visit in not_leaved:
        entered_at = Visit.objects.filter(leaved_at=None)[0].entered_at
        visit_duration = visit.get_duration(visit)
        format_duration = visit.format_duration(visit_duration)
        is_strange = visit.is_visit_long(visit, minutes=60)
        names = ", ".join(visit)

        non_closed_visits = [
            {
                'who_entered': names,
                'entered_at': entered_at,
                'duration': format_duration,
                'is_strange': is_strange,
            }
        ]
        context = {
            'non_closed_visits': non_closed_visits,
        }
        non_closed_visits.append(visit.passcard.owner_name)
        return render(request, 'storage_information.html', context)
