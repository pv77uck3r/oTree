from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from operator import itemgetter

class Instructions(Page):

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_riskloss2')
        }

    def before_next_page(self):
        self.player.record_number()


class Risk(Page):

    form_model = 'player'
    form_fields = ['risk_decision']

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_riskloss2')
        }


class Loss(Page):

    form_model = 'player'
    form_fields = ['loss_decision_1', 'loss_decision_2', 'loss_decision_3', 'loss_decision_4', 'loss_decision_5',
                   'loss_decision_6', 'loss_decision_7', 'loss_decision_8', 'loss_decision_9', 'loss_decision_10',
                   'loss_decision_11', 'loss_decision_12']

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_riskloss2')
        }


class Ambiguity(Page):
    form_model = 'player'
    form_fields = ['ambiguity_color_decision_1', 'ambiguity_color_decision_2', 'ambiguity_color_decision_3',
                   'ambiguity_color_decision_4', 'ambiguity_price_decision_1', 'ambiguity_price_decision_2',
                   'ambiguity_price_decision_3', 'ambiguity_price_decision_4', ]

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_riskloss2')
        }


class ReadyForResults(Page):

    def before_next_page(self):
        self.player.payoffs()
        self.player.set_payoffs()
        self.player.set_big_payoff()


class LittleResults(Page):

    def vars_for_template(self):
        if self.session.vars['paymentmodule'] == 1:
            modulechosen = 'first'
            singleloss = None
            otherroll = None
            urn1 = 0
            urn2 = 0
            urn3 = 0
            urn4 = 0
            totalurn = 0
            if self.player.participant.vars['HTRisk'] == 0:
                randomroll = 'less than or equal to 50'
            else:
                randomroll = 'greater than 50'
        else:
            if self.session.vars['paymentmodule'] == 2:
                modulechosen = 'second'
                urn1 = 0
                urn2 = 0
                urn3 = 0
                urn4 = 0
                totalurn = 0
                if self.player.participant.vars['LossDecision'] % 2 == 1:
                    singleloss = 1
                    otherroll = None
                    if self.player.participant.vars['HTLoss'] == 0:
                        randomroll = 'less than or equal to 50'
                    else:
                        randomroll = 'greater than 50'
                else:
                    randomroll = self.player.participant.vars['numheadsLoss']
                    otherroll = Constants.num_cointosses - randomroll
                    singleloss = None
            else:
                modulechosen = 'third'
                randomroll = 'Not Yet Defined'
                urn1 = self.player.ambiguity_payment1
                urn2 = self.player.ambiguity_payment2
                urn3 = self.player.ambiguity_payment3
                urn4 = self.player.ambiguity_payment4
                totalurn = self.player.ambiguity_payment1 + self.player.ambiguity_payment2 + \
                           self.player.ambiguity_payment3 + self.player.ambiguity_payment4
                singleloss = None
                otherroll = None

        return {'modulechosen': modulechosen,
                'randomroll': randomroll,
                'riskchoice': self.player.risk_decision,
                'lossdecision': self.player.participant.vars['LossDecision'],
                'singleloss': singleloss,
                'otherroll': otherroll,
                'riskpayment': format(self.participant.vars['payoffmodule5'], '.2f'),
                'losspayment': format(self.participant.vars['payoffmodule5'], '.2f'),
                'urn1': format(urn1, '.2f'),
                'urn2': format(urn2, '.2f'),
                'urn3': format(urn3, '.2f'),
                'urn4': format(urn4, '.2f'),
                'totalurn': format(totalurn, '.2f'),
                'Part': self.session.config['app_sequence'].index('criminal_riskloss2')
                }

class Results(Page):

    def vars_for_template(self):

        SequencePayoff = [
            [self.participant.vars['thefirstone'], self.participant.vars['payoffmodule1']],
            [self.participant.vars['thesecondone'], self.participant.vars['payoffmodule2']],
            [self.participant.vars['thethirdone'], self.participant.vars['payoffmodule3']],
            [self.participant.vars['thethirdone'], self.participant.vars['payoffmodule4']],
            [self.participant.vars['thefifthone'], self.participant.vars['payoffmodule5']]
        ]

        NSP = sorted(SequencePayoff, key=itemgetter(0))

        return {'payoff1': format(NSP[0][1], '.2f'),
                'payoff2': format(NSP[1][1], '.2f'),
                'payoff3': format(NSP[2][1], '.2f'),
                'payoff4': format(NSP[3][1], '.2f'),
                'payoff5': format(NSP[4][1], '.2f'),
                'finalpayoff': format(self.participant.vars['bigpayoff'], '.2f'),
                'SubjectID': self.participant.id_in_session
                }


First = [Instructions]

Second = [
    Risk,
    Loss,
    Ambiguity
]

random.shuffle(Second)

Third = [
    ReadyForResults,
    LittleResults,
    Results
]

page_sequence = First + Second + Third
