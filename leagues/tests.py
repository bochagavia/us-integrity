from django.test import TestCase
from leagues.models import Leagues, Teams


class TestListLeaguesView(TestCase):
    def setUp(self):
        for i in range(4):
            Leagues.objects.create(abbr=f'L{i}', name=f'League {i}')

        for i in range(30):
            Teams.objects.create(abbr=f'T{i}', name=f'Team {i}', league=Leagues.objects.first())

    def test_when_ok_then_return_template_with_context(self):
        response = self.client.get('')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'list_leagues.html')

        self.assertEqual(4, len(response.context['leagues']))
        league0 = response.context['leagues'][0]
        self.assertEqual('League 0', league0['name'])
        self.assertEqual(30, len(league0['teams']))

