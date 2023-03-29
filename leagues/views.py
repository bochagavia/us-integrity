import logging
import traceback
from django.shortcuts import render, redirect
from leagues.models import Leagues


def index(request):
    try:
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
    except Exception as e:
        logging.error(traceback.format_exc())
        return render(request, 'error.html', context=context)


def handler404(request, *args, **argv):
    return redirect('/')


def handler500(request, *args, **argv):
    return render(request, 'error.html')