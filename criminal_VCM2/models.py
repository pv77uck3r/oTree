from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""

def shift_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst

class Constants(BaseConstants):
    name_in_url = 'criminal_VCM2'
    players_per_group = 3
    num_rounds = 1

    multiplier = 0.5
    endowment = 10

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

    totalcontribution1 = models.IntegerField()

    totalcontribution2 = models.IntegerField()

    totalcontribution3 = models.IntegerField()

    totalcontribution4 = models.IntegerField()

    totalcontribution5 = models.IntegerField()

    totalcontribution6 = models.IntegerField()

    individualshare1 = models.FloatField()

    individualshare2 = models.FloatField()

    individualshare3 = models.FloatField()

    individualshare4 = models.FloatField()

    individualshare5 = models.FloatField()

    individualshare6 = models.FloatField()

    # def sum_and_store(self):
    #     players = self.get_players()
    #
    #     ## We use the same local variable (contributions) to sum for each condition and calculate individual shares ##
    #
    #     contributions = [p.contribution1 for p in players]
    #     self.total_contribution1 = sum(contributions)
    #     self.individual_share1 = self.total_contribution1 * Constants.multiplier / Constants.players_per_group
    #     for p in players:
    #         p.participant.vars['VCMPayoff21'] = Constants.endowment - p.contribution1 + self.individual_share1
    #
    #     contributions = [p.contribution2 for p in players]
    #     self.total_contribution2 = sum(contributions)
    #     self.individual_share2 = self.total_contribution2 * Constants.multiplier / Constants.players_per_group
    #     for p in players:
    #         p.participant.vars['VCMPayoff22'] = Constants.endowment - p.contribution2 + self.individual_share2
    #
    #     contributions = [p.contribution3 for p in players]
    #     self.total_contribution3 = sum(contributions)
    #     self.individual_share3 = self.total_contribution3 * Constants.multiplier / Constants.players_per_group
    #     for p in players:
    #         p.participant.vars['VCMPayoff23'] = Constants.endowment - p.contribution3 + self.individual_share3
    #
    #     contributions = [p.contribution4 for p in players]
    #     self.total_contribution4 = sum(contributions)
    #     self.individual_share4 = self.total_contribution4 * Constants.multiplier / Constants.players_per_group
    #     for p in players:
    #         p.participant.vars['VCMPayoff24'] = Constants.endowment - p.contribution4 + self.individual_share4
    #
    #     contributions = [p.contribution5 for p in players]
    #     self.total_contribution5 = sum(contributions)
    #     self.individual_share5 = self.total_contribution5 * Constants.multiplier / Constants.players_per_group
    #     for p in players:
    #         p.participant.vars['VCMPayoff25'] = Constants.endowment - p.contribution5 + self.individual_share5
    #
    #     contributions = [p.contribution6 for p in players]
    #     self.total_contribution6 = sum(contributions)
    #     self.individual_share6 = self.total_contribution6 * Constants.multiplier / Constants.players_per_group
    #     for p in players:
    #         p.participant.vars['VCMPayoff26'] = Constants.endowment - p.contribution6 + self.individual_share6


    def set_payoff_1(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)


        ## First, Player1 finds their contribution
        ## First, Innocent/Innocent
        if p1.participant.id_in_session % 2 == 1:
            if p2.participant.vars['ending_trial_status'] == False and p3.participant.vars['ending_trial_status'] == False:
                contribution1 = p1.participant.vars['contribution1']
            else:
                ## Next, Innocent/Acquitted
                if ((p2.participant.vars['ending_trial_status'] == True and p2.participant.vars['ending_guilt'] == False)
                    and (p3.participant.vars['ending_trial_status'] == False)) or ((p3.participant.vars['ending_trial_status'] == True and p3.participant.vars['ending_guilt'] == False)
                    and (p2.participant.vars['ending_trial_status'] == False)):
                    contribution1 = p1.participant.vars['contribution2']
                else:
                    ## Next, Innocent/Guilty
                    if (p2.participant.vars['ending_trial_status'] == False and p3.participant.vars['ending_guilt'] == True) or (p2.participant.vars['ending_guilt'] == True or p3.participant.vars['ending_trial_status'] == False):
                        contribution1 = p1.participant.vars['contribution3']
                    else:
                        ##Next, Acquitted/Acquitted
                        if (p2.participant.vars['ending_trial_status'] == True and p2.participant.vars['ending_guilt'] == False) and (p3.participant.vars['ending_trial_status'] == True and p3.participant.vars['ending_guilt'] == False):
                            contribution1 = p1.participant.vars['contribution4']
                        else:
                            ## Next, Guilty/Guilty
                            if (p2.participant.vars['ending_guilt'] == True and p3.participant.vars['ending_guilt'] == True):
                                contribution1 = p1.participant.vars['contribution6']
                            ## Last, Acquitted/Guilty
                            else:
                                contribution1 = p1.participant.vars['contribution5']
        else:
            contribution1 = p1.participant.vars['contribution1']

        ## Next, Player3 finds their contribution
        if p3.participant.id_in_session % 2 == 1:
            if p1.participant.vars['ending_trial_status'] == False and p2.participant.vars['ending_trial_status'] == False:
                contribution3 = p3.participant.vars['contribution1']
            else:
                ## Next, Innocent/Acquitted
                if ((p1.participant.vars['ending_trial_status'] == True and p1.participant.vars['ending_guilt'] == False)
                    and (p2.participant.vars['ending_trial_status'] == False)) or ((p2.participant.vars[
                                                                                        'ending_trial_status'] == True and
                                                                                    p2.participant.vars[
                                                                                        'ending_guilt'] == False)
                                                                                   and (p1.participant.vars[
                                                                                            'ending_trial_status'] == False)):
                    contribution3 = p3.participant.vars['contribution2']
                else:
                    ## Next, Innocent/Guilty
                    if (p1.participant.vars['ending_trial_status'] == False and p2.participant.vars['ending_guilt'] == True) \
                            or (p1.participant.vars['ending_guilt'] == True or p2.participant.vars[
                        'ending_trial_status'] == False):
                        contribution3 = p3.participant.vars['contribution3']
                    else:
                        ##Next, Acquitted/Acquitted
                        if (p1.participant.vars['ending_trial_status'] == True and p1.participant.vars[
                            'ending_guilt'] == False) and \
                                (p2.participant.vars['ending_trial_status'] == True and p2.participant.vars[
                                    'ending_guilt'] == False):
                            contribution3 = p3.participant.vars['contribution4']
                        else:
                            ## Next, Guilty/Guilty
                            if (p1.participant.vars['ending_guilt'] == True and p2.participant.vars[
                                'ending_guilt'] == True):
                                contribution3 = p1.participant.vars['contribution6']
                            ## Last, Acquitted/Guilty
                            else:
                                contribution3 = p3.participant.vars['contribution5']
        else:
            contribution3 = p3.participant.vars['contribution1']

        ## Next, Player2 finds their contribution
        ## NOTE: Player2 has their conditional decision used

        unconditionalcontributions = round((contribution1 + contribution3)/2)

        if p2.participant.id_in_session % 2 == 1:
            if p1.participant.vars['ending_trial_status'] == False and p3.participant.vars[
                'ending_trial_status'] == False:
                if unconditionalcontributions == 0:
                    contribution2 = p2.participant.vars['Cond_contribution_1_0']
                else:
                    if unconditionalcontributions == 1:
                        contribution2 = p2.participant.vars['Cond_contribution_1_2']
                    else:
                        if unconditionalcontributions == 2:
                            contribution2 = p2.participant.vars['Cond_contribution_1_4']
                        else:
                            if unconditionalcontributions == 3:
                                contribution2 = p2.participant.vars['Cond_contribution_1_6']
                            else:
                                if unconditionalcontributions == 4:
                                    contribution2 = p2.participant.vars['Cond_contribution_1_8']
                                else:
                                    if unconditionalcontributions == 5:
                                        contribution2 = p2.participant.vars['Cond_contribution_1_10']
                                    else:
                                        if unconditionalcontributions == 6:
                                            contribution2 = p2.participant.vars['Cond_contribution_1_12']
                                        else:
                                            if unconditionalcontributions == 7:
                                                contribution2 = p2.participant.vars['Cond_contribution_1_14']
                                            else:
                                                if unconditionalcontributions == 8:
                                                    contribution2 = p2.participant.vars['Cond_contribution_1_16']
                                                else:
                                                    if unconditionalcontributions == 9:
                                                        contribution2 = p2.participant.vars['Cond_contribution_1_18']
                                                    else:
                                                        contribution2 = p2.participant.vars['Cond_contribution_1_20']
            else:
                ## Next, Innocent/Acquitted
                if ((p1.participant.vars['ending_trial_status'] == True and p1.participant.vars[
                    'ending_guilt'] == False)
                    and (p3.participant.vars['ending_trial_status'] == False)) or ((p3.participant.vars[
                                                                                        'ending_trial_status'] == True and
                                                                                    p3.participant.vars[
                                                                                        'ending_guilt'] == False)
                                                                                   and (p1.participant.vars[
                                                                                            'ending_trial_status'] == False)):
                    if unconditionalcontributions == 0:
                        contribution2 = p2.participant.vars['Cond_contribution_2_0']
                    else:
                        if unconditionalcontributions == 1:
                            contribution2 = p2.participant.vars['Cond_contribution_2_2']
                        else:
                            if unconditionalcontributions == 2:
                                contribution2 = p2.participant.vars['Cond_contribution_2_4']
                            else:
                                if unconditionalcontributions == 3:
                                    contribution2 = p2.participant.vars['Cond_contribution_2_6']
                                else:
                                    if unconditionalcontributions == 4:
                                        contribution2 = p2.participant.vars['Cond_contribution_2_8']
                                    else:
                                        if unconditionalcontributions == 5:
                                            contribution2 = p2.participant.vars['Cond_contribution_2_10']
                                        else:
                                            if unconditionalcontributions == 6:
                                                contribution2 = p2.participant.vars['Cond_contribution_2_12']
                                            else:
                                                if unconditionalcontributions == 7:
                                                    contribution2 = p2.participant.vars['Cond_contribution_2_14']
                                                else:
                                                    if unconditionalcontributions == 8:
                                                        contribution2 = p2.participant.vars['Cond_contribution_2_16']
                                                    else:
                                                        if unconditionalcontributions == 9:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_2_18']
                                                        else:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_2_20']
                else:
                    ## Next, Innocent/Guilty
                    if (p1.participant.vars['ending_trial_status'] == False and p3.participant.vars[
                        'ending_guilt'] == True) \
                            or (p1.participant.vars['ending_guilt'] == True or p3.participant.vars[
                        'ending_trial_status'] == False):
                        if unconditionalcontributions == 0:
                            contribution2 = p2.participant.vars['Cond_contribution_3_0']
                        else:
                            if unconditionalcontributions == 1:
                                contribution2 = p2.participant.vars['Cond_contribution_3_2']
                            else:
                                if unconditionalcontributions == 2:
                                    contribution2 = p2.participant.vars['Cond_contribution_3_4']
                                else:
                                    if unconditionalcontributions == 3:
                                        contribution2 = p2.participant.vars['Cond_contribution_3_6']
                                    else:
                                        if unconditionalcontributions == 4:
                                            contribution2 = p2.participant.vars['Cond_contribution_3_8']
                                        else:
                                            if unconditionalcontributions == 5:
                                                contribution2 = p2.participant.vars['Cond_contribution_3_10']
                                            else:
                                                if unconditionalcontributions == 6:
                                                    contribution2 = p2.participant.vars['Cond_contribution_3_12']
                                                else:
                                                    if unconditionalcontributions == 7:
                                                        contribution2 = p2.participant.vars['Cond_contribution_3_14']
                                                    else:
                                                        if unconditionalcontributions == 8:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_3_16']
                                                        else:
                                                            if unconditionalcontributions == 9:
                                                                contribution2 = p2.participant.vars[
                                                                    'Cond_contribution_3_18']
                                                            else:
                                                                contribution2 = p2.participant.vars[
                                                                    'Cond_contribution_3_20']
                    else:
                        ##Next, Acquitted/Acquitted
                        if (p1.participant.vars['ending_trial_status'] == True and p1.participant.vars[
                            'ending_guilt'] == False) and \
                                (p3.participant.vars['ending_trial_status'] == True and p3.participant.vars[
                                    'ending_guilt'] == False):
                            if unconditionalcontributions == 0:
                                contribution2 = p2.participant.vars['Cond_contribution_4_0']
                            else:
                                if unconditionalcontributions == 1:
                                    contribution2 = p2.participant.vars['Cond_contribution_4_2']
                                else:
                                    if unconditionalcontributions == 2:
                                        contribution2 = p2.participant.vars['Cond_contribution_4_4']
                                    else:
                                        if unconditionalcontributions == 3:
                                            contribution2 = p2.participant.vars['Cond_contribution_4_6']
                                        else:
                                            if unconditionalcontributions == 4:
                                                contribution2 = p2.participant.vars['Cond_contribution_4_8']
                                            else:
                                                if unconditionalcontributions == 5:
                                                    contribution2 = p2.participant.vars['Cond_contribution_4_10']
                                                else:
                                                    if unconditionalcontributions == 6:
                                                        contribution2 = p2.participant.vars['Cond_contribution_4_12']
                                                    else:
                                                        if unconditionalcontributions == 7:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_4_14']
                                                        else:
                                                            if unconditionalcontributions == 8:
                                                                contribution2 = p2.participant.vars[
                                                                    'Cond_contribution_4_16']
                                                            else:
                                                                if unconditionalcontributions == 9:
                                                                    contribution2 = p2.participant.vars[
                                                                        'Cond_contribution_4_18']
                                                                else:
                                                                    contribution2 = p2.participant.vars[
                                                                        'Cond_contribution_4_20']
                        else:
                            ## Next, Guilty/Guilty
                            if (p1.participant.vars['ending_guilt'] == True and p3.participant.vars[
                                'ending_guilt'] == True):
                                if unconditionalcontributions == 0:
                                    contribution2 = p2.participant.vars['Cond_contribution_6_0']
                                else:
                                    if unconditionalcontributions == 1:
                                        contribution2 = p2.participant.vars['Cond_contribution_6_2']
                                    else:
                                        if unconditionalcontributions == 2:
                                            contribution2 = p2.participant.vars['Cond_contribution_6_4']
                                        else:
                                            if unconditionalcontributions == 3:
                                                contribution2 = p2.participant.vars['Cond_contribution_6_6']
                                            else:
                                                if unconditionalcontributions == 4:
                                                    contribution2 = p2.participant.vars['Cond_contribution_6_8']
                                                else:
                                                    if unconditionalcontributions == 5:
                                                        contribution2 = p2.participant.vars['Cond_contribution_6_10']
                                                    else:
                                                        if unconditionalcontributions == 6:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_6_12']
                                                        else:
                                                            if unconditionalcontributions == 7:
                                                                contribution2 = p2.participant.vars[
                                                                    'Cond_contribution_6_14']
                                                            else:
                                                                if unconditionalcontributions == 8:
                                                                    contribution2 = p2.participant.vars[
                                                                        'Cond_contribution_6_16']
                                                                else:
                                                                    if unconditionalcontributions == 9:
                                                                        contribution2 = p2.participant.vars[
                                                                            'Cond_contribution_6_18']
                                                                    else:
                                                                        contribution2 = p2.participant.vars[
                                                                            'Cond_contribution_6_20']
                            ## Last, Acquitted/Guilty
                            else:
                                if unconditionalcontributions == 0:
                                    contribution2 = p2.participant.vars['Cond_contribution_6_0']
                                else:
                                    if unconditionalcontributions == 1:
                                        contribution2 = p2.participant.vars['Cond_contribution_6_2']
                                    else:
                                        if unconditionalcontributions == 2:
                                            contribution2 = p2.participant.vars['Cond_contribution_6_4']
                                        else:
                                            if unconditionalcontributions == 3:
                                                contribution2 = p2.participant.vars['Cond_contribution_6_6']
                                            else:
                                                if unconditionalcontributions == 4:
                                                    contribution2 = p2.participant.vars['Cond_contribution_6_8']
                                                else:
                                                    if unconditionalcontributions == 5:
                                                        contribution2 = p2.participant.vars['Cond_contribution_6_10']
                                                    else:
                                                        if unconditionalcontributions == 6:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_6_12']
                                                        else:
                                                            if unconditionalcontributions == 7:
                                                                contribution2 = p2.participant.vars[
                                                                    'Cond_contribution_6_14']
                                                            else:
                                                                if unconditionalcontributions == 8:
                                                                    contribution2 = p2.participant.vars[
                                                                        'Cond_contribution_6_16']
                                                                else:
                                                                    if unconditionalcontributions == 9:
                                                                        contribution2 = p2.participant.vars[
                                                                            'Cond_contribution_6_18']
                                                                    else:
                                                                        contribution2 = p2.participant.vars[
                                                                            'Cond_contribution_6_20']
        else:
            if unconditionalcontributions == 0:
                contribution2 = p2.participant.vars['Cond_contribution_1_0']
            else:
                if unconditionalcontributions == 1:
                    contribution2 = p2.participant.vars['Cond_contribution_1_2']
                else:
                    if unconditionalcontributions == 2:
                        contribution2 = p2.participant.vars['Cond_contribution_1_4']
                    else:
                        if unconditionalcontributions == 3:
                            contribution2 = p2.participant.vars['Cond_contribution_1_6']
                        else:
                            if unconditionalcontributions == 4:
                                contribution2 = p2.participant.vars['Cond_contribution_1_8']
                            else:
                                if unconditionalcontributions == 5:
                                    contribution2 = p2.participant.vars['Cond_contribution_1_10']
                                else:
                                    if unconditionalcontributions == 6:
                                        contribution2 = p2.participant.vars['Cond_contribution_1_12']
                                    else:
                                        if unconditionalcontributions == 7:
                                            contribution2 = p2.participant.vars['Cond_contribution_1_14']
                                        else:
                                            if unconditionalcontributions == 8:
                                                contribution2 = p2.participant.vars['Cond_contribution_1_16']
                                            else:
                                                if unconditionalcontributions == 9:
                                                    contribution2 = p2.participant.vars['Cond_contribution_1_18']
                                                else:
                                                    contribution2 = p2.participant.vars['Cond_contribution_1_20']

        groupaccount = contribution1 + contribution2 + contribution3
        groupaccountreturn = Constants.multiplier * groupaccount
        payoff1 = (Constants.endowment - contribution1) + groupaccountreturn
        payoff2 = (Constants.endowment - contribution2) + groupaccountreturn
        payoff3 = (Constants.endowment - contribution3) + groupaccountreturn
        p1.participant.vars['payoffmodule1'] = payoff1
        p2.participant.vars['payoffmodule1'] = payoff2
        p3.participant.vars['payoffmodule1'] = payoff3

    def set_payoff_2(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)

        ## First, Player1 finds their contribution
        ## First, Innocent/Innocent
        if self.session.vars['new_group_matrix'][p1.participant.id_in_session] % 2 == 0:
            if p2.participant.vars['ending_trial_status'] == False and p3.participant.vars['ending_trial_status'] == False:
                contribution1 = p1.contribution1
            else:
                ## Next, Innocent/Acquitted
                if ((p2.participant.vars['ending_trial_status'] == True and p2.participant.vars['ending_guilt'] == False)
                    and (p3.participant.vars['ending_trial_status'] == False)) or ((p3.participant.vars[
                                                                                        'ending_trial_status'] == True and
                                                                                    p3.participant.vars[
                                                                                        'ending_guilt'] == False)
                                                                                   and (p2.participant.vars[
                                                                                            'ending_trial_status'] == False)):
                    contribution1 = p1.contribution2
                else:
                    ## Next, Innocent/Guilty
                    if (p2.participant.vars['ending_trial_status'] == False and p3.participant.vars['ending_guilt'] == True) \
                            or (p2.participant.vars['ending_guilt'] == True or p3.participant.vars[
                        'ending_trial_status'] == False):
                        contribution1 = p1.contribution3
                    else:
                        ##Next, Acquitted/Acquitted
                        if (p2.participant.vars['ending_trial_status'] == True and p2.participant.vars[
                            'ending_guilt'] == False) and \
                                (p3.participant.vars['ending_trial_status'] == True and p3.participant.vars[
                                    'ending_guilt'] == False):
                            contribution1 = p1.contribution4
                        else:
                            ## Next, Guilty/Guilty
                            if (p2.participant.vars['ending_guilt'] == True and p3.participant.vars[
                                'ending_guilt'] == True):
                                contribution1 = p1.contribution6
                            ## Last, Acquitted/Guilty
                            else:
                                contribution1 = p1.contribution5
        else:
            contribution1 = p1.contribution1


        ## Next, Player3 finds their contribution
        if self.session.vars['new_group_matrix'][p1.participant.id_in_session] % 2 == 0:
            if p1.participant.vars['ending_trial_status'] == False and p2.participant.vars['ending_trial_status'] == False:
                contribution3 = p3.contribution1
            else:
                ## Next, Innocent/Acquitted
                if ((p1.participant.vars['ending_trial_status'] == True and p1.participant.vars['ending_guilt'] == False)
                    and (p2.participant.vars['ending_trial_status'] == False)) or ((p2.participant.vars[
                                                                                        'ending_trial_status'] == True and
                                                                                    p2.participant.vars[
                                                                                        'ending_guilt'] == False)
                                                                                   and (p1.participant.vars[
                                                                                            'ending_trial_status'] == False)):
                    contribution3 = p3.contribution2
                else:
                    ## Next, Innocent/Guilty
                    if (p1.participant.vars['ending_trial_status'] == False and p2.participant.vars['ending_guilt'] == True) \
                            or (p1.participant.vars['ending_guilt'] == True or p2.participant.vars[
                        'ending_trial_status'] == False):
                        contribution3 = p3.contribution3
                    else:
                        ##Next, Acquitted/Acquitted
                        if (p1.participant.vars['ending_trial_status'] == True and p1.participant.vars[
                            'ending_guilt'] == False) and \
                                (p2.participant.vars['ending_trial_status'] == True and p2.participant.vars[
                                    'ending_guilt'] == False):
                            contribution3 = p3.contribution4
                        else:
                            ## Next, Guilty/Guilty
                            if (p1.participant.vars['ending_guilt'] == True and p2.participant.vars[
                                'ending_guilt'] == True):
                                contribution3 = p3.contribution6
                            ## Last, Acquitted/Guilty
                            else:
                                contribution3 = p3.contribution5
        else:
            contribution3 = p3.contribution1

        unconditionalcontributions = round((contribution1 + contribution3)/2)

        ## Next, Player2 finds their contribution
        ## NOTE: Player2 has their conditional decision used

        if self.session.vars['new_group_matrix'][p1.participant.id_in_session] % 2 == 0:
            if p1.participant.vars['ending_trial_status'] == False and p3.participant.vars[
                'ending_trial_status'] == False:
                if unconditionalcontributions == 0:
                    contribution2 = p2.Cond_contribution_1_0
                else:
                    if unconditionalcontributions == 1:
                        contribution2 = p2.Cond_contribution_1_2
                    else:
                        if unconditionalcontributions == 2:
                            contribution2 = p2.Cond_contribution_1_4
                        else:
                            if unconditionalcontributions == 3:
                                contribution2 = p2.Cond_contribution_1_6
                            else:
                                if unconditionalcontributions == 4:
                                    contribution2 = p2.Cond_contribution_1_8
                                else:
                                    if unconditionalcontributions == 5:
                                        contribution2 = p2.Cond_contribution_1_10
                                    else:
                                        if unconditionalcontributions == 6:
                                            contribution2 = p2.Cond_contribution_1_12
                                        else:
                                            if unconditionalcontributions == 7:
                                                contribution2 = p2.Cond_contribution_1_14
                                            else:
                                                if unconditionalcontributions == 8:
                                                    contribution2 = p2.Cond_contribution_1_16
                                                else:
                                                    if unconditionalcontributions == 9:
                                                        contribution2 = p2.Cond_contribution_1_18
                                                    else:
                                                        contribution2 = p2.Cond_contribution_1_20
            else:
                ## Next, Innocent/Acquitted
                if ((p1.participant.vars['ending_trial_status'] == True and p1.participant.vars[
                    'ending_guilt'] == False)
                    and (p3.participant.vars['ending_trial_status'] == False)) or ((p3.participant.vars[
                                                                                        'ending_trial_status'] == True and
                                                                                    p3.participant.vars[
                                                                                        'ending_guilt'] == False)
                                                                                   and (p1.participant.vars[
                                                                                            'ending_trial_status'] == False)):
                    if unconditionalcontributions == 0:
                        contribution2 = p2.Cond_contribution_2_0
                    else:
                        if unconditionalcontributions == 1:
                            contribution2 = p2.Cond_contribution_2_2
                        else:
                            if unconditionalcontributions == 2:
                                contribution2 = p2.Cond_contribution_2_4
                            else:
                                if unconditionalcontributions == 3:
                                    contribution2 = p2.Cond_contribution_2_6
                                else:
                                    if unconditionalcontributions == 4:
                                        contribution2 = p2.Cond_contribution_2_8
                                    else:
                                        if unconditionalcontributions == 5:
                                            contribution2 = p2.Cond_contribution_2_10
                                        else:
                                            if unconditionalcontributions == 6:
                                                contribution2 = p2.Cond_contribution_2_12
                                            else:
                                                if unconditionalcontributions == 7:
                                                    contribution2 = p2.Cond_contribution_2_14
                                                else:
                                                    if unconditionalcontributions == 8:
                                                        contribution2 = p2.Cond_contribution_2_16
                                                    else:
                                                        if unconditionalcontributions == 9:
                                                            contribution2 = p2.Cond_contribution_2_18
                                                        else:
                                                            contribution2 = p2.Cond_contribution_2_20
                else:
                    ## Next, Innocent/Guilty
                    if (p1.participant.vars['ending_trial_status'] == False and p3.participant.vars[
                        'ending_guilt'] == True) \
                            or (p1.participant.vars['ending_guilt'] == True or p3.participant.vars[
                        'ending_trial_status'] == False):
                        if unconditionalcontributions == 0:
                            contribution2 = p2.Cond_contribution_3_0
                        else:
                            if unconditionalcontributions == 1:
                                contribution2 = p2.Cond_contribution_3_2
                            else:
                                if unconditionalcontributions == 2:
                                    contribution2 = p2.Cond_contribution_3_4
                                else:
                                    if unconditionalcontributions == 3:
                                        contribution2 = p2.Cond_contribution_3_6
                                    else:
                                        if unconditionalcontributions == 4:
                                            contribution2 = p2.Cond_contribution_3_8
                                        else:
                                            if unconditionalcontributions == 5:
                                                contribution2 = p2.Cond_contribution_3_10
                                            else:
                                                if unconditionalcontributions == 6:
                                                    contribution2 = p2.Cond_contribution_3_12
                                                else:
                                                    if unconditionalcontributions == 7:
                                                        contribution2 = p2.Cond_contribution_3_14
                                                    else:
                                                        if unconditionalcontributions == 8:
                                                            contribution2 = p2.participant.vars[
                                                                'Cond_contribution_3_16']
                                                        else:
                                                            if unconditionalcontributions == 9:
                                                                contribution2 = p2.Cond_contribution_3_18
                                                            else:
                                                                contribution2 = p2.Cond_contribution_3_20
                    else:
                        ##Next, Acquitted/Acquitted
                        if (p1.participant.vars['ending_trial_status'] == True and p1.participant.vars[
                            'ending_guilt'] == False) and \
                                (p3.participant.vars['ending_trial_status'] == True and p3.participant.vars[
                                    'ending_guilt'] == False):
                            if unconditionalcontributions == 0:
                                contribution2 = p2.Cond_contribution_4_0
                            else:
                                if unconditionalcontributions == 1:
                                    contribution2 = p2.Cond_contribution_4_2
                                else:
                                    if unconditionalcontributions == 2:
                                        contribution2 = p2.Cond_contribution_4_4
                                    else:
                                        if unconditionalcontributions == 3:
                                            contribution2 = p2.Cond_contribution_4_6
                                        else:
                                            if unconditionalcontributions == 4:
                                                contribution2 = p2.Cond_contribution_4_8
                                            else:
                                                if unconditionalcontributions == 5:
                                                    contribution2 = p2.Cond_contribution_4_10
                                                else:
                                                    if unconditionalcontributions == 6:
                                                        contribution2 = p2.Cond_contribution_4_12
                                                    else:
                                                        if unconditionalcontributions == 7:
                                                            contribution2 = p2.Cond_contribution_4_14
                                                        else:
                                                            if unconditionalcontributions == 8:
                                                                contribution2 = p2.Cond_contribution_4_16
                                                            else:
                                                                if unconditionalcontributions == 9:
                                                                    contribution2 = p2.Cond_contribution_4_18
                                                                else:
                                                                    contribution2 = p2.Cond_contribution_4_20
                        else:
                            ## Next, Guilty/Guilty
                            if (p1.participant.vars['ending_guilt'] == True and p3.participant.vars[
                                'ending_guilt'] == True):
                                if unconditionalcontributions == 0:
                                    contribution2 = p2.Cond_contribution_6_0
                                else:
                                    if unconditionalcontributions == 1:
                                        contribution2 = p2.Cond_contribution_6_2
                                    else:
                                        if unconditionalcontributions == 2:
                                            contribution2 = p2.Cond_contribution_6_4
                                        else:
                                            if unconditionalcontributions == 3:
                                                contribution2 = p2.Cond_contribution_6_6
                                            else:
                                                if unconditionalcontributions == 4:
                                                    contribution2 = p2.Cond_contribution_6_8
                                                else:
                                                    if unconditionalcontributions == 5:
                                                        contribution2 = p2.Cond_contribution_6_10
                                                    else:
                                                        if unconditionalcontributions == 6:
                                                            contribution2 = p2.Cond_contribution_6_12
                                                        else:
                                                            if unconditionalcontributions == 7:
                                                                contribution2 = p2.Cond_contribution_6_14
                                                            else:
                                                                if unconditionalcontributions == 8:
                                                                    contribution2 = p2.Cond_contribution_6_16
                                                                else:
                                                                    if unconditionalcontributions == 9:
                                                                        contribution2 = p2.Cond_contribution_6_18
                                                                    else:
                                                                        contribution2 = p2.Cond_contribution_6_20
                            ## Last, Acquitted/Guilty
                            else:
                                if unconditionalcontributions == 0:
                                    contribution2 = p2.Cond_contribution_6_0
                                else:
                                    if unconditionalcontributions == 1:
                                        contribution2 = p2.Cond_contribution_6_2
                                    else:
                                        if unconditionalcontributions == 2:
                                            contribution2 = p2.Cond_contribution_6_4
                                        else:
                                            if unconditionalcontributions == 3:
                                                contribution2 = p2.Cond_contribution_6_6
                                            else:
                                                if unconditionalcontributions == 4:
                                                    contribution2 = p2.Cond_contribution_6_8
                                                else:
                                                    if unconditionalcontributions == 5:
                                                        contribution2 = p2.Cond_contribution_6_10
                                                    else:
                                                        if unconditionalcontributions == 6:
                                                            contribution2 = p2.Cond_contribution_6_12
                                                        else:
                                                            if unconditionalcontributions == 7:
                                                                contribution2 = p2.Cond_contribution_6_14
                                                            else:
                                                                if unconditionalcontributions == 8:
                                                                    contribution2 = p2.Cond_contribution_6_16
                                                                else:
                                                                    if unconditionalcontributions == 9:
                                                                        contribution2 = p2.Cond_contribution_6_18
                                                                    else:
                                                                        contribution2 = p2.Cond_contribution_6_20
        else:
            if unconditionalcontributions == 0:
                contribution2 = p2.Cond_contribution_1_0
            else:
                if unconditionalcontributions == 1:
                    contribution2 = p2.Cond_contribution_1_2
                else:
                    if unconditionalcontributions == 2:
                        contribution2 = p2.Cond_contribution_1_4
                    else:
                        if unconditionalcontributions == 3:
                            contribution2 = p2.Cond_contribution_1_6
                        else:
                            if unconditionalcontributions == 4:
                                contribution2 = p2.Cond_contribution_1_8
                            else:
                                if unconditionalcontributions == 5:
                                    contribution2 = p2.Cond_contribution_1_10
                                else:
                                    if unconditionalcontributions == 6:
                                        contribution2 = p2.Cond_contribution_1_12
                                    else:
                                        if unconditionalcontributions == 7:
                                            contribution2 = p2.Cond_contribution_1_14
                                        else:
                                            if unconditionalcontributions == 8:
                                                contribution2 = p2.Cond_contribution_1_16
                                            else:
                                                if unconditionalcontributions == 9:
                                                    contribution2 = p2.Cond_contribution_1_18
                                                else:
                                                    contribution2 = p2.Cond_contribution_1_20

        groupaccount = contribution1 + contribution2 + contribution3
        groupaccountreturn = Constants.multiplier * groupaccount
        payoff1 = (Constants.endowment - contribution1) + groupaccountreturn
        payoff2 = (Constants.endowment - contribution2) + groupaccountreturn
        payoff3 = (Constants.endowment - contribution3) + groupaccountreturn
        p1.participant.vars['payoffmodule4'] = payoff1
        p2.participant.vars['payoffmodule4'] = payoff2
        p3.participant.vars['payoffmodule4'] = payoff3


