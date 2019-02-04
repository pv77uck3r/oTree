import xlrd
import os.path
from itertools import product
import numpy as np
from random import shuffle
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jason Ralston'

doc = """
Defendants love this game.
"""

def plea_decision(label):
    return models.IntegerField(
        choices=[
            [1, 'Accept plea'],
            [2, 'Go to trial and present your evidence of innocence'],
            [3, 'Go to trial and exercise right to not present your evidence of innocence']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def plea_decision2(label):
    return models.IntegerField(
        choices=[
            [1, 'Accept plea'],
            [3, 'Go to trial and exercise right to not present your evidence of innocence']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def trial_decision(label):
    return models.IntegerField(
        choices=[
            [1, 'Go to trial and present your evidence of innocence'],
            [2, 'Go to trial and exercise right to not present your evidence of innocence']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def trial_decision2(label):
    return models.IntegerField(
        choices=[
            [2, 'Go to trial and exercise right to not present your evidence of innocence']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

class Constants(BaseConstants):
    name_in_url = 'criminal_plea_ALT_3'
    players_per_group = None
    num_rounds = 18

    EFFORT_TO_COST = {
        .1: 0,
        .2: 1,
        .3: 2,
        .4: 4,
        .5: 6,
        .6: 8,
        .7: 10,
        .8: 12,
        .9: 15,
        1: 18}

def cost_from_effort(effort):
        return c(Constants.EFFORT_TO_COST[effort])


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


    def gen_info_sets(self):
        if self.round_number == 1:
            for p in self.get_players():

                # Generating sets of innocence: 1 is the true level of innocence, the other is from higher/lower
                # category and is purely hypothetical

                if p.participant.vars['innocencelevel'].item() == 1 or p.participant.vars['innocencelevel'].item() == 2:
                    p.alt_innocence_level = np.random.choice([3, 4])
                else:
                    p.alt_innocence_level = np.random.choice([1, 2])
                p.participant.vars['conjinnocencelevels'] = [p.participant.vars['innocencelevel'].item(), p.alt_innocence_level]

                # Generating sets of guilt: 1 is the true level of guilty, the other is from higher/lower category
                # and is purely hypothetical

                # if p.participant.vars['guiltlevel'] == 1 or p.participant.vars['guiltlevel'] == 2:
                #     p.alt_guilt_level = np.random.choice([3, 4])
                # else:
                #     p.alt_guilt_level = np.random.choice([1, 2])
                p.participant.vars['conjguiltlevels'] = [2, 3, 4]

                # Creating triplet of real, fake, and fake punishment levels:
                # Also creating the true punishment amount and crime level
                if p.participant.vars['proschoice'] == 2 or p.participant.vars['proschoice'] == 1:
                    p.alt_pun_level_1 = np.random.choice([.2, .5])
                    p.alt_pun_level_2 = np.random.choice([.7, 1])
                    p.alt_pun_level_3 = 1.2
                    p.participant.vars['conjpunlevel'] = [p.alt_pun_level_1, p.alt_pun_level_2, p.alt_pun_level_3]
                if p.participant.vars['proschoice'] == 3:
                    if p.participant.vars['pleacharge'] == 1:
                        p.alt_pun_level_1 = .2
                        p.alt_pun_level_2 = np.random.choice([.7, 1])
                        p.alt_pun_level_3 = 1.2
                        p.participant.vars['conjpunlevel'] = [p.alt_pun_level_1, p.alt_pun_level_2, p.alt_pun_level_3]
                    if p.participant.vars['pleacharge'] == 2:
                        p.alt_pun_level_1 = .5
                        p.alt_pun_level_2 = np.random.choice([.7, 1])
                        p.alt_pun_level_3 = 1.2
                        p.participant.vars['conjpunlevel'] = [p.alt_pun_level_1, p.alt_pun_level_2, p.alt_pun_level_3]
                    if p.participant.vars['pleacharge'] == 3:
                        p.alt_pun_level_1 = np.random.choice([.2, .5])
                        p.alt_pun_level_2 = .7
                        p.alt_pun_level_3 = 1.2
                        p.participant.vars['conjpunlevel'] = [p.alt_pun_level_1, p.alt_pun_level_2, p.alt_pun_level_3]
                    if p.participant.vars['pleacharge'] == 4:
                        p.alt_pun_level_1 = np.random.choice([.2, .5])
                        p.alt_pun_level_2 = 1
                        p.alt_pun_level_3 = 1.2
                        p.participant.vars['conjpunlevel'] = [p.alt_pun_level_1, p.alt_pun_level_2, p.alt_pun_level_3]
                    if p.participant.vars['pleacharge'] == 5:
                        p.alt_pun_level_1 = np.random.choice([.2, .5])
                        p.alt_pun_level_2 = np.random.choice([.7, 1])
                        p.alt_pun_level_3 = 1.2
                        p.participant.vars['conjpunlevel'] = [p.alt_pun_level_1, p.alt_pun_level_2, p.alt_pun_level_3]

                p.participant.vars['realtriplet'] = [p.participant.vars['innocencelevel'].item(), p.participant.vars['guiltlevel'].item(), p.participant.vars['pleapunishment']]
                np.random.shuffle(p.participant.vars['conjinnocencelevels'])
                np.random.shuffle(p.participant.vars['conjguiltlevels'])
                p.participant.vars['infosets'] = [p.participant.vars['conjinnocencelevels'],
                                                  p.participant.vars['conjguiltlevels'],
                                                  p.participant.vars['conjpunlevel']
                                                  ]

                # Now create all possible cartesian products of 1. innocence level, 2. guilt levels, 3. punishment
                # levels

                tupleproduct = [[w, x, y] for w in p.participant.vars['conjinnocencelevels'] for x in p.participant.vars['conjguiltlevels'] for y in p.participant.vars['conjpunlevel']]
                p.participant.vars['allpossibleinfo'] = tupleproduct
                if p.participant.vars['guiltlevel'].item() != 1:
                    if p.participant.vars['pleapunishment'] != -1:
                        p.participant.vars['whatround'] = p.participant.vars['allpossibleinfo'].index(p.participant.vars['realtriplet']) + 1
                    else:
                        p.participant.vars['whatround'] = p.participant.vars['allpossibleinfo'].index([p.participant.vars['innocencelevel'].item(), p.participant.vars['guiltlevel'].item(), 1.2]) + 1
                else:
                    p.participant.vars['whatround'] = 1

class Group(BaseGroup):

    def set_payoffs_1(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if not (p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3):
            amount_offered = p1.participant.vars['agent_fixed_pay_1_ALT']
            if amount_offered == 0:
                accept = p2.participant.vars['contract_accepted_1_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_1_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 10:
                accept = p2.participant.vars['contract_accepted_2_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_2_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 20:
                accept = p2.participant.vars['contract_accepted_3_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_3_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 30:
                accept = p2.participant.vars['contract_accepted_4_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_4_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 40:
                accept = p2.participant.vars['contract_accepted_5_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_5_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 50:
                accept = p2.participant.vars['contract_accepted_6_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_6_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 60:
                accept = p2.participant.vars['contract_accepted_7_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_7_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 70:
                accept = p2.participant.vars['contract_accepted_8_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_8_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 80:
                accept = p2.participant.vars['contract_accepted_9_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_9_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 90:
                accept = p2.participant.vars['contract_accepted_10_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_10_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 100:
                accept = p2.participant.vars['contract_accepted_11_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_11_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 110:
                accept = p2.participant.vars['contract_accepted_12_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_12_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if amount_offered == 120:
                accept = p2.participant.vars['contract_accepted_13_ALT']
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_13_ALT']
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20

        if p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3:
            if p2.participant.vars['ending_guilt_level'] == 0:
                amount_offered = p1.participant.vars['agent_fixed_pay_2_ALT']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if p2.participant.vars['ending_guilt_level'] == 1:
                amount_offered = p1.participant.vars['agent_fixed_pay_3_ALT']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if p2.participant.vars['ending_guilt_level'] == 2:
                amount_offered = p1.participant.vars['agent_fixed_pay_4_ALT']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
            if p2.participant.vars['ending_guilt_level'] == 3:
                amount_offered = p1.participant.vars['agent_fixed_pay_5_ALT']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13_ALT']
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13_ALT']
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
        p1.payoffmodule4 = p1.participant.vars['payoffmodule4'] * .10 + 2
        p2.payoffmodule4 = p2.participant.vars['payoffmodule4'] * .10 + 2


class Player(BasePlayer):

    quiz1 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='Question 1: If you accept a plea bargain you are not contesting your guilt (in other words you are not claiming '
              'innocence)'
    )

    quiz2 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='Question 2: If you accept a plea bargain or are found guilty at the experimental trial, then the monetary penalty '
              'will reduce your experimental payment today.'
    )

    quiz3 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'The prosecutor has to present the evidence of guilt you see in the plea bargain trial threat'],
            [2, 'You have to present your evidence of innocence'],
            [3, 'There is no monetary penalty if you are found guilty']
        ],
        label='Question 3: At trial, which of the following is true?'
    )

    plea_decision2 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.40 and $0.60 '
                                   '(a Small Crime) you will'
    )
    plea_decision3 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.60 and $0.80 '
                                   '(a Medium Crime) you will'
    )
    plea_decision4 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.90 and $1.10 '
                                   '(a Medium Crime) you will'
    )
    plea_decision5 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $1.10 and $1.30 '
                                   '(a Large Crime) you will'
    )
    plea_decision6 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $1.40 and $1.60 '
                                   '(a Large Crime) you will'
    )

    trial_decision1 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.10 and $0.30 '
                                   '(a Small Crime) you will'
    )
    trial_decision2 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.40 and $0.60 '
                                   '(a Small Crime) you will'
    )
    trial_decision3 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.60 and $0.80 '
                                   '(a Medium Crime) you will'
    )
    trial_decision4 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $0.90 and $1.10 '
                                   '(a Medium Crime) you will'
    )
    trial_decision5 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $1.10 and $1.30 '
                                   '(a Large Crime) you will'
    )
    trial_decision6 = models.IntegerField(
        widget=widgets.RadioSelect,
        label='If the monetary penalty for being found guilty at trial is between $1.40 and $1.60 '
                                   '(a Large Crime) you will'
    )

    belief = models.IntegerField(
        min=0,
        max=100,
        widget=widgets.Slider(attrs={'size': 100}),
        label=''
    )

    alt_innocence_level = models.IntegerField()

    alt_guilt_level = models.IntegerField()

    alt_pun_level_1 = models.FloatField()

    alt_pun_level_2 = models.FloatField()

    alt_pun_level_3 = models.FloatField()

    ending_guilt = models.BooleanField()

    ending_guilt_level = models.IntegerField()

    ending_punishment = models.CurrencyField()

    ending_trial_status = models.BooleanField()

    relevant_decision = models.IntegerField()

    innocence_level = models.IntegerField()

    guilt_level = models.IntegerField()

    plea_punishment = models.FloatField()

    no_plea_punishment = models.FloatField()

    crime_level = models.IntegerField()

    pros_choice = models.IntegerField()

    plea_threat = models.IntegerField()

    innocence_level_this_round = models.IntegerField()

    guilt_level_this_round = models.IntegerField()

    plea_punishment_this_round = models.FloatField()

    what_round = models.IntegerField()

    payoffmodule3 = models.CurrencyField()

    trialcrime = models.IntegerField()
    defenseevid = models.IntegerField()
    prosevid = models.IntegerField()

    # Trial status:
    # True - went to trial
    # False - took plea

    def set_payoff(self):
        # WE RECORD DECISIONS ONLY WHEN THE INNOCENCE LEVEL, GUILT LEVEL, AND PLEA MATCH THOSE SEEN BY A JURY OR PLEA
        # OFFERED BY A PROSECUTOR
        self.innocence_level = self.participant.vars['innocencelevel'].item()
        self.guilt_level = self.participant.vars['guiltlevel'].item()
        self.crime_level = self.participant.vars['crimelevel']
        self.pros_choice = self.participant.vars['proschoice']
        self.plea_punishment = self.participant.vars['pleapunishment']
        self.no_plea_punishment = self.participant.vars['nopleapun']
        self.plea_threat = self.participant.vars['pleathreat']
        self.innocence_level_this_round = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0]
        self.guilt_level_this_round = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1]
        self.plea_punishment_this_round = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2]
        self.what_round = self.participant.vars['whatround']

        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0] == self.participant.vars['innocencelevel'].item() and \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1] == self.participant.vars['guiltlevel'].item() and \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == self.participant.vars['pleapunishment']:

                # FIRST WE LOOK AT WHEN THE PROSECUTOR DECIDES TO MAKE A PLEA OFFER

                if self.participant.vars['proschoice'] == 3:

                    # NOW WE RESTRICT OUR ATTENTION TO WHICH PLEA THREAT WAS MADE

                    if self.participant.vars['pleathreat'] == 1:

                        # WE RECORD THE DEFENDANT'S DECISION

                        self.participant.vars['relevantdecision'] = self.plea_decision2
                    if self.participant.vars['pleathreat'] == 2:
                        self.participant.vars['relevantdecision'] = self.plea_decision3
                    if self.participant.vars['pleathreat'] == 3:
                        self.participant.vars['relevantdecision'] = self.plea_decision4
                    if self.participant.vars['pleathreat'] == 4:
                        self.participant.vars['relevantdecision'] = self.plea_decision5
                    if self.participant.vars['pleathreat'] == 5:
                        self.participant.vars['relevantdecision'] = self.plea_decision6

                    # IF THE DEFENDANT TAKES THE PLEA DEAL, INDICATED BY A 1, THEN WE SET THEIR PAYOFF FOR THIS MODULE
                    # TO THE PROPOSED PUNISHMENT AMOUNT

                    if self.participant.vars['relevantdecision'] == 1:
                        self.ending_guilt = True
                        self.ending_guilt_level = self.participant.vars['pleacrimelevel']
                        self.ending_punishment = self.participant.vars['pleapunishment']
                        self.ending_trial_status = False
                        self.payoff = -self.participant.vars['pleapunishment']
                        self.relevant_decision = self.participant.vars['relevantdecision']

                    # IF THE DEFENDANT GOES TO TRIAL WITH THEIR INNOCENCE LEVEL PROVIDED, INDICATED BY A 2, THEN WE
                    # GATHER THE THE THREATENED CRIME LEVEL (FROM PROSECUTOR), THREATENED EVIDENCE LEVEL (FROM
                    # PROSECUTOR), AND THE INNOCENCE LEVEL (FROM DEFENDANT) AND FIND THE APPROPRIATE ROW IN THE JURY
                    # DECISION TABLE, AND SIMULATE A TRIAL.

                    if self.participant.vars['relevantdecision'] == 2:
                        self.ending_trial_status = True
                        if self.participant.vars['pleathreat'] == 1:
                            trialcrime = 1
                            trialdefevid = self.participant.vars['innocencelevel'].item()
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 2:
                            trialcrime = 2
                            trialdefevid = self.participant.vars['innocencelevel'].item()
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 3:
                            trialcrime = 2
                            trialdefevid = self.participant.vars['innocencelevel'].item()
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 4:
                            trialcrime = 3
                            trialdefevid = self.participant.vars['innocencelevel'].item()
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 5:
                            trialcrime = 3
                            trialdefevid = self.participant.vars['innocencelevel'].item()
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']

                        # HERE WE ACTUALLY SIMULATE THE GUILTY/NOT GUILTY FINDING FROM THE JURY TABLE

                        self.trialcrime = trialcrime
                        self.defenseevid = trialdefevid

                        if trialdefevid == 1:
                            trialdefevid = 0
                        else:
                            if trialdefevid == 2:
                                trialdefevid = 1
                            else:
                                if trialdefevid == 3:
                                    trialdefevid = 2
                                else:
                                    if trialdefevid == 4:
                                        trialdefevid = 3

                        self.prosevid = trialprosevid

                        self.participant.vars['jurydecision'] = np.random.binomial(1, (self.session.vars['juryprobs'].loc[(self.session.vars['juryprobs']['Crime'] == trialcrime) & (self.session.vars['juryprobs']['Defense evidence'] == trialdefevid) & (self.session.vars['juryprobs']['Prosecutor evidence'] == trialprosevid), 'Probability of a guilty findng at trial'].item()))

                        # IF JURY DECIDES NOT GUILTY, INDICATED BY A 0, THEN NO PUNISHMENT

                        if self.participant.vars['jurydecision'] == 0:
                            self.payoff = 0
                            self.ending_guilt = False
                            self.ending_guilt_level = 0
                            self.ending_punishment = 0
                            self.relevant_decision = self.participant.vars['relevantdecision']

                        # IF JURY DECIDES GUILTY, THEN WE LOOK AT THE RELEVANT THREAT LEVEL AND GENERATE A PUNISHMENT

                        else:
                            self.ending_guilt = True
                            if self.participant.vars['pleathreat'] == 1:
                                self.ending_punishment = np.random.choice([.1, .2, .3])
                                self.ending_guilt_level = 1
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 2:
                                self.ending_punishment = np.random.choice([.4, .5, .6])
                                self.ending_guilt_level = 1
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 3:
                                self.ending_punishment = np.random.choice([.6, .7, .8])
                                self.ending_guilt_level = 2
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 4:
                                self.ending_punishment = np.random.choice([.9, 1, 1.1])
                                self.ending_guilt_level = 2
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 5:
                                self.ending_punishment = np.random.choice([1.1, 1.2, 1.3])
                                self.ending_guilt_level = 3
                                self.relevant_decision = self.participant.vars['relevantdecision']

                    # WE DO SOMETHING VERY SIMILAR FOR WHEN THE DEFENDANT DECIDES TO PLEA THE FIFTH, INDICATED BY A 3

                    if self.participant.vars['relevantdecision'] == 3:
                        self.ending_trial_status = True
                        if self.participant.vars['pleathreat'] == 1:
                            trialcrime = 1
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 2:
                            trialcrime = 2
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 3:
                            trialcrime = 2
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 4:
                            trialcrime = 3
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        if self.participant.vars['pleathreat'] == 5:
                            trialcrime = 3
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                            self.relevant_decision = self.participant.vars['relevantdecision']

                        self.trialcrime = trialcrime
                        self.defenseevid = trialdefevid

                        if trialdefevid == 1:
                            trialdefevid = 0
                        else:
                            if trialdefevid == 2:
                                trialdefevid = 1
                            else:
                                if trialdefevid == 3:
                                    trialdefevid = 2
                                else:
                                    if trialdefevid == 4:
                                        trialdefevid = 3

                        self.prosevid = trialprosevid
                        self.participant.vars['jurydecision'] = np.random.binomial(1, (self.session.vars['juryprobs'].loc[(self.session.vars['juryprobs']['Crime'] == trialcrime) & (self.session.vars['juryprobs']['Defense evidence'] == trialdefevid) & (self.session.vars['juryprobs']['Prosecutor evidence'] == trialprosevid), 'Probability of a guilty findng at trial'].item()))

                        if self.participant.vars['jurydecision'] == 0:
                            self.payoff = 0
                            self.ending_guilt = False
                            self.ending_guilt_level = 0
                            self.ending_punishment = 0
                            self.relevant_decision = self.participant.vars['relevantdecision']
                        else:
                            self.ending_guilt = True
                            if self.participant.vars['pleathreat'] == 1:
                                self.ending_punishment = np.random.choice([.1, .2, .3])
                                self.ending_guilt_level = 1
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 2:
                                self.ending_punishment = np.random.choice([.4, .5, .6])
                                self.ending_guilt_level = 1
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 3:
                                self.ending_punishment = np.random.choice([.6, .7, .8])
                                self.ending_guilt_level = 2
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 4:
                                self.ending_punishment = np.random.choice([.9, 1, 1.1])
                                self.ending_guilt_level = 2
                                self.relevant_decision = self.participant.vars['relevantdecision']
                            if self.participant.vars['pleathreat'] == 5:
                                self.ending_punishment = np.random.choice([1.1, 1.2, 1.3])
                                self.ending_guilt_level = 3
                                self.relevant_decision = self.participant.vars['relevantdecision']

        # NEXT WE CONSIDER WHEN THEIR IS NO PLEA OFFER AND THE PROSECUTOR GOES STRAIGHT TO TRIAL. THIS IS ALL VERY
        # SIMILAR TO WHAT IS DONE ABOVE WHEN THE DEFENDANT WANTS TO GO TO TRIAL AGAINST A THREAT

        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0] == self.participant.vars['innocencelevel'].item() and \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1] == self.participant.vars['guiltlevel'].item() and \
                self.subsession.round_number % 3 == 0:

            if self.participant.vars['proschoice'] == 2:
                self.ending_trial_status = True
                if self.participant.vars['nopleapun'] == 0:
                    self.participant.vars['relevantdecision'] = self.trial_decision1
                    self.relevant_decision = self.participant.vars['relevantdecision']
                    trialcrime = 1
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel'].item()
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 1:
                    self.participant.vars['relevantdecision'] = self.trial_decision2
                    self.relevant_decision = self.participant.vars['relevantdecision']
                    trialcrime = 1
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel'].item()
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 2:
                    self.participant.vars['relevantdecision'] = self.trial_decision3
                    self.relevant_decision = self.participant.vars['relevantdecision']
                    trialcrime = 2
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel'].item()
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 3:
                    self.participant.vars['relevantdecision'] = self.trial_decision4
                    self.relevant_decision = self.participant.vars['relevantdecision']
                    trialcrime = 2
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel'].item()
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 4:
                    self.participant.vars['relevantdecision'] = self.trial_decision5
                    self.relevant_decision = self.participant.vars['relevantdecision']
                    trialcrime = 3
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel'].item()
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 5:
                    self.participant.vars['relevantdecision'] = self.trial_decision6
                    self.relevant_decision = self.participant.vars['relevantdecision']
                    trialcrime = 3
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel'].item()
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']

                self.trialcrime = trialcrime
                self.defenseevid = trialdefevid

                if trialdefevid == 1:
                    trialdefevid = 0
                else:
                    if trialdefevid == 2:
                        trialdefevid = 1
                    else:
                        if trialdefevid == 3:
                            trialdefevid = 2
                        else:
                            if trialdefevid == 4:
                                trialdefevid = 3

                self.prosevid = trialprosevid

                self.participant.vars['jurydecision'] = np.random.binomial(1, (self.session.vars['juryprobs'].loc[(self.session.vars['juryprobs']['Crime'] == trialcrime) & (self.session.vars['juryprobs']['Defense evidence'] == trialdefevid) & (self.session.vars['juryprobs']['Prosecutor evidence'] == trialprosevid), 'Probability of a guilty findng at trial'].item()))
                if self.participant.vars['jurydecision'] == 0:
                    self.payoff = 0
                    self.ending_guilt = False
                    self.ending_guilt_level = 0
                    self.ending_punishment = 0
                    self.relevant_decision = self.participant.vars['relevantdecision']
                else:
                    self.ending_guilt = True
                    if self.participant.vars['nopleapun'] == 0:
                        self.ending_punishment = np.random.choice([.1, .2, .3])
                        self.ending_guilt_level = 1
                    if self.participant.vars['nopleapun'] == 1:
                        self.ending_punishment = np.random.choice([.4, .5, .6])
                        self.ending_guilt_level = 1
                    if self.participant.vars['nopleapun'] == 2:
                        self.ending_punishment = np.random.choice([.6, .7, .8])
                        self.ending_guilt_level = 2
                    if self.participant.vars['nopleapun'] == 3:
                        self.ending_punishment = np.random.choice([.9, 1, 1.1])
                        self.ending_guilt_level = 2
                    if self.participant.vars['nopleapun'] == 4:
                        self.ending_punishment = np.random.choice([1.1, 1.2, 1.3])
                        self.ending_guilt_level = 3
                    if self.participant.vars['nopleapun'] == 5:
                        self.ending_punishment = np.random.choice([1.4, 1.5, 1.6])
                        self.ending_guilt_level = 3
            if self.participant.vars['proschoice'] == 1:
                self.ending_trial_status = False
                self.ending_guilt = False
                self.payoff = 0
                self.ending_guilt_level = 0
                self.ending_punishment = 0
                self.relevant_decision = 0

        # WE MUST ALSO CONSIDER THE CASE WHERE THE PROSECUTOR HAS NO EVIDENCE

        if self.participant.vars['guiltlevel'].item() == 1:
            self.ending_trial_status = False
            self.participant.vars['ending_trial_status'] = self.ending_trial_status
            self.ending_guilt = False
            self.participant.vars['ending_guilt'] = self.ending_guilt
            self.payoff = 0
            self.ending_guilt_level = 0
            self.participant.vars['ending_guilt_level'] = self.ending_guilt_level
            self.ending_punishment = 0
            self.participant.vars['ending_punishment'] = self.ending_punishment
            self.participant.vars['relevantdecision'] = None
            self.relevant_decision = self.participant.vars['relevantdecision']
            self.participant.vars['payoffmodule3'] = c(self.ending_punishment)

        # Record this decision so it can be displayed on final page

        # self.participant.vars['payoffmodule3'] = c(self.ending_punishment)

        # For excel checking purposes...
        if self.subsession.round_number == self.participant.vars['whatround']:
            self.participant.vars['ending_trial_status'] = self.ending_trial_status
            self.ending_trial_status = self.ending_trial_status
            self.participant.vars['ending_guilt'] = self.ending_guilt
            self.ending_guilt = self.ending_guilt
            self.payoff = self.payoff
            self.participant.vars['ending_guilt_level'] = self.ending_guilt_level
            self.ending_guilt_level = self.ending_guilt_level
            self.participant.vars['ending_punishment'] = self.ending_punishment
            self.participant.vars['payoffmodule3'] = c(-self.ending_punishment)
            self.ending_punishment = self.ending_punishment
            self.payoffmodule3 = self.participant.vars['ending_punishment']


            # THINGS RECORDED:
            # payoff - the resulting punishment, if anything
            # ending_guilt_level - what level of crime they were determined to have committed, if any
            # ending_punishment - same thing as payoff in this module


