import xlrd
import os.path
from itertools import product
import numpy as np
from random import shuffle
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_riskloss'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            # Here we choose a random module for payment
            # 1 - risk
            # 2 - loss
            # 3 - ambiguity
            self.session.vars['paymentmodule'] = np.random.choice([1, 2, 3])
            if self.session.vars['paymentmodule'] == 1:
                for p in self.get_players():
                    # If we pay for risk, we select a 0 - Heads or 1 - Tails.
                    p.participant.vars['HTRisk'] = np.random.choice([0, 1])
                else:
                    if self.session.vars['paymentmodule'] == 2:
                        for x in self.get_players():
                            # If we pay for loss, we select a random decision they made and also a coin toss
                            x.participant.vars['LossDecision'] = np.random.choice(range(1, 13))
                            if x.participant.vars['LossDecision'] % 2 == 1:
                                x.participant.vars['HTLoss'] = np.random.choice([1, 2])
                            else:
                                x.participant.vars['numheadsLoss'] = np.random.binomial(6, p=0.5)
                        else:
                            pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    risk_decision = models.IntegerField(
        choices=[
            [1, 'A: 50% chance to get $4.30, 50% chance to get $5.65'],
            [2, 'B: 50% chance to get $4.15, 50% chance to get $5.95'],
            [3, 'C: 50% chance to get $4.00, 50% chance to get $6.25'],
            [4, 'D: 50% chance to get $3.85, 50% chance to get $6.55'],
            [5, 'E: 50% chance to get $3.65, 50% chance to get $6.90'],
            [6, 'F: 50% chance to get $3.45, 50% chance to get $7.20'],
            [7, 'G: 50% chance to get $3.10, 50% chance to get $7.60']
        ],
        widget=widgets.RadioSelect
    )

    loss_decision_1 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 1: 50% chance to LOSE $2.00, 50% chance to gain $6.00'
    )

    loss_decision_2 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 2: This decision consists of six independent repetitions of the gamble in Decision 1. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )

    loss_decision_3 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 3: 50% chance to LOSE $3.00, 50% chance to gain $6.00'
    )

    loss_decision_4 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 2: This decision consists of six independent repetitions of the gamble in Decision 3. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )

    loss_decision_5 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 5: 50% chance to LOSE $2.00, 50% chance to gain $6.00'
    )

    loss_decision_6 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 2: This decision consists of six independent repetitions of the gamble in Decision 5. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )

    loss_decision_7 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 7: 50% chance to LOSE $2.00, 50% chance to gain $6.00'
    )

    loss_decision_8 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 2: This decision consists of six independent repetitions of the gamble in Decision 7. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )

    loss_decision_9 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 9: 50% chance to LOSE $2.00, 50% chance to gain $6.00'
    )

    loss_decision_10 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 2: This decision consists of six independent repetitions of the gamble in Decision 9. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )

    loss_decision_11 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 11: 50% chance to LOSE $2.00, 50% chance to gain $6.00'
    )

    loss_decision_12 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 2: This decision consists of six independent repetitions of the gamble in Decision 11. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )


