from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Quiz(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']


class Belief1(Page):
    form_model = 'player'
    form_fields = ['belief1']


class Belief2(Page):
    form_model = 'player'
    form_fields = ['belief2']


class Belief3(Page):
    form_model = 'player'
    form_fields = ['belief3']


class Decision1(Page):
    form_model = 'player'
    form_fields = ['decision1']


class Decision2(Page):
    form_model = 'player'
    form_fields = ['decision2']


class Decision3(Page):
    form_model = 'player'
    form_fields = ['decision3']


class Decision4(Page):
    form_model = 'player'
    form_fields = ['decision4']


class Decision5(Page):
    form_model = 'player'
    form_fields = ['decision5']


class Decision6(Page):
    form_model = 'player'
    form_fields = ['decision6']


class RecordDecisions(WaitPage):
    def after_all_players_arrive(self):
        self.group.keep_decisions()


page_sequence = [
    Instructions,
    Quiz,
    Belief1,
    Belief2,
    Belief3,
    Decision1,
    Decision2,
    Decision3,
    Decision4,
    Decision5,
    Decision6,
    RecordDecisions
]
