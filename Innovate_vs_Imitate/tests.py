from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):

    def play_round(self):
        yield Submission(pages.retainDraws, check_html=False)
        yield (pages.Decision, {'InnovateorImitateButton': 100, 'Innovate': False, 'NoInnovate': False})
        yield (pages.Results)
        yield (pages.FinalResults)
        yield (pages.EndOfSuperGamesResults)
