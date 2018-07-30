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
    form_fields = ['quiz1', 'quiz2', 'quiz3']

    def quiz1_error_message(self, value):
        if value != 1:
            return 'Question 1 is incorrect. Please try again.'

    def quiz2_error_message(self, value):
        if value != 1:
            return 'Question 2 is incorrect. Please try again.'

    def quiz3_error_message(self, value):
        if value != 1:
            return 'Question 3 is incorrect. Please try again.'


class Preparation(Page):
    pass


class Decisions(Page):
    pass


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Quiz,
    Preparation,
    Decisions,
    Results
]