class Player(BasePlayer):
    contribution1 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_0 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $0.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $2.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $4.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $6.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_8 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $8.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_10 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $10.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_12 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $12.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_14 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $14.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_16 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $16.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_18 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $18.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_1_20 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $20.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    contribution2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_0 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $0.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $2.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $4.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $6.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_8 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $8.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_10 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $10.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_12 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $12.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_14 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $14.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_16 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $16.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_18 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $18.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_2_20 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $20.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    contribution3 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_0 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $0.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $2.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $4.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $6.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_8 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $8.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_10 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $10.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_12 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $12.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_14 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $14.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_16 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $16.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_18 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $18.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_3_20 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $20.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    contribution4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_0 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $0.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $2.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $4.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $6.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_8 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $8.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_10 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $10.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_12 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $12.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_14 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $14.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_16 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $16.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_18 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $18.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_4_20 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $20.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    contribution5 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_0 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $0.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $2.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $4.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $6.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_8 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $8.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_10 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $10.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_12 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $12.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_14 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $14.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_16 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $16.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_18 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $18.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_5_20 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $20.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    contribution6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_0 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $0.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $2.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $4.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $6.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_8 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $8.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_10 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $10.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_12 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $12.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_14 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $14.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_16 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $16.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_18 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $18.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    Cond_contribution_6_20 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='How many dollars from '
              'your endowment would you like to contribute to the group account if the other members contribute $20.00?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    belief1 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='What do you believe a participant who has never been accused of taking ANY '
              'amount of money from their partner will contribute to the group account on average?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    belief2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='What do you believe a participant who HAS been accused of taking some amount of money from their '
              'partner, '
              'but never found '
              'guilty, '
              'will contribute to the group account on average?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    belief3 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        min=0,
        max=10,
        label='What do you believe a participant who HAS been accused and HAS been found guilty '
              'of taking some amount of money from their '
              'partner will contribute to the group account on average?',
        widget=widgets.Slider(attrs={'step': '2'})
    )

    quiz1 = models.IntegerField(
        choices=[
            [1, '(a) You are each endowed with with 5.'],
            [2, '(b) You are endowed with 10 and your partners endowed with with 0.'],
            [3, '(c) Your partners are endowed with 10 and you start with 0.'],
            [4, '(d) You are each endowed with 10.']
        ],
        widget=widgets.RadioSelect,
        label="Question 1: How many dollars are you and your partners endowed with for this part of the experiment?"
    )

    quiz2 = models.IntegerField(
        choices=[
            [1, '(a) Everyone will earn $2 ($4 x 0.5) from your contribution.'],
            [2, '(b) Everyone will earn $4 ($4 x 1.0) from your contribution.'],
            [3, '(c) Everyone will earn $1 ($4 x 0.25) from your contribution.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 2: If you contribute $4 to the Group Account "
    )

    quiz3 = models.IntegerField(
        choices=[
            [1, '(a) $0 is held in your Private Account.'],
            [2, '(b) $4 is held in your Private Account.'],
            [3, '(c) $6 is held is your Private Account.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 3: If you contribute $4 to the Group Account "
    )

    quiz4 = models.IntegerField(
        choices=[
            [1, '(a) All partners you could interact with in this part of the experiment are guaranteed to have '
                'taken money from others previously.'],
            [2, '(b) Some partners who were truly innocent may have been found guilty of taking money from another '
                'subject.'],
            [3, '(c) Partners who were found guilty of taking money from another participant faced no monetary '
                'penalty from their guilty finding.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 4: Which of the following is true "
    )

    def keep_contributions(self):
        self.participant.vars['contribution1'] = self.contribution1
        self.participant.vars['Cond_contribution_1_0'] = self.Cond_contribution_1_0
        self.participant.vars['Cond_contribution_1_2'] = self.Cond_contribution_1_2
        self.participant.vars['Cond_contribution_1_4'] = self.Cond_contribution_1_4
        self.participant.vars['Cond_contribution_1_6'] = self.Cond_contribution_1_6
        self.participant.vars['Cond_contribution_1_8'] = self.Cond_contribution_1_8
        self.participant.vars['Cond_contribution_1_10'] = self.Cond_contribution_1_10
        self.participant.vars['Cond_contribution_1_12'] = self.Cond_contribution_1_12
        self.participant.vars['Cond_contribution_1_14'] = self.Cond_contribution_1_14
        self.participant.vars['Cond_contribution_1_16'] = self.Cond_contribution_1_16
        self.participant.vars['Cond_contribution_1_18'] = self.Cond_contribution_1_18
        self.participant.vars['Cond_contribution_1_20'] = self.Cond_contribution_1_20
        self.participant.vars['contribution2'] = self.contribution2
        self.participant.vars['Cond_contribution_2_0'] = self.Cond_contribution_2_0
        self.participant.vars['Cond_contribution_2_2'] = self.Cond_contribution_2_2
        self.participant.vars['Cond_contribution_2_4'] = self.Cond_contribution_2_4
        self.participant.vars['Cond_contribution_2_6'] = self.Cond_contribution_2_6
        self.participant.vars['Cond_contribution_2_8'] = self.Cond_contribution_2_8
        self.participant.vars['Cond_contribution_2_10'] = self.Cond_contribution_2_10
        self.participant.vars['Cond_contribution_2_12'] = self.Cond_contribution_2_12
        self.participant.vars['Cond_contribution_2_14'] = self.Cond_contribution_2_14
        self.participant.vars['Cond_contribution_2_16'] = self.Cond_contribution_2_16
        self.participant.vars['Cond_contribution_2_18'] = self.Cond_contribution_2_18
        self.participant.vars['Cond_contribution_2_20'] = self.Cond_contribution_2_20
        self.participant.vars['contribution3'] = self.contribution3
        self.participant.vars['Cond_contribution_3_0'] = self.Cond_contribution_3_0
        self.participant.vars['Cond_contribution_3_2'] = self.Cond_contribution_3_2
        self.participant.vars['Cond_contribution_3_4'] = self.Cond_contribution_3_4
        self.participant.vars['Cond_contribution_3_6'] = self.Cond_contribution_3_6
        self.participant.vars['Cond_contribution_3_8'] = self.Cond_contribution_3_8
        self.participant.vars['Cond_contribution_3_10'] = self.Cond_contribution_3_10
        self.participant.vars['Cond_contribution_3_12'] = self.Cond_contribution_3_12
        self.participant.vars['Cond_contribution_3_14'] = self.Cond_contribution_3_14
        self.participant.vars['Cond_contribution_3_16'] = self.Cond_contribution_3_16
        self.participant.vars['Cond_contribution_3_18'] = self.Cond_contribution_3_18
        self.participant.vars['Cond_contribution_3_20'] = self.Cond_contribution_3_20
        self.participant.vars['contribution4'] = self.contribution4
        self.participant.vars['Cond_contribution_4_0'] = self.Cond_contribution_4_0
        self.participant.vars['Cond_contribution_4_2'] = self.Cond_contribution_4_2
        self.participant.vars['Cond_contribution_4_4'] = self.Cond_contribution_4_4
        self.participant.vars['Cond_contribution_4_6'] = self.Cond_contribution_4_6
        self.participant.vars['Cond_contribution_4_8'] = self.Cond_contribution_4_8
        self.participant.vars['Cond_contribution_4_10'] = self.Cond_contribution_4_10
        self.participant.vars['Cond_contribution_4_12'] = self.Cond_contribution_4_12
        self.participant.vars['Cond_contribution_4_14'] = self.Cond_contribution_4_14
        self.participant.vars['Cond_contribution_4_16'] = self.Cond_contribution_4_16
        self.participant.vars['Cond_contribution_4_18'] = self.Cond_contribution_4_18
        self.participant.vars['Cond_contribution_4_20'] = self.Cond_contribution_4_20
        self.participant.vars['contribution5'] = self.contribution5
        self.participant.vars['Cond_contribution_5_0'] = self.Cond_contribution_5_0
        self.participant.vars['Cond_contribution_5_2'] = self.Cond_contribution_5_2
        self.participant.vars['Cond_contribution_5_4'] = self.Cond_contribution_5_4
        self.participant.vars['Cond_contribution_5_6'] = self.Cond_contribution_5_6
        self.participant.vars['Cond_contribution_5_8'] = self.Cond_contribution_5_8
        self.participant.vars['Cond_contribution_5_10'] = self.Cond_contribution_5_10
        self.participant.vars['Cond_contribution_5_12'] = self.Cond_contribution_5_12
        self.participant.vars['Cond_contribution_5_14'] = self.Cond_contribution_5_14
        self.participant.vars['Cond_contribution_5_16'] = self.Cond_contribution_5_16
        self.participant.vars['Cond_contribution_5_18'] = self.Cond_contribution_5_18
        self.participant.vars['Cond_contribution_5_20'] = self.Cond_contribution_5_20
        self.participant.vars['contribution6'] = self.contribution6
        self.participant.vars['Cond_contribution_6_0'] = self.Cond_contribution_6_0
        self.participant.vars['Cond_contribution_6_2'] = self.Cond_contribution_6_2
        self.participant.vars['Cond_contribution_6_4'] = self.Cond_contribution_6_4
        self.participant.vars['Cond_contribution_6_6'] = self.Cond_contribution_6_6
        self.participant.vars['Cond_contribution_6_8'] = self.Cond_contribution_6_8
        self.participant.vars['Cond_contribution_6_10'] = self.Cond_contribution_6_10
        self.participant.vars['Cond_contribution_6_12'] = self.Cond_contribution_6_12
        self.participant.vars['Cond_contribution_6_14'] = self.Cond_contribution_6_14
        self.participant.vars['Cond_contribution_6_16'] = self.Cond_contribution_6_16
        self.participant.vars['Cond_contribution_6_18'] = self.Cond_contribution_6_18
        self.participant.vars['Cond_contribution_6_20'] = self.Cond_contribution_6_20

    def role(self):
        if self.participant.id_in_session % 2 == 0:
            return 'primed'
        else:
            return 'unprimed'

    def chosen_one_selector(self):
        if self.id_in_group == 1:
            self.chosen_one = True
        else:
            self.chosen_one = False
