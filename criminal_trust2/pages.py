from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class QuizI(Page):
    form_model = 'player'
    form_fields = ['investor_quiz1', 'investor_quiz2', 'investor_quiz3', 'investor_quiz4']

    def is_displayed(self):
        return self.player.id_in_group == 1


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


class QuizT(Page):
    form_model = 'player'
    form_fields = ['trustee_quiz1', 'trustee_quiz2', 'trustee_quiz3']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def trustee_quiz1_error_message(self, value):
        if value != 4:
            return 'Question 1 is incorrect. Please try again.'

    def trustee_quiz2_error_message(self, value):
        if value != 1:
            return 'Question 2 is incorrect. Please try again.'

    def trustee_quiz3_error_message(self, value):
        if value != 3:
            return 'Question 3 is incorrect. Please try again.'


class DecisionsI(Page):
    form_model = 'group'
    form_fields = ['investor_decision1', 'investor_decision2', 'investor_decision3', 'investor_decision4',
                   'investor_decision5']

    def is_displayed(self):
        return self.player.id_in_group == 1

class DecisionsI1(Page):
    form_model = 'group'
    form_fields = ['investor_decision1']

    def is_displayed(self):
        return self.player.id_in_group == 1


class DecisionsI2(Page):
    form_model = 'group'
    form_fields = ['investor_decision2']

    def is_displayed(self):
        return self.player.id_in_group == 1


class DecisionsI3(Page):
    form_model = 'group'
    form_fields = ['investor_decision3']

    def is_displayed(self):
        return self.player.id_in_group == 1


class DecisionsI4(Page):
    form_model = 'group'
    form_fields = ['investor_decision4']

    def is_displayed(self):
        return self.player.id_in_group == 1


class DecisionsI5(Page):
    form_model = 'group'
    form_fields = ['investor_decision5']

    def is_displayed(self):
        return self.player.id_in_group == 1

class DecisionsT(Page):
    form_model = 'group'
    form_fields = ['trustee_decision1', 'trustee_decision2', 'trustee_decision3', 'trustee_decision4',
                   'trustee_decision5', 'trustee_decision6', 'trustee_decision7', 'trustee_decision8',
                   'trustee_decision9', 'trustee_decision10']

    def is_displayed(self):
        return self.player.id_in_group == 2


class RecordDecisions(WaitPage):
    def after_all_players_arrive(self):
        self.group.keep_decisions()


class SetGroups1(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_1()


class GenTrustGame1Payoffs(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs_1()


class SetGroups2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_2()


class KeepDecisions(WaitPage):
    def after_all_players_arrive(self):
        self.group.keep_decisions()


class GenTrustGame2Payoffs(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_2()


# class Results(Page):
#
#     def vars_for_template(self):
#         return {'payoff1': format(self.participant.vars['payoffmodule1']*0.25, '.2f'),
#                 'payoff2': format(self.participant.vars['payoffmodule2'], '.2f'),
#                 'payoff3': format(self.participant.vars['payoffmodule3'], '.2f'),
#                 'payoff4': format(self.participant.vars['payoffmodule4']*0.25, '.2f'),
#                 'finalpayoff': format(self.participant.vars['bigpayoff'], '.2f')
#                 }


page_sequence = [
    SetGroups1,
    GenTrustGame1Payoffs,
    SetGroups2,
    Instructions,
    DecisionsI1,
    DecisionsI2,
    DecisionsI3,
    DecisionsI4,
    DecisionsI5,
    DecisionsT,
    KeepDecisions,
    GenTrustGame2Payoffs,
    Results
]
