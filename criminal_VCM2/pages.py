from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Quiz(Page):
    pass


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
    form_fields = ['contribution1']


class Decision2(Page):
    form_model = 'player'
    form_fields = ['contribution2']


class Decision3(Page):
    form_model = 'player'
    form_fields = ['contribution3']


class Decision4(Page):
    form_model = 'player'
    form_fields = ['contribution4']


class Decision5(Page):
    form_model = 'player'
    form_fields = ['contribution5']


class Decision6(Page):
    form_model = 'player'
    form_fields = ['contribution6']


class SetGroups1(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_1()


class GenVCMGame1Payoffs(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff_1()


class SetGroups2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_2()


class KeepDecisions(WaitPage):
    def after_all_players_arrive(self):
        self.group.keep_contributions()


class GenVCMGame2Payoffs(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff_2()


page_sequence = [
    SetGroups1,
    GenVCMGame1Payoffs,
    SetGroups2,
    Instructions,
    Belief1,
    Belief2,
    Belief3,
    Decision1,
    Decision2,
    Decision3,
    Decision4,
    Decision5,
    Decision6,
    KeepDecisions,
    GenVCMGame2Payoffs
]
