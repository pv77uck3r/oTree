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

    def before_next_page(self):
        self.player.payoffs()
        self.player.set_payoffs()
        self.player.set_big_payoff()


class LittleResults(Page):

    def vars_for_template(self):
        if self.player.participant.vars['paymentmodule'] == 1:
            modulechosen = 'first'
            if self.player.participant.vars['HTRisk'] == 0:
                randomroll = 'below 50'
            else:
                randomroll = 'greater than or equal to 50'
        else:
            if self.player.participant.vars['paymentmodule'] == 2:
                modulechosen = 'second'
                if self.player.participant.vars['LossDecision'] % 2 == 1:
                    singleloss = 1
                    if self.player.participant.vars['HTLoss'] == 0:
                        randomroll = 'below 50'
                    else:
                        randomroll = 'greater than or equal to 50'
                else:
                    randomroll = self.player.participant.vars['numberheadsLoss']
                    otherroll = Constants.num_cointosses - randomroll
            else:
                modulechosen = 'third'
                randomroll = 'Not Yet Defined'

        return {'modulechosen': modulechosen,
                'randomroll': randomroll,
                'riskchoice': self.player.risk_decision,
                'lossdecision': self.player.participant.vars['LossDecision'],
                'singleloss': singleloss,
                'otherroll': otherroll,
                'riskpayment': format(self.player.risk_payment, '.2f'),
                'losspayment': format(self.player.loss_payment, '.2f')
                }

class Results(Page):

    def vars_for_template(self):
        return {'payoff1': format(self.participant.vars['payoffmodule1']*0.25, '.2f'),
                'payoff2': format(self.participant.vars['payoffmodule2'], '.2f'),
                'payoff3': format(self.participant.vars['payoffmodule3'], '.2f'),
                'payoff4': format(self.participant.vars['payoffmodule4']*0.25, '.2f'),
                'payoff5': format(self.participant.vars['payoffmodule5'], '.2f'),
                'finalpayoff': format(self.participant.vars['bigpayoff'], '.2f')
                }


page_sequence = [
    Risk,
    Loss,
    LittleResults,
    Results
]
