from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_VCM2_ALT_ORDER')
        }

    def before_next_page(self):
        self.player.record_number()


class Instructions2(Page):

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_VCM2_ALT_ORDER')
        }


class Quiz_1(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 0


class Quiz_2(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3']

    def is_displayed(self):
        return self.participant.id_in_session % 2 == 1


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
    def after_all_players_arrive(self):
        self.group.keep_contributions()


class GenVCMGame2Payoffs(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff_2()


page_sequence = [
    SetGroups2,
    Instructions,
    Instructions2,
    Quiz_1,
    Quiz_2,
    Belief1,
    Belief2,
    Belief3,
    Decision1,
    Decision2,
    Decision3,
    Decision4,
    Decision5,
    Decision6,
    KeepDecisions,
]
