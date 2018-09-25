from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Risk(Page):

    form_model = 'player'
    form_fields = ['risk_decision']


class Loss(Page):

    form_model = 'player'
    form_fields = ['loss_decision_1', 'loss_decision_2', 'loss_decision_3', 'loss_decision_4', 'loss_decision_5',
                   'loss_decision_6', 'loss_decision_7', 'loss_decision_8', 'loss_decision_9', 'loss_decision_10',
                   'loss_decision_11', 'loss_decision_12']


page_sequence = [
    Risk,
    Loss
]
