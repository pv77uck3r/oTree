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
    name_in_url = 'criminal_riskloss_2'
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
            self.session.vars['paymentmodule'] = np.random.choice([1, 2, 3])
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
            elif self.session.vars['paymentmodule'] == 3:
                for p in self.get_players():
                    p.participant.vars['LossDecision'] = None
                    p.participant.vars['HTLoss'] = None
                    p.participant.vars['numheadsLoss'] = None
                    p.participant.vars['HTRisk'] = None
                self.session.vars['redball1'] = 0.5
                self.session.vars['redball2'] = np.random.choice([0.4, 0.5, 0.6])
                self.session.vars['redball3'] = np.random.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
                self.session.vars['redball4'] = np.random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
                self.session.vars['randprice1'] = np.random.choice(np.linspace(0,2.51,250,endpoint=False))
                self.session.vars['randprice2'] = np.random.choice(np.linspace(0,2.51,250,endpoint=False))
                self.session.vars['randprice3'] = np.random.choice(np.linspace(0,2.51,250,endpoint=False))
                self.session.vars['randprice4'] = np.random.choice(np.linspace(0,2.51,250,endpoint=False))


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    risk_decision = models.IntegerField(
        choices=[
            [1, 'A: 50% chance to get $2.80, 50% chance to get $2.80'],
            [2, 'B: 50% chance to get $2.40, 50% chance to get $3.60'],
            [3, 'C: 50% chance to get $2.00, 50% chance to get $4.40'],
            [4, 'D: 50% chance to get $1.60, 50% chance to get $5.20'],
            [5, 'E: 50% chance to get $1.20, 50% chance to get $6.00'],
            [6, 'F: 50% chance to get $0.20, 50% chance to get $7.00']
        ],
        widget=widgets.RadioSelect
    )

    loss_decision_1 = models.IntegerField(
        choices=[
            [1, 'Accept'],
            [2, 'Reject']
        ],
        widget=widgets.RadioSelectHorizontal,
        label='Decision 1: 50% chance to LOSE 2 dimes, 50% chance to GAIN 6 dimes'
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
        label='Decision 3: 50% chance to LOSE 3 dimes, 50% chance to GAIN 6 dimes'
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
        label='Decision 5: 50% chance to LOSE 4 dimes, 50% chance to GAIN 6 dimes'
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
        label='Decision 7: 50% chance to LOSE 5 dimes, 50% chance to GAIN 6 dimes'
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
        label='Decision 9: 50% chance to LOSE 6 dimes, 50% chance to GAIN 6 dimes'
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
        label='Decision 11: 50% chance to LOSE 7 dimes, 50% chance to GAIN 6 dimes'
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

    ambiguity_color_decision_1 = models.IntegerField(
        choices=[
            [1, 'Red'],
            [2, 'Blue']
        ],
        widget=widgets.RadioSelect,
        label='What color do you think the randomly drawn ball from this box will be?'
    )

    ambiguity_color_decision_2 = models.IntegerField(
        choices=[
            [1, 'Red'],
            [2, 'Blue']
        ],
        widget=widgets.RadioSelect,
        label='What color do you think the randomly drawn ball from this box will be?'
    )

    ambiguity_color_decision_3 = models.IntegerField(
        choices=[
            [1, 'Red'],
            [2, 'Blue']
        ],
        widget=widgets.RadioSelect,
        label='What color do you think the randomly drawn ball from this box will be?'
    )

    ambiguity_color_decision_4 = models.IntegerField(
        choices=[
            [1, 'Red'],
            [2, 'Blue']
        ],
        widget=widgets.RadioSelect,
        label='What color do you think the randomly drawn ball from this box will be?'
    )

    ambiguity_price_decision_1 = models.FloatField(
        min=0,
        max=2.50,
        label='What price would you be willing to sell your bet for?'
    )

    ambiguity_price_decision_2 = models.FloatField(
        min=0,
        max=2.50,
        label='What price would you be willing to sell your bet for?'
    )

    ambiguity_price_decision_3 = models.FloatField(
        min=0,
        max=2.50,
        label='What price would you be willing to sell your bet for?'
    )

    ambiguity_price_decision_4 = models.FloatField(
        min=0,
        max=2.50,
        label='What price would you be willing to sell your bet for?'
    )

    risk_payment = models.FloatField()
    loss_payment = models.FloatField()
    ambiguity_payment = models.FloatField()
    ambiguity_payment1 = models.FloatField()
    ambiguity_payment2 = models.FloatField()
    ambiguity_payment3 = models.FloatField()
    ambiguity_payment4 = models.FloatField()

    Final_Payoff = models.CurrencyField()

    ModuleChoice = models.IntegerField()
    LossDecision = models.IntegerField()

    def payoffs(self):
        if self.session.vars['paymentmodule'] == 1:
            self.ModuleChoice = self.session.vars['paymentmodule']
            self.loss_payment = 0
            if self.risk_decision == 1:
                if self.participant.vars['HTRisk'] == 0:
                    self.risk_payment = 2.80
                else:
                    self.risk_payment = 2.80
            else:
                if self.risk_decision == 2:
                    if self.participant.vars['HTRisk'] == 0:
                        self.risk_payment = 2.40
                    else:
                        self.risk_payment = 3.60
                else:
                    if self.risk_decision == 3:
                        if self.participant.vars['HTRisk'] == 0:
                            self.risk_payment = 2.00
                        else:
                            self.risk_payment = 4.40
                    else:
                        if self.risk_decision == 4:
                            if self.participant.vars['HTRisk'] == 0:
                                self.risk_payment = 1.60
                            else:
                                self.risk_payment = 5.20
                        else:
                            if self.risk_decision == 5:
                                if self.participant.vars['HTRisk'] == 0:
                                    self.risk_payment = 1.20
                                else:
                                    self.risk_payment = 6.00
                            else:
                                if self.risk_decision == 6:
                                    if self.participant.vars['HTRisk'] == 0:
                                        self.risk_payment = 0.20
                                    else:
                                        self.risk_payment = 7.00
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
                if self.session.vars['paymentmodule'] == 3:
                    self.risk_payment = 0
                    self.loss_payment = 0
                    if self.session.vars['randprice1'] > self.ambiguity_price_decision_1:
                        self.ambiguity_payment1 = self.session.vars['randprice1']
                    else:
                        ## 1 - red, 0 - blue
                        ballcolor = np.random.binomial(1, self.session.vars['redball1'])
                        if ballcolor == self.ambiguity_color_decision_1:
                            self.ambiguity_payment1 = 2.50
                        else:
                            self.ambiguity_payment1 = 0

                    if self.session.vars['randprice2'] > self.ambiguity_price_decision_2:
                        self.ambiguity_payment2 = self.session.vars['randprice2']
                    else:
                        ## 1 - red, 0 - blue
                        ballcolor = np.random.binomial(1, self.session.vars['redball2'])
                        if ballcolor == self.ambiguity_color_decision_2:
                            self.ambiguity_payment2 = 2.50
                        else:
                            self.ambiguity_payment2 = 0

                    if self.session.vars['randprice3'] > self.ambiguity_price_decision_3:
                        self.ambiguity_payment3 = self.session.vars['randprice3']
                    else:
                        ## 1 - red, 0 - blue
                        ballcolor = np.random.binomial(1, self.session.vars['redball3'])
                        if ballcolor == self.ambiguity_color_decision_3:
                            self.ambiguity_payment3 = 2.50
                        else:
                            self.ambiguity_payment3 = 0

                    if self.session.vars['randprice4'] > self.ambiguity_price_decision_4:
                        self.ambiguity_payment4 = self.session.vars['randprice4']
                    else:
                        ## 1 - red, 0 - blue
                        ballcolor = np.random.binomial(1, self.session.vars['redball4'])
                        if ballcolor == self.ambiguity_color_decision_4:
                            self.ambiguity_payment4 = 2.50
                        else:
                            self.ambiguity_payment4 = 0


    def set_payoffs(self):
        if self.session.vars['paymentmodule'] == 1:
            self.participant.vars['payoffmodule5'] = self.risk_payment
        else:
            if self.session.vars['paymentmodule'] == 2:
                self.participant.vars['payoffmodule5'] = self.loss_payment * 0.10
            else:
                if self.session.vars['paymentmodule'] == 3:
                    self.participant.vars['payoffmodule5'] = self.ambiguity_payment1 + self.ambiguity_payment2 + \
                                                             self.ambiguity_payment3 + self.ambiguity_payment4

    def set_big_payoff(self):
        self.participant.vars['bigpayoff'] = 7 + \
                                             self.participant.vars['payoffmodule1'] * 0.25 + \
                                             self.participant.vars['payoffmodule2'] + \
                                             self.participant.vars['payoffmodule3'] + \
                                             self.participant.vars['payoffmodule4'] * 0.25 + \
                                             self.participant.vars['payoffmodule5']
        self.Final_Payoff = self.participant.vars['bigpayoff']
        self.participant.payoff = self.Final_Payoff

