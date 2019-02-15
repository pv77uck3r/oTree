from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from operator import itemgetter


class Instructions(Page):

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_VCM2_ALT_ORDER_2')
        }

    def before_next_page(self):
        self.player.record_number()


class Instructions2(Page):

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_VCM2_ALT_ORDER_2')
        }


class Quiz_1(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0

    def investor_quiz1_error_message(self, value):
        if value != 4:
            return 'Question 1 is incorrect. Please try again.'

    def investor_quiz2_error_message(self, value):
        if value != 1:
            return 'Question 2 is incorrect. Please try again.'

    def investor_quiz3_error_message(self, value):
        if value != 3:
            return 'Question 3 is incorrect. Please try again.'

    def investor_quiz4_error_message(self, value):
        if value != 2:
            return 'Question 4 is incorrect. Please try again.'


class Quiz_2(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3']

    def trustee_quiz1_error_message(self, value):
        if value != 4:
            return 'Question 1 is incorrect. Please try again.'

    def trustee_quiz2_error_message(self, value):
        if value != 1:
            return 'Question 2 is incorrect. Please try again.'

    def trustee_quiz3_error_message(self, value):
        if value != 3:
            return 'Question 3 is incorrect. Please try again.'

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 1


class InterimPage(Page):

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Belief1(Page):
    form_model = 'player'
    form_fields = ['belief1']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Belief2(Page):
    form_model = 'player'
    form_fields = ['belief2']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Belief3(Page):
    form_model = 'player'
    form_fields = ['belief3']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Decision1(Page):
    form_model = 'player'
    form_fields = ['contribution1', 'Cond_contribution_1_0', 'Cond_contribution_1_2', 'Cond_contribution_1_4',
                   'Cond_contribution_1_6', 'Cond_contribution_1_8', 'Cond_contribution_1_10', 'Cond_contribution_1_12',
                   'Cond_contribution_1_14', 'Cond_contribution_1_16', 'Cond_contribution_1_18',
                   'Cond_contribution_1_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Decision1b(Page):
    form_model = 'player'
    form_fields = ['contribution1', 'Cond_contribution_1_0', 'Cond_contribution_1_2', 'Cond_contribution_1_4',
                   'Cond_contribution_1_6', 'Cond_contribution_1_8', 'Cond_contribution_1_10', 'Cond_contribution_1_12',
                   'Cond_contribution_1_14', 'Cond_contribution_1_16', 'Cond_contribution_1_18',
                   'Cond_contribution_1_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 1

    def before_next_page(self):
        self.player.keep_contributions()



class Decision2(Page):
    form_model = 'player'
    form_fields = ['contribution2', 'Cond_contribution_2_0', 'Cond_contribution_2_2', 'Cond_contribution_2_4',
                   'Cond_contribution_2_6', 'Cond_contribution_2_8', 'Cond_contribution_2_10', 'Cond_contribution_2_12',
                   'Cond_contribution_2_14', 'Cond_contribution_2_16', 'Cond_contribution_2_18',
                   'Cond_contribution_2_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Decision2b(Page):
    form_model = 'player'
    form_fields = ['contribution2', 'Cond_contribution_2_0', 'Cond_contribution_2_2', 'Cond_contribution_2_4',
                   'Cond_contribution_2_6', 'Cond_contribution_2_8', 'Cond_contribution_2_10', 'Cond_contribution_2_12',
                   'Cond_contribution_2_14', 'Cond_contribution_2_16', 'Cond_contribution_2_18',
                   'Cond_contribution_2_20']

    def is_displayed(self):
        return self.player.role == 'unprimed'


class Decision3(Page):
    form_model = 'player'
    form_fields = ['contribution3', 'Cond_contribution_3_0', 'Cond_contribution_3_2', 'Cond_contribution_3_4',
                   'Cond_contribution_3_6', 'Cond_contribution_3_8', 'Cond_contribution_3_10', 'Cond_contribution_3_12',
                   'Cond_contribution_3_14', 'Cond_contribution_3_16', 'Cond_contribution_3_18',
                   'Cond_contribution_3_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Decision3b(Page):
    form_model = 'player'
    form_fields = ['contribution3', 'Cond_contribution_3_0', 'Cond_contribution_3_2', 'Cond_contribution_3_4',
                   'Cond_contribution_3_6', 'Cond_contribution_3_8', 'Cond_contribution_3_10', 'Cond_contribution_3_12',
                   'Cond_contribution_3_14', 'Cond_contribution_3_16', 'Cond_contribution_3_18',
                   'Cond_contribution_3_20']

    def is_displayed(self):
        return self.player.role == 'unprimed'


class Decision4(Page):
    form_model = 'player'
    form_fields = ['contribution4', 'Cond_contribution_4_0', 'Cond_contribution_4_2', 'Cond_contribution_4_4',
                   'Cond_contribution_4_6', 'Cond_contribution_4_8', 'Cond_contribution_4_10', 'Cond_contribution_4_12',
                   'Cond_contribution_4_14', 'Cond_contribution_4_16', 'Cond_contribution_4_18',
                   'Cond_contribution_4_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Decision4b(Page):
    form_model = 'player'
    form_fields = ['contribution4', 'Cond_contribution_4_0', 'Cond_contribution_4_2', 'Cond_contribution_4_4',
                   'Cond_contribution_4_6', 'Cond_contribution_4_8', 'Cond_contribution_4_10', 'Cond_contribution_4_12',
                   'Cond_contribution_4_14', 'Cond_contribution_4_16', 'Cond_contribution_4_18',
                   'Cond_contribution_4_20']

    def is_displayed(self):
        return self.player.role == 'unprimed'


class Decision5(Page):
    form_model = 'player'
    form_fields = ['contribution5', 'Cond_contribution_5_0', 'Cond_contribution_5_2', 'Cond_contribution_5_4',
                   'Cond_contribution_5_6', 'Cond_contribution_5_8', 'Cond_contribution_5_10', 'Cond_contribution_5_12',
                   'Cond_contribution_5_14', 'Cond_contribution_5_16', 'Cond_contribution_5_18',
                   'Cond_contribution_5_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Decision5b(Page):
    form_model = 'player'
    form_fields = ['contribution5', 'Cond_contribution_5_0', 'Cond_contribution_5_2', 'Cond_contribution_5_4',
                   'Cond_contribution_5_6', 'Cond_contribution_5_8', 'Cond_contribution_5_10', 'Cond_contribution_5_12',
                   'Cond_contribution_5_14', 'Cond_contribution_5_16', 'Cond_contribution_5_18',
                   'Cond_contribution_5_20']

    def is_displayed(self):
        return self.player.role == 'unprimed'


class Decision6(Page):
    form_model = 'player'
    form_fields = ['contribution6', 'Cond_contribution_6_0', 'Cond_contribution_6_2', 'Cond_contribution_6_4',
                   'Cond_contribution_6_6', 'Cond_contribution_6_8', 'Cond_contribution_6_10', 'Cond_contribution_6_12',
                   'Cond_contribution_6_14', 'Cond_contribution_6_16', 'Cond_contribution_6_18',
                   'Cond_contribution_6_20']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0

    def before_next_page(self):
        self.player.keep_contributions()


class Decision6b(Page):
    form_model = 'player'
    form_fields = ['contribution6', 'Cond_contribution_6_0', 'Cond_contribution_6_2', 'Cond_contribution_6_4',
                   'Cond_contribution_6_6', 'Cond_contribution_6_8', 'Cond_contribution_6_10', 'Cond_contribution_6_12',
                   'Cond_contribution_6_14', 'Cond_contribution_6_16', 'Cond_contribution_6_18',
                   'Cond_contribution_6_20']

    def is_displayed(self):
        return self.player.role == 'unprimed'

class SetGroups1(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_1()


class GenVCMGame1Payoffs(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff_1()


class SetGroups2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_2()


class KeepDecisions(WaitPage):
    pass
    # def after_all_players_arrive(self):
    #     self.group.keep_contributions()


class GenVCMGame2Payoffs(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff_2()


class ReadyForResults(Page):

    def before_next_page(self):
        self.player.set_big_payoff()


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


page_sequence = [
    SetGroups1,
    GenVCMGame1Payoffs,
    SetGroups2,
    Instructions,
    Instructions2,
    Quiz_1,
    Quiz_2,
    InterimPage,
    Belief1,
    Belief2,
    Belief3,
    Decision1,
    Decision1b,
    Decision2,
    Decision3,
    Decision4,
    Decision5,
    Decision6,
    #KeepDecisions,
    GenVCMGame2Payoffs,
    ReadyForResults,
    Results
]
