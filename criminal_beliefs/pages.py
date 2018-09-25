from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Decisions(Page):
    form_model = 'player'
    form_fields = ['belief']

    def vars_for_template(self):
        if self.player.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1] ==

class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decisions
]
