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
            [1, 'Report Truthfully'],
            [2, 'Take ${0:.1f} of your counterpart\'s money.'.format(self.participant.vars['xdraws'][self.subsession.round_number - 1])],
            [3, 'Take ${0:.1f} of your counterpart\'s money.'.format(self.participant.vars['ydraws'][self.subsession.round_number - 1])],
            [4, 'Take ${0:.1f} of your counterpart\'s money.'.format(self.participant.vars['zdraws'][self.subsession.round_number - 1])],
        ]
        return choices

    def vars_for_template(self):
        return {'W': round(self.participant.vars['Wdraws'][self.subsession.round_number - 1], 1),
                '10W': round(10 - self.participant.vars['Wdraws'][self.subsession.round_number - 1], 1),
                'x': round(self.participant.vars['xdraws'][self.subsession.round_number - 1], 1),
                'y': round(self.participant.vars['ydraws'][self.subsession.round_number - 1], 1),
                'z': round(self.participant.vars['zdraws'][self.subsession.round_number - 1], 1)}


page_sequence = [
    Instructions,
    Quiz,
    Decisions
]
