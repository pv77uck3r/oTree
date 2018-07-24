from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['quiz1', 'quiz2']

    def quiz1_error_message(self, value):
        if value != 2:
            return 'Question 1 is incorrect. Please try again.'

    def quiz2_error_message(self, value):
        if value != 2:
            return 'Question 2 is incorrect. Please try again.'


class Decisions(Page):

    form_model = 'group'
    form_fields = ['ThiefChoice']

    def ThiefChoice_choices(self):
        choices = [
            ['Report Truthfully'],
            ['Take $', self.session.vars['xdraws'][self.player.id_in_subsession][self.subsession.round_number],
             'of your counterpart\'s money.'],
            ['Take $', self.session.vars['ydraws'][self.player.id_in_subsession][self.subsession.round_number],
             'of your counterpart\'s money.'],
            ['Take $', self.session.vars['zdraws'][self.player.id_in_subsession][self.subsession.round_number],
             'of your counterpart\'s money.'],
        ]
        return choices

    def vars_for_template(self):
        return {'W': self.session.vars['Wdraws'][self.player.id_in_subsession][self.subsession.round_number],
                '10-W': 10 - self.session.vars['Wdraws'][self.player.id_in_subsession][self.subsession.round_number],
                'x': self.session.vars['xdraws'][self.player.id_in_subsession][self.subsession.round_number],
                'y': self.session.vars['ydraws'][self.player.id_in_subsession][self.subsession.round_number],
                'z': self.session.vars['zdraws'][self.player.id_in_subsession][self.subsession.round_number]}


page_sequence = [
    Instructions,
    Quiz,
    Decisions
]
