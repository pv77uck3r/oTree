from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jason Ralston'

doc = """
Variant of trust game
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_trust'
    players_per_group = 2
    num_rounds = 1

    endowment = 10
    multiplier = 3


class Subsession(BaseSubsession):

    def set_groups_1(self):
        self.set_group_matrix(self.session.vars['subjlists'][0])
        for group in self.get_groups():
            players = group.get_players()
            group.set_players(players)

    def set_groups_2(self):
        self.set_group_matrix(self.session.vars['subjlists'][3])
        for group in self.get_groups():
            players = group.get_players()
            group.set_players(players)


class Group(BaseGroup):
    #################INVESTOR DECISIONS#####################
    investor_decision1 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS NEVER ACCUSED of taking a small, "
                                                  "medium, or large amount of money that belonged to another "
                                                  "participant?  Anything you send to them will be tripled by the "
                                                  "experimenter and they can send back to you between 0 and that tripled"
                                                  " number of quarters.")

    investor_decision2 = models.IntegerField(min=0, max=10,
                                             choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                             widget=widgets.RadioSelectHorizontal,
                                             label="How many of your initial 10 quarters will you send to your "
                                                   "counterpart if your counterpart WAS ACCUSED but FOUND NOT-GUILTY of "
                                                   "taking a small, medium, or large amount of money that belonged to "
                                                   "another participant?  Anything you send to them will be tripled by "
                                                   "the experimenter and they can send back to you between 0 and that "
                                                   "tripled number of quarters.")

    investor_decision3 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS FOUND GUILTY of taking a SMALL "
                                                  "amount of money that belonged to another participant?  Anything you "
                                                  "send to them will be tripled by the experimenter and they can send "
                                                  "back to you between 0 and that tripled number of quarters.")

    investor_decision4 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS FOUND GUILTY of taking a MEDIUM "
                                                  "amount of money that belonged to another participant?  Anything you "
                                                  "send to them will be tripled by the experimenter and they can send "
                                                  "back to you between 0 and that tripled number of quarters.")

    investor_decision5 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS FOUND GUILTY of taking a LARGE "
                                                  "amount of money that belonged to another participant?  Anything you "
                                                  "send to them will be tripled by the experimenter and they can send "
                                                  "back to you between 0 and that tripled number of quarters.")

    #################TRUSTEE DECISIONS#######################
    trustee_decision1 = models.IntegerField(min=0, max=3,
                                            label="If your counterpart sends you 1 quarter (tripled into 3 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 3)")

    trustee_decision2 = models.IntegerField(min=0, max=6,
                                            label="If your counterpart sends you 2 quarter (tripled into 6 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 6)")

    trustee_decision3 = models.IntegerField(min=0, max=9,
                                            label="If your counterpart sends you 3 quarter (tripled into 9 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 9)")

    trustee_decision4 = models.IntegerField(min=0, max=12,
                                            label="If your counterpart sends you 4 quarter (tripled into 12 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 12)")

    trustee_decision5 = models.IntegerField(min=0, max=15,
                                            label="If your counterpart sends you 5 quarter (tripled into 15 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 15)")

    trustee_decision6 = models.IntegerField(min=0, max=18,
                                            label="If your counterpart sends you 6 quarter (tripled into 18 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 18)")

    trustee_decision7 = models.IntegerField(min=0, max=21,
                                            label="If your counterpart sends you 7 quarter (tripled into 21 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 21)")

    trustee_decision8 = models.IntegerField(min=0, max=24,
                                            label="If your counterpart sends you 8 quarter (tripled into 24 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 24)")

    trustee_decision9 = models.IntegerField(min=0, max=27,
                                            label="If your counterpart sends you 9 quarter (tripled into 27 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 27)")

    trustee_decision10 = models.IntegerField(min=0, max=30,
                                            label="If your counterpart sends you 10 quarter (tripled into 30 quarters),"
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 30)")

    def set_payoffs_1(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if not (p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3):
            if p1.participant.vars['investor_decision1'] == 0:
                p1.participant.vars['payoffmodule1'] = 10
                p2.participant.vars['payoffmodule1'] = 10
            if p1.participant.vars['investor_decision1'] == 1:
                p1.participant.vars['payoffmodule1'] = 9 + p2.participant.vars['trustee_decision1']
                p2.participant.vars['payoffmodule1'] = 10 + 3*p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision1']
            if p1.participant.vars['investor_decision1'] == 2:
                p1.participant.vars['payoffmodule1'] = 8 + p2.participant.vars['trustee_decision2']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision2']
            if p1.participant.vars['investor_decision1'] == 3:
                p1.participant.vars['payoffmodule1'] = 7 + p2.participant.vars['trustee_decision3']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision3']
            if p1.participant.vars['investor_decision1'] == 4:
                p1.participant.vars['payoffmodule1'] = 6 + p2.participant.vars['trustee_decision4']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision4']
            if p1.participant.vars['investor_decision1'] == 5:
                p1.participant.vars['payoffmodule1'] = 5 + p2.participant.vars['trustee_decision5']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision5']
            if p1.participant.vars['investor_decision1'] == 6:
                p1.participant.vars['payoffmodule1'] = 4 + p2.participant.vars['trustee_decision6']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision6']
            if p1.participant.vars['investor_decision1'] == 7:
                p1.participant.vars['payoffmodule1'] = 3 + p2.participant.vars['trustee_decision7']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision7']
            if p1.participant.vars['investor_decision1'] == 8:
                p1.participant.vars['payoffmodule1'] = 2 + p2.participant.vars['trustee_decision8']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision8']
            if p1.participant.vars['investor_decision1'] == 9:
                p1.participant.vars['payoffmodule1'] = 1 + p2.participant.vars['trustee_decision9']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision9']
            if p1.participant.vars['investor_decision1'] == 10:
                p1.participant.vars['payoffmodule1'] = p2.participant.vars['trustee_decision10']
                p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision1'] - \
                                                       p2.participant.vars['trustee_decision10']
        if p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3:
            if p2.participant.vars['ending_guilt_level'] == 0:
                if p1.participant.vars['investor_decision2'] == 0:
                    p1.participant.vars['payoffmodule1'] = 10
                    p2.participant.vars['payoffmodule1'] = 10
                if p1.participant.vars['investor_decision2'] == 1:
                    p1.participant.vars['payoffmodule1'] = 9 + p2.participant.vars['trustee_decision1']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision1']
                if p1.participant.vars['investor_decision2'] == 2:
                    p1.participant.vars['payoffmodule1'] = 8 + p2.participant.vars['trustee_decision2']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision2']
                if p1.participant.vars['investor_decision2'] == 3:
                    p1.participant.vars['payoffmodule1'] = 7 + p2.participant.vars['trustee_decision3']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision3']
                if p1.participant.vars['investor_decision2'] == 4:
                    p1.participant.vars['payoffmodule1'] = 6 + p2.participant.vars['trustee_decision4']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision4']
                if p1.participant.vars['investor_decision2'] == 5:
                    p1.participant.vars['payoffmodule1'] = 5 + p2.participant.vars['trustee_decision5']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision5']
                if p1.participant.vars['investor_decision2'] == 6:
                    p1.participant.vars['payoffmodule1'] = 4 + p2.participant.vars['trustee_decision6']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision6']
                if p1.participant.vars['investor_decision2'] == 7:
                    p1.participant.vars['payoffmodule1'] = 3 + p2.participant.vars['trustee_decision7']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision7']
                if p1.participant.vars['investor_decision2'] == 8:
                    p1.participant.vars['payoffmodule1'] = 2 + p2.participant.vars['trustee_decision8']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision8']
                if p1.participant.vars['investor_decision2'] == 9:
                    p1.participant.vars['payoffmodule1'] = 1 + p2.participant.vars['trustee_decision9']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision9']
                if p1.participant.vars['investor_decision2'] == 10:
                    p1.participant.vars['payoffmodule1'] = p2.participant.vars['trustee_decision10']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision2'] - \
                                                           p2.participant.vars['trustee_decision10']
            if p2.participant.vars['ending_guilt_level'] == 1:
                if p1.participant.vars['investor_decision3'] == 0:
                    p1.participant.vars['payoffmodule1'] = 10
                    p2.participant.vars['payoffmodule1'] = 10
                if p1.participant.vars['investor_decision3'] == 1:
                    p1.participant.vars['payoffmodule1'] = 9 + p2.participant.vars['trustee_decision1']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision1']
                if p1.participant.vars['investor_decision3'] == 2:
                    p1.participant.vars['payoffmodule1'] = 8 + p2.participant.vars['trustee_decision2']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision2']
                if p1.participant.vars['investor_decision3'] == 3:
                    p1.participant.vars['payoffmodule1'] = 7 + p2.participant.vars['trustee_decision3']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision3']
                if p1.participant.vars['investor_decision3'] == 4:
                    p1.participant.vars['payoffmodule1'] = 6 + p2.participant.vars['trustee_decision4']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision4']
                if p1.participant.vars['investor_decision3'] == 5:
                    p1.participant.vars['payoffmodule1'] = 5 + p2.participant.vars['trustee_decision5']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision5']
                if p1.participant.vars['investor_decision3'] == 6:
                    p1.participant.vars['payoffmodule1'] = 4 + p2.participant.vars['trustee_decision6']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision6']
                if p1.participant.vars['investor_decision3'] == 7:
                    p1.participant.vars['payoffmodule1'] = 3 + p2.participant.vars['trustee_decision7']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision7']
                if p1.participant.vars['investor_decision3'] == 8:
                    p1.participant.vars['payoffmodule1'] = 2 + p2.participant.vars['trustee_decision8']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision8']
                if p1.participant.vars['investor_decision3'] == 9:
                    p1.participant.vars['payoffmodule1'] = 1 + p2.participant.vars['trustee_decision9']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision9']
                if p1.participant.vars['investor_decision3'] == 10:
                    p1.participant.vars['payoffmodule1'] = p2.participant.vars['trustee_decision10']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision3'] - \
                                                           p2.participant.vars['trustee_decision10']
            if p2.participant.vars['ending_guilt_level'] == 2:
                if p1.participant.vars['investor_decision4'] == 0:
                    p1.participant.vars['payoffmodule1'] = 10
                    p2.participant.vars['payoffmodule1'] = 10
                if p1.participant.vars['investor_decision4'] == 1:
                    p1.participant.vars['payoffmodule1'] = 9 + p2.participant.vars['trustee_decision1']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision1']
                if p1.participant.vars['investor_decision4'] == 2:
                    p1.participant.vars['payoffmodule1'] = 8 + p2.participant.vars['trustee_decision2']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision2']
                if p1.participant.vars['investor_decision4'] == 3:
                    p1.participant.vars['payoffmodule1'] = 7 + p2.participant.vars['trustee_decision3']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision3']
                if p1.participant.vars['investor_decision4'] == 4:
                    p1.participant.vars['payoffmodule1'] = 6 + p2.participant.vars['trustee_decision4']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision4']
                if p1.participant.vars['investor_decision4'] == 5:
                    p1.participant.vars['payoffmodule1'] = 5 + p2.participant.vars['trustee_decision5']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision5']
                if p1.participant.vars['investor_decision4'] == 6:
                    p1.participant.vars['payoffmodule1'] = 4 + p2.participant.vars['trustee_decision6']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision6']
                if p1.participant.vars['investor_decision4'] == 7:
                    p1.participant.vars['payoffmodule1'] = 3 + p2.participant.vars['trustee_decision7']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision7']
                if p1.participant.vars['investor_decision4'] == 8:
                    p1.participant.vars['payoffmodule1'] = 2 + p2.participant.vars['trustee_decision8']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision8']
                if p1.participant.vars['investor_decision4'] == 9:
                    p1.participant.vars['payoffmodule1'] = 1 + p2.participant.vars['trustee_decision9']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision9']
                if p1.participant.vars['investor_decision4'] == 10:
                    p1.participant.vars['payoffmodule1'] = p2.participant.vars['trustee_decision10']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision4'] - \
                                                           p2.participant.vars['trustee_decision10']
            if p2.participant.vars['ending_guilt_level'] == 3:
                if p1.participant.vars['investor_decision5'] == 0:
                    p1.participant.vars['payoffmodule1'] = 10
                    p2.participant.vars['payoffmodule1'] = 10
                if p1.participant.vars['investor_decision5'] == 1:
                    p1.participant.vars['payoffmodule1'] = 9 + p2.participant.vars['trustee_decision1']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision1']
                if p1.participant.vars['investor_decision5'] == 2:
                    p1.participant.vars['payoffmodule1'] = 8 + p2.participant.vars['trustee_decision2']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision2']
                if p1.participant.vars['investor_decision5'] == 3:
                    p1.participant.vars['payoffmodule1'] = 7 + p2.participant.vars['trustee_decision3']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision3']
                if p1.participant.vars['investor_decision5'] == 4:
                    p1.participant.vars['payoffmodule1'] = 6 + p2.participant.vars['trustee_decision4']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision4']
                if p1.participant.vars['investor_decision5'] == 5:
                    p1.participant.vars['payoffmodule1'] = 5 + p2.participant.vars['trustee_decision5']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision5']
                if p1.participant.vars['investor_decision5'] == 6:
                    p1.participant.vars['payoffmodule1'] = 4 + p2.participant.vars['trustee_decision6']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision6']
                if p1.participant.vars['investor_decision5'] == 7:
                    p1.participant.vars['payoffmodule1'] = 3 + p2.participant.vars['trustee_decision7']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision7']
                if p1.participant.vars['investor_decision5'] == 8:
                    p1.participant.vars['payoffmodule1'] = 2 + p2.participant.vars['trustee_decision8']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision8']
                if p1.participant.vars['investor_decision5'] == 9:
                    p1.participant.vars['payoffmodule1'] = 1 + p2.participant.vars['trustee_decision9']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision9']
                if p1.participant.vars['investor_decision5'] == 10:
                    p1.participant.vars['payoffmodule1'] = p2.participant.vars['trustee_decision10']
                    p2.participant.vars['payoffmodule1'] = 10 + 3 * p1.participant.vars['investor_decision5'] - \
                                                           p2.participant.vars['trustee_decision10']

    def set_payoffs_2(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if not (p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3):
            if p1.investor_decision1 == 0:
                p1.participant.vars['payoffmodule4'] = 10
                p2.participant.vars['payoffmodule4'] = 10
            if p1.investor_decision1 == 1:
                p1.participant.vars['payoffmodule4'] = 9 + p2.trustee_decision1
                p2.participant.vars['payoffmodule4'] = 10 + 3*p1.investor_decision1 - \
                                                       p2.trustee_decision1
            if p1.investor_decision1 == 2:
                p1.participant.vars['payoffmodule4'] = 8 + p2.trustee_decision2
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision2
            if p1.investor_decision1 == 3:
                p1.participant.vars['payoffmodule4'] = 7 + p2.trustee_decision3
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision3
            if p1.investor_decision1 == 4:
                p1.participant.vars['payoffmodule4'] = 6 + p2.trustee_decision4
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision4
            if p1.investor_decision1 == 5:
                p1.participant.vars['payoffmodule4'] = 5 + p2.trustee_decision5
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision5
            if p1.investor_decision1 == 6:
                p1.participant.vars['payoffmodule4'] = 4 + p2.trustee_decision6
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision6
            if p1.investor_decision1 == 7:
                p1.participant.vars['payoffmodule4'] = 3 + p2.trustee_decision7
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision7
            if p1.investor_decision1 == 8:
                p1.participant.vars['payoffmodule4'] = 2 + p2.trustee_decision8
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision8
            if p1.investor_decision1 == 9:
                p1.participant.vars['payoffmodule4'] = 1 + p2.trustee_decision9
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision9
            if p1.investor_decision1 == 10:
                p1.participant.vars['payoffmodule4'] = p2.trustee_decision10
                p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision1 - \
                                                       p2.trustee_decision10
        if p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3:
            if p2.participant.vars['ending_guilt_level'] == 0:
                if p1.investor_decision2 == 0:
                    p1.participant.vars['payoffmodule4'] = 10
                    p2.participant.vars['payoffmodule4'] = 10
                if p1.investor_decision2 == 1:
                    p1.participant.vars['payoffmodule4'] = 9 + p2.trustee_decision1
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision1
                if p1.investor_decision2 == 2:
                    p1.participant.vars['payoffmodule4'] = 8 + p2.trustee_decision2
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision2
                if p1.investor_decision2 == 3:
                    p1.participant.vars['payoffmodule4'] = 7 + p2.trustee_decision3
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision3
                if p1.investor_decision2 == 4:
                    p1.participant.vars['payoffmodule4'] = 6 + p2.trustee_decision4
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision4
                if p1.investor_decision2 == 5:
                    p1.participant.vars['payoffmodule4'] = 5 + p2.trustee_decision5
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision5
                if p1.investor_decision2 == 6:
                    p1.participant.vars['payoffmodule4'] = 4 + p2.trustee_decision6
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision6
                if p1.investor_decision2 == 7:
                    p1.participant.vars['payoffmodule4'] = 3 + p2.trustee_decision7
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision7
                if p1.investor_decision2 == 8:
                    p1.participant.vars['payoffmodule4'] = 2 + p2.trustee_decision8
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision8
                if p1.investor_decision2 == 9:
                    p1.participant.vars['payoffmodule4'] = 1 + p2.trustee_decision9
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision9
                if p1.investor_decision2 == 10:
                    p1.participant.vars['payoffmodule4'] = p2.trustee_decision10
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision2 - \
                                                           p2.trustee_decision10
            if p2.participant.vars['ending_guilt_level'] == 1:
                if p1.investor_decision3 == 0:
                    p1.participant.vars['payoffmodule4'] = 10
                    p2.participant.vars['payoffmodule4'] = 10
                if p1.investor_decision3 == 1:
                    p1.participant.vars['payoffmodule4'] = 9 + p2.trustee_decision1
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision1
                if p1.investor_decision3 == 2:
                    p1.participant.vars['payoffmodule4'] = 8 + p2.trustee_decision2
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision2
                if p1.investor_decision3 == 3:
                    p1.participant.vars['payoffmodule4'] = 7 + p2.trustee_decision3
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision3
                if p1.investor_decision3 == 4:
                    p1.participant.vars['payoffmodule4'] = 6 + p2.trustee_decision4
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision4
                if p1.investor_decision3 == 5:
                    p1.participant.vars['payoffmodule4'] = 5 + p2.trustee_decision5
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision5
                if p1.investor_decision3 == 6:
                    p1.participant.vars['payoffmodule4'] = 4 + p2.trustee_decision6
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision6
                if p1.investor_decision3 == 7:
                    p1.participant.vars['payoffmodule4'] = 3 + p2.trustee_decision7
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision7
                if p1.investor_decision3 == 8:
                    p1.participant.vars['payoffmodule4'] = 2 + p2.trustee_decision8
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision8
                if p1.investor_decision3 == 9:
                    p1.participant.vars['payoffmodule4'] = 1 + p2.trustee_decision9
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision9
                if p1.investor_decision3 == 10:
                    p1.participant.vars['payoffmodule4'] = p2.trustee_decision10
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision3 - \
                                                           p2.trustee_decision10
            if p2.participant.vars['ending_guilt_level'] == 2:
                if p1.investor_decision4 == 0:
                    p1.participant.vars['payoffmodule4'] = 10
                    p2.participant.vars['payoffmodule4'] = 10
                if p1.investor_decision4 == 1:
                    p1.participant.vars['payoffmodule4'] = 9 + p2.trustee_decision1
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision1
                if p1.investor_decision4 == 2:
                    p1.participant.vars['payoffmodule4'] = 8 + p2.trustee_decision2
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision2
                if p1.investor_decision4 == 3:
                    p1.participant.vars['payoffmodule4'] = 7 + p2.trustee_decision3
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision3
                if p1.investor_decision4 == 4:
                    p1.participant.vars['payoffmodule4'] = 6 + p2.trustee_decision4
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision4
                if p1.investor_decision4 == 5:
                    p1.participant.vars['payoffmodule4'] = 5 + p2.trustee_decision5
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision5
                if p1.investor_decision4 == 6:
                    p1.participant.vars['payoffmodule4'] = 4 + p2.trustee_decision6
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision6
                if p1.investor_decision4 == 7:
                    p1.participant.vars['payoffmodule4'] = 3 + p2.trustee_decision7
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision7
                if p1.investor_decision4 == 8:
                    p1.participant.vars['payoffmodule4'] = 2 + p2.trustee_decision8
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision8
                if p1.investor_decision4 == 9:
                    p1.participant.vars['payoffmodule4'] = 1 + p2.trustee_decision9
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision9
                if p1.investor_decision4 == 10:
                    p1.participant.vars['payoffmodule4'] = p2.trustee_decision10
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision4 - \
                                                           p2.trustee_decision10
            if p2.participant.vars['ending_guilt_level'] == 3:
                if p1.investor_decision5 == 0:
                    p1.participant.vars['payoffmodule4'] = 10
                    p2.participant.vars['payoffmodule4'] = 10
                if p1.investor_decision5 == 1:
                    p1.participant.vars['payoffmodule4'] = 9 + p2.trustee_decision1
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision1
                if p1.investor_decision5 == 2:
                    p1.participant.vars['payoffmodule4'] = 8 + p2.trustee_decision2
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision2
                if p1.investor_decision5 == 3:
                    p1.participant.vars['payoffmodule4'] = 7 + p2.trustee_decision3
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision3
                if p1.investor_decision5 == 4:
                    p1.participant.vars['payoffmodule4'] = 6 + p2.trustee_decision4
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision4
                if p1.investor_decision5 == 5:
                    p1.participant.vars['payoffmodule4'] = 5 + p2.trustee_decision5
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision5
                if p1.investor_decision5 == 6:
                    p1.participant.vars['payoffmodule4'] = 4 + p2.trustee_decision6
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision6
                if p1.investor_decision5 == 7:
                    p1.participant.vars['payoffmodule4'] = 3 + p2.trustee_decision7
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision7
                if p1.investor_decision5 == 8:
                    p1.participant.vars['payoffmodule4'] = 2 + p2.trustee_decision8
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision8
                if p1.investor_decision5 == 9:
                    p1.participant.vars['payoffmodule4'] = 1 + p2.trustee_decision9
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision9
                if p1.investor_decision5 == 10:
                    p1.participant.vars['payoffmodule4'] = p2.trustee_decision10
                    p2.participant.vars['payoffmodule4'] = 10 + 3 * p1.investor_decision5 - \
                                                           p2.trustee_decision10
        p1.set_big_payoff()
        p2.set_big_payoff()


class Player(BasePlayer):

    investor_quiz1 = models.IntegerField(
        choices=[
            [1, '(a) You each start with 5.'],
            [2, '(b) You start with 10 and your counterpart starts with 0.'],
            [3, '(c) Your counterpart starts with 10 and you start with 0.'],
            [4, '(d) You each start with 10.']
        ],
        widget=widgets.RadioSelect,
        label="How many quarters do you and your counterpart start with in this part of the experiment?"
    )

    investor_quiz2 = models.IntegerField(
        choices=[
            [1, '(a) It will triple to 12 quarters before reaching them.'],
            [2, '(b) It will double to 8 quarters before reaching them.'],
            [3, '(c) They will receive 4 quarters.'],
        ],
        widget=widgets.RadioSelect,
        label="If you send your counterpart 4 quarters "
    )

    investor_quiz3 = models.IntegerField(
        choices=[
            [1, '(a) Will be tripled before reaching you.'],
            [2, '(b) Will be doubled before reaching you.'],
            [3, '(c) Will not be multiplied before reaching you.'],
        ],
        widget=widgets.RadioSelect,
        label="Any quarters your counterpart returns to you "
    )

    investor_quiz4 = models.IntegerField(
        choices=[
            [1, '(a) All participants you could interact with in this part of the experiment are guaranteed to have '
                'taken money from others previously.'],
            [2, '(b) Some participants who were truly innocent may have been found guilty of taking money from another '
                'subject.'],
            [3, '(c) Participants who were found guilty of taking money from another participant faced no monetary '
                'penalty from their guilty finding.'],
        ],
        widget=widgets.RadioSelect,
        label="Which of the following is true "
    )

    trustee_quiz1 = models.IntegerField(
        choices=[
            [1, '(a) You each start with 5.'],
            [2, '(b) You start with 10 and your counterpart starts with 0.'],
            [3, '(c) Your counterpart starts with 10 and you start with 0.'],
            [4, '(d) You each start with 10.']
        ],
        widget=widgets.RadioSelect,
        label="How many quarters do you and your counterpart start with? "
    )

    trustee_quiz2 = models.IntegerField(
        choices=[
            [1, '(a) It will triple to 12 quarters before reaching you.'],
            [2, '(b) It will double to 8 quarters before reaching you.'],
            [3, '(c) You will receive 4 quarters.']
        ],
        widget=widgets.RadioSelect,
        label="If your counterpart sends you 4 quarters "
    )

    trustee_quiz3 = models.IntegerField(
        choices=[
            [1, '(a) Will be tripled before reaching them.'],
            [2, '(b) Will be doubled before reaching them.'],
            [3, '(c) Will not be multiplied before reaching them.']
        ],
        widget=widgets.RadioSelect,
        label="Any quarters you return to your counterpart "
    )

    def role(self):
        if self.id_in_group == 1:
            return 'Investor'
        if self.id_in_group == 2:
            return 'Trustee'

    def set_big_payoff(self):
        self.participant.vars['bigpayoff'] = self.participant.vars['payoffmodule1'] + self.participant.vars['payoffmodule2'] + self.participant.vars['payoffmodule3'] + self.participant.vars['payoffmodule4']
