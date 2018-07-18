from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class QuizI(Page):
    form_model = 'player'
    form_fields = ['investor_quiz1', 'investor_quiz2', 'investor_quiz3', 'investor_quiz4']

    def is_displayed(self):
        return self.player.role == 'Investor'


class QuizT(Page):
    form_model = 'player'
    form_fields = ['trustee_quiz1', 'trustee_quiz2', 'trustee_quiz3']

    def is_displayed(self):
        return self.player.role == 'Trustee'


class DecisionsI(Page):
    form_model = 'group'
    form_fields = ['investor_decision1', 'investor_decision2', 'investor_decision3', 'investor_decision4',
                   'investor_decision5']

    def is_displayed(self):
        return self.player.role == 'Investor'


class DecisionsT(Page):
    form_model = 'group'
    form_fields = ['trustee_decision1', 'trustee_decision2', 'trustee_decision3', 'trustee_decision4',
                   'trustee_decision5', 'trustee_decision6', 'trustee_decision7', 'trustee_decision8',
                   'trustee_decision9', 'trustee_decision10']

    def is_displayed(self):
        return self.player.role == 'Trustee'


page_sequence = [
    Instructions,
    QuizI,
    QuizT,
    DecisionsI,
    DecisionsT
]
