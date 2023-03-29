from django.shortcuts import render
from leagues.models import Leagues


def index(request):
    leagues = Leagues.objects.all()
    context = {'leagues': []}

    for league in leagues:
        context['leagues'].append({
            'abbr': league.abbr,
            'name': league.name,
            'id': league.id,
            'teams': [{'name': team.name, 'abbr': team.abbr} for team in league.teams_set.all()]
        })

    return render(request, 'list_leagues.html', context=context)
