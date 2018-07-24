from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):

    def play_round(self):
        yield Submission(views.retainDraws, check_html=False)
        yield (views.Decision, {'InnovateorImitateButton': 100, 'Innovate': False, 'NoInnovate': False})
        yield (views.Results)
        yield (views.FinalResults)
        yield (views.EndOfSuperGamesResults)
