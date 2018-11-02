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
    name_in_url = 'criminal_riskloss2'
    players_per_group = None
    num_rounds = 1
    num_cointosses = 6


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            # Here we choose a random module for payment
            # 1 - risk
            # 2 - loss
            # 3 - ambiguity
            self.session.vars['paymentmodule'] = np.random.choice([1, 2])
            if self.session.vars['paymentmodule'] == 1:
                for p in self.get_players():
                    # If we pay for risk, we select a 0 - Heads or 1 - Tails.
                    p.participant.vars['HTRisk'] = np.random.choice([0, 1])
                    p.participant.vars['LossDecision'] = None
                    p.participant.vars['HTLoss'] = None
                    p.participant.vars['numheadsLoss'] = None
                    p.ModuleChoice = self.session.vars['paymentmodule']
            elif self.session.vars['paymentmodule'] == 2:
                    for p in self.get_players():
                        # If we pay for loss, we select a random decision they made and also a coin toss or series
                        # of coin tosses
                        p.participant.vars['HTRisk'] = None
                        p.participant.vars['LossDecision'] = np.random.choice(list(np.arange(1, 13)))
                        p.LossDecision = p.participant.vars['LossDecision']
                        if p.participant.vars['LossDecision'] % 2 == 1:
                            p.participant.vars['HTLoss'] = np.random.choice([1, 2])
                        else:
                            p.participant.vars['numheadsLoss'] = np.random.binomial(Constants.num_cointosses, p=0.5)
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
        label='Decision 4: This decision consists of six independent repetitions of the gamble in Decision 3. That is, '
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
        label='Decision 6: This decision consists of six independent repetitions of the gamble in Decision 5. That is, '
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
        label='Decision 8: This decision consists of six independent repetitions of the gamble in Decision 7. That is, '
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
        label='Decision 10: This decision consists of six independent repetitions of the gamble in Decision 9. That is, '
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
        label='Decision 12: This decision consists of six independent repetitions of the gamble in Decision 11. That is, '
              'you will be paid off the outcomes of six independent coin tosses.'
    )

    risk_payment = models.FloatField()
    loss_payment = models.FloatField()

    Final_Payoff = models.CurrencyField()

    ModuleChoice = models.IntegerField()
    LossDecision = models.IntegerField()

    def payoffs(self):
        if self.session.vars['paymentmodule'] == 1:
            self.ModuleChoice = self.session.vars['paymentmodule']
            self.loss_payment = 0
            if self.risk_decision == 1:
                if self.participant.vars['HTRisk'] == 0:
                    self.risk_payment = 4.30
                else:
                    self.risk_payment = 5.65
            else:
                if self.risk_decision == 2:
                    if self.participant.vars['HTRisk'] == 0:
                        self.risk_payment = 4.15
                    else:
                        self.risk_payment = 5.95
                else:
                    if self.risk_decision == 3:
                        if self.participant.vars['HTRisk'] == 0:
                            self.risk_payment = 4.00
                        else:
                            self.risk_payment = 6.25
                    else:
                        if self.risk_decision == 4:
                            if self.participant.vars['HTRisk'] == 0:
                                self.risk_payment = 3.85
                            else:
                                self.risk_payment = 6.55
                        else:
                            if self.risk_decision == 5:
                                if self.participant.vars['HTRisk'] == 0:
                                    self.risk_payment = 3.65
                                else:
                                    self.risk_payment = 6.90
                            else:
                                if self.risk_decision == 6:
                                    if self.participant.vars['HTRisk'] == 0:
                                        self.risk_payment = 3.45
                                    else:
                                        self.risk_payment = 7.20
                                else:
                                    if self.risk_decision == 7:
                                        if self.participant.vars['HTRisk'] == 0:
                                            self.risk_payment = 3.10
                                        else:
                                            self.risk_payment = 7.60
        else:
            if self.session.vars['paymentmodule'] == 2:
                self.risk_payment = 0
                self.ModuleChoice = self.session.vars['paymentmodule']
                self.LossDecision = self.participant.vars['LossDecision']
                if self.participant.vars['LossDecision'] % 2 == 1:
                    if self.participant.vars['LossDecision'] == 1:
                        if self.loss_decision_1 == 1:
                            if self.participant.vars['HTLoss'] == 0:
                                self.loss_payment = -2.00
                            else:
                                self.loss_payment = 6.00
                        else:
                            self.loss_payment = 0
                    else:
                        if self.participant.vars['LossDecision'] == 3:
                            if self.loss_decision_3 == 1:
                                if self.participant.vars['HTLoss'] == 0:
                                    self.loss_payment = -3.00
                                else:
                                    self.loss_payment = 6.00
                            else:
                                self.loss_payment = 0
                        else:
                            if self.participant.vars['LossDecision'] == 5:
                                if self.loss_decision_5 == 1:
                                    if self.participant.vars['HTLoss'] == 0:
                                        self.loss_payment = -4.00
                                    else:
                                        self.loss_payment = 6.00
                                else:
                                    self.loss_payment = 0
                            else:
                                if self.participant.vars['LossDecision'] == 7:
                                    if self.loss_decision_7 == 1:
                                        if self.participant.vars['HTLoss'] == 0:
                                            self.loss_payment = -5.00
                                        else:
                                            self.loss_payment = 6.00
                                    else:
                                        self.loss_payment = 0
                                else:
                                    if self.participant.vars['LossDecision'] == 9:
                                        if self.loss_decision_9 == 1:
                                            if self.participant.vars['HTLoss'] == 0:
                                                self.loss_payment = -6.00
                                            else:
                                                self.loss_payment = 6.00
                                        else:
                                            self.loss_payment = 0
                                    else:
                                        if self.participant.vars['LossDecision'] == 11:
                                            if self.loss_decision_11 == 1:
                                                if self.participant.vars['HTLoss'] == 0:
                                                    self.loss_payment = -7.00
                                                else:
                                                    self.loss_payment = 6.00
                                            else:
                                                self.loss_payment = 0
                else:
                    if self.participant.vars['LossDecision'] == 2:
                        if self.loss_decision_2 == 1:
                            self.loss_payment = self.participant.vars['numheadsLoss']*6.00 + \
                                                (Constants.num_cointosses - self.participant.vars['numheadsLoss'])*-2.00
                        else:
                            self.loss_payment = 0
                    else:
                        if self.participant.vars['LossDecision'] == 4:
                            if self.loss_decision_4 == 1:
                                self.loss_payment = self.participant.vars['numheadsLoss'] * 6.00 + \
                                                    (Constants.num_cointosses - self.participant.vars[
                                                        'numheadsLoss']) * -3.00
                            else:
                                self.loss_payment = 0
                        else:
                            if self.participant.vars['LossDecision'] == 6:
                                if self.loss_decision_6 == 1:
                                    self.loss_payment = self.participant.vars['numheadsLoss'] * 6.00 + \
                                                        (Constants.num_cointosses - self.participant.vars[
                                                            'numheadsLoss']) * -4.00
                                else:
                                    self.loss_payment = 0
                            else:
                                if self.participant.vars['LossDecision'] == 8:
                                    if self.loss_decision_8 == 1:
                                        self.loss_payment = self.participant.vars['numheadsLoss'] * 6.00 + \
                                                            (Constants.num_cointosses - self.participant.vars[
                                                                'numheadsLoss']) * -5.00
                                    else:
                                        self.loss_payment = 0
                                else:
                                    if self.participant.vars['LossDecision'] == 10:
                                        if self.loss_decision_10 == 1:
                                            self.loss_payment = self.participant.vars['numheadsLoss'] * 6.00 + \
                                                                (Constants.num_cointosses - self.participant.vars[
                                                                    'numheadsLoss']) * -6.00
                                        else:
                                            self.loss_payment = 0
                                    else:
                                        if self.participant.vars['LossDecision'] == 12:
                                            if self.loss_decision_12 == 1:
                                                self.loss_payment = self.participant.vars['numheadsLoss'] * 6.00 + \
                                                                    (Constants.num_cointosses - self.participant.vars[
                                                                        'numheadsLoss']) * -7.00
                                            else:
                                                self.loss_payment = 0
            else:
                self.ModuleChoice = self.session.vars['paymentmodule']
                pass

    def set_payoffs(self):
        if self.session.vars['paymentmodule'] == 1:
            self.participant.vars['payoffmodule5'] = self.risk_payment
        else:
            if self.session.vars['paymentmodule'] == 2:
                self.participant.vars['payoffmodule5'] = self.loss_payment
            else:
                if self.session.vars['paymentmodule'] == 3:
                    self.participant.vars['payoffmodule5'] = 0

    def set_big_payoff(self):
        self.participant.vars['bigpayoff'] = 7 + \
                                             self.participant.vars['payoffmodule1'] + \
                                             self.participant.vars['payoffmodule2'] + \
                                             self.participant.vars['payoffmodule3'] + \
                                             self.participant.vars['payoffmodule4'] + \
                                             self.participant.vars['payoffmodule5']
        self.Final_Payoff = self.participant.vars['bigpayoff']
        self.participant.payoff = self.Final_Payoff

