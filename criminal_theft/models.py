import numpy as np
import pandas as pd
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Jason Ralston'

doc = """
Variant of lying game.
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_theft'
    players_per_group = 2
    num_rounds = 10

    ### EXPERIMENTER SETS THE NUMBER OF DRAWS BELOW ###

    numdraws = 10


class Subsession(BaseSubsession):

    groups_1_indicator_pre = models.BooleanField(initial=0)
    groups_1_indicator_post = models.BooleanField(initial=0)
    groups_2_indicator_pre = models.BooleanField(initial=0)
    groups_2_indicator_post = models.BooleanField(initial=0)

    def creating_session(self):
        self.set_group_matrix(self.session.vars['subjlists'][1])
        # Wdraws = [None]*len(self.get_players())
        # xdraws = [None]*len(self.get_players())
        # ydraws = [None]*len(self.get_players())
        # zdraws = [None]*len(self.get_players())
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['Wdraws'] = np.random.choice(np.arange(3.90, 7.00, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['xdraws'] = np.random.choice(np.arange(0.10, 1.10, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['ydraws'] = np.random.choice(np.arange(1.10, 2.10, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['zdraws'] = np.random.choice(np.arange(2.10, 3.10, 0.10), Constants.numdraws, replace=False)

    def set_groups_1(self):
        self.groups_1_indicator_pre = True
        self.set_group_matrix(self.session.vars['subjlists'][1])
        for group in self.get_groups():
            players = group.get_players()
            group.set_players(players)
        self.groups_1_indicator_post = True

    def set_groups_2(self):
        self.groups_2_indicator_pre = True
        self.set_group_matrix(self.session.vars['subjlists'][2])
        for group in self.get_groups():
            players = group.get_players()
            group.set_players(players)
        self.groups_2_indicator_post = True

            # for i in range(1, len(self.get_players())):
            #     W = np.random.choice(np.arange(3.90, 7.00, 0.10), 10, replace=False)
            #     x = np.random.choice(np.arange(0.10, 1.10, 0.10), 10, replace=False)
            #     y = np.random.choice(np.arange(1.00, 2.10, 0.10), 10, replace=False)
            #     z = np.random.choice(np.arange(2.00, 3.10, 0.10), 10, replace=False)
            #     Wdraws[i-1] = W
            #     xdraws[i-1] = x
            #     ydraws[i-1] = y
            #     zdraws[i-1] = z
            # self.session.vars['Wdraws'] = Wdraws
            # self.session.vars['xdraws'] = xdraws
            # self.session.vars['ydraws'] = ydraws
            # self.session.vars['zdraws'] = zdraws

    def retain_stuff(self):
        if self.round_number > 1:
            for p in self.get_players():
                p.retain_theft_round()

    def sub_record_choice(self):
        for p in self.get_players():
            p.record_choice()


class Group(BaseGroup):
    kept = models.FloatField()

    first_calc_indicator = models.BooleanField(initial=0)
    second_calc_indicator = models.BooleanField(initial=0)

    decisions_1_indicator = models.BooleanField(initial=0)
    decisions_2_indicator = models.BooleanField(initial=0)

    def group_decisions_1(self):
        if self.subsession.round_number == Constants.num_rounds:
            self.decisions_1_indicator = True
            p1 = self.get_player_by_id(1)
            p2 = self.get_player_by_id(2)
            if p1.participant.vars['theftchoice'] == 1:
                self.first_calc_indicator = True
                self.kept = p1.participant.vars['W']
            else:
                self.first_calc_indicator = True
                self.kept = p1.participant.vars['W'] + p1.participant.vars['amountstolen']
            p1.payoff1 = self.kept
            p2.payoff1 = 10 - self.kept

    def group_decisions_2(self):
        if self.subsession.round_number == Constants.num_rounds:
            self.decisions_2_indicator = True
            p1 = self.get_player_by_id(1)
            p2 = self.get_player_by_id(2)
            if p1.participant.vars['theftchoice'] == 1:
                self.second_calc_indicator = True
                self.kept = p1.participant.vars['W']
            else:
                self.second_calc_indicator = True
                self.kept = p1.participant.vars['W'] + p1.participant.vars['amountstolen']
            p1.payoff2 = self.kept
            p2.payoff2 = 10 - self.kept

    def set_payoffs(self):
        if self.subsession.round_number == Constants.num_rounds:
            p1 = self.get_player_by_id(1)
            p2 = self.get_player_by_id(2)
            p1.set_payoff()
            p2.set_payoff()


class Player(BasePlayer):

    payoff1 = models.FloatField()
    payoff2 = models.FloatField()

    record_choice_indicator = models.BooleanField(initial=False)

    proschoice = models.IntegerField()

    guiltlevel = models.IntegerField()
    innocencelevel = models.IntegerField()
    trulyinnocent = models.BooleanField()


    no_plea_charge = models.IntegerField()
    no_plea_evidence = models.IntegerField()
    no_plea_pun = models.IntegerField()
    plea_charge = models.IntegerField()
    plea_crime_level = models.IntegerField()
    plea_punishment = models.FloatField()
    plea_evidence = models.IntegerField()
    plea_threat = models.IntegerField()
    threat_charge = models.IntegerField()
    payoffmodule2 = models.CurrencyField()

    crime_indicator = models.IntegerField(initial=0)

    randround = models.IntegerField()

    theftchoice = models.IntegerField()

    # self.participant.vars['nopleacharge'] = -1
    # self.participant.vars['nopleaevidence'] = -1
    # self.participant.vars['nopleapun'] = -1
    # self.participant.vars['pleacharge'] = -1
    # self.participant.vars['pleacrimelevel'] = -1
    # self.participant.vars['pleapunishment'] = -1
    # self.participant.vars['pleaevidence'] = -1
    # self.participant.vars['pleaethreat'] = -1
    # self.participant.vars['threatcharge'] = -1

    quiz1 = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='Question 1: If you report the division of money accurately it is impossible for there to be evidence suggesting you '
              'are guilty.'
    )

    quiz2 = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='Question 2: If you report the division of money inaccurately (and take some of your counterpart\'s money), there is '
              'guaranteed to be evidence suggesting you are guilty.'
    )

    def role(self):
        if self.id_in_group == 1:
            return 'Thief'
        if self.id_in_group == 2:
            return 'NonThief'

    ThiefChoice = models.IntegerField(
        widget=widgets.RadioSelect,
        label='Please Report the Division'
    )

    def retain_theft_round(self):
        if self.subsession.round_number > 1:
            self.crime_indicator = self.in_round(self.subsession.round_number - 1).crime_indicator


    def record_choice(self):

        # LEVELS OF EVIDENCE CODING:
        # 1 - no evidence of ______
        # 2 - small evidence of ______
        # 3 - medium evidence of ______
        # 4 - large evidence of ______

        # CRIME LEVELS
        # 1 - no crime
        # 2 - small crime
        # 3 - medium crime
        # 4 - large crime

        #for p in self.get_players():

        # Choosing a random round #
        # Rounds are chosen at random, with increased probability on the first round in which a theft was committed #
        # This requires a lot of conditionals
        numplayer = len(self.subsession.get_players())
        if self.crime_indicator == 0:
            self.participant.vars['randround'] = np.random.choice(range(1, Constants.num_rounds + 1), replace=False)
        else:
            if self.crime_indicator == 1:
                p = [(1/2), (1/2)/(numplayer - 1), (1/2)/(numplayer - 1),
                                                                         (1/2)/(numplayer - 1), (1/2)/(numplayer - 1),
                                                                         (1/2)/(numplayer - 1), (1/2)/(numplayer - 1),
                                                                         (1/2)/(numplayer - 1), (1/2)/(numplayer - 1),
                                                                         (1/2)/(numplayer - 1)]
                p = [x / sum(p) for x in p]
                self.participant.vars['randround'] = np.random.choice(range(1, Constants.num_rounds + 1), replace=False,
                                                                      p=p)
            else:
                if self.crime_indicator == 2:
                    p = [(1 / 2) / (numplayer - 1), (1 / 2), (1 / 2) / (numplayer - 1),
                         (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                         (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                         (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                         (1 / 2) / (numplayer - 1)]
                    p = [x / sum(p) for x in p]
                    self.participant.vars['randround'] = np.random.choice(range(1, Constants.num_rounds + 1),
                                                                          replace=False,
                                                                          p=p)
                else:
                    if self.crime_indicator == 3:
                        p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1), (1 / 2),
                             (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                             (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                             (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                             (1 / 2) / (numplayer - 1)]
                        p = [x / sum(p) for x in p]
                        self.participant.vars['randround'] = np.random.choice(range(1, Constants.num_rounds + 1),
                                                                              replace=False,
                                                                              p=p)
                    else:
                        if self.crime_indicator == 4:
                            p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                 (1 / 2), (1 / 2) / (numplayer - 1),
                                 (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                 (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                 (1 / 2) / (numplayer - 1)]
                            p = [x / sum(p) for x in p]
                            self.participant.vars['randround'] = np.random.choice(range(1, Constants.num_rounds + 1),
                                                                                  replace=False,
                                                                                  p=p)
                        else:
                            if self.crime_indicator == 5:
                                p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                     (1 / 2) / (numplayer - 1), (1 / 2),
                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                     (1 / 2) / (numplayer - 1)]
                                p = [x / sum(p) for x in p]
                                self.participant.vars['randround'] = np.random.choice(
                                    range(1, Constants.num_rounds + 1),
                                    replace=False,
                                    p=p)
                            else:
                                if self.crime_indicator == 6:
                                    p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                         (1 / 2) / (numplayer - 1),
                                         (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                         (1 / 2), (1 / 2) / (numplayer - 1),
                                         (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                         (1 / 2) / (numplayer - 1)]
                                    p = [x / sum(p) for x in p]
                                    self.participant.vars['randround'] = np.random.choice(
                                        range(1, Constants.num_rounds + 1),
                                        replace=False,
                                        p=p)
                                else:
                                    if self.crime_indicator == 7:
                                        p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                             (1 / 2) / (numplayer - 1),
                                             (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                             (1 / 2) / (numplayer - 1), (1 / 2),
                                             (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                             (1 / 2) / (numplayer - 1)]
                                        p = [x / sum(p) for x in p]
                                        self.participant.vars['randround'] = np.random.choice(
                                            range(1, Constants.num_rounds + 1),
                                            replace=False,
                                            p=p)
                                    else:
                                        if self.crime_indicator == 8:
                                            p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                 (1 / 2) / (numplayer - 1),
                                                 (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                 (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                 (1 / 2), (1 / 2) / (numplayer - 1),
                                                 (1 / 2) / (numplayer - 1)]
                                            p = [x / sum(p) for x in p]
                                            self.participant.vars['randround'] = np.random.choice(
                                                range(1, Constants.num_rounds + 1),
                                                replace=False,
                                                p=p)
                                        else:
                                            if self.crime_indicator == 9:
                                                p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1), (1 / 2),
                                                     (1 / 2) / (numplayer - 1)]
                                                p = [x / sum(p) for x in p]
                                                self.participant.vars['randround'] = np.random.choice(
                                                    range(1, Constants.num_rounds + 1),
                                                    replace=False,
                                                    p=p)
                                            else:
                                                p = [(1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2) / (numplayer - 1), (1 / 2) / (numplayer - 1),
                                                     (1 / 2)]
                                                p = [x / sum(p) for x in p]
                                                self.participant.vars['randround'] = np.random.choice(
                                                    range(1, Constants.num_rounds + 1),
                                                    replace=False,
                                                    p=p)

        ThiefDecisions = [p.ThiefChoice for p in self.in_all_rounds()]

        self.randround = self.participant.vars['randround']
        self.record_choice_indicator = True
        self.participant.vars['W'] = self.participant.vars['Wdraws'][self.participant.vars['randround'] - 1]
        self.participant.vars['theftchoice'] = ThiefDecisions[self.participant.vars['randround'] - 1]
        self.theftchoice = self.participant.vars['theftchoice']
        if self.participant.vars['theftchoice'] == 1:
            self.participant.vars['amountstolen'] = 0
            self.participant.vars['crimelevel'] = 1
        if self.participant.vars['theftchoice'] == 2:
            self.participant.vars['amountstolen'] = self.participant.vars['xdraws'][self.participant.vars['randround'] - 1]
            self.participant.vars['crimelevel'] = 2
        if self.participant.vars['theftchoice'] == 3:
            self.participant.vars['amountstolen'] = self.participant.vars['ydraws'][self.participant.vars['randround'] - 1]
            self.participant.vars['crimelevel'] = 3
        if self.participant.vars['theftchoice'] == 4:
            self.participant.vars['amountstolen'] = self.participant.vars['zdraws'][self.participant.vars['randround'] - 1]
            self.participant.vars['crimelevel'] = 4
        if self.participant.vars['amountstolen'] == 0:
            self.participant.vars['trulyinnocent'] = True
            self.participant.vars['innocencelevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.2, .4, .25, .15])
            self.participant.vars['guiltlevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.7, .15, .1, .05])
        else:
            self.participant.vars['trulyinnocent'] = False
            self.participant.vars['innocencelevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.7, .15, .1, .05])
            self.participant.vars['guiltlevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.3, .3, .25, .15])
        if self.participant.vars['guiltlevel'] > 1:
            if self.participant.vars['crimelevel'] == 1:
                self.participant.vars['crimelevel'] = np.random.choice([2, 3, 4])
            if self.participant.vars['crimelevel'] == 2:
                self.participant.vars['crimelevel'] = np.random.choice([2, 3, 4], 1, replace=False,
                                                                       p=[.5, .25, .25])
            if self.participant.vars['crimelevel'] == 3:
                self.participant.vars['crimelevel'] = np.random.choice([2, 3, 4], 1, replace=False,
                                                                       p=[.25, .5, .25])
            if self.participant.vars['crimelevel'] == 4:
                self.participant.vars['crimelevel'] = np.random.choice([2, 3, 4], 1, replace=False,
                                                                       p=[.25, .25, .5])
        self.guiltlevel = self.participant.vars['guiltlevel']
        self.innocencelevel = self.participant.vars['innocencelevel']
        self.trulyinnocent = self.participant.vars['trulyinnocent']

        #def set_prosecutor_decisions(self):
        #if self.subsession.round_number == self.participant.vars['randround']:
        if self.participant.vars['guiltlevel'] == 1:
            self.participant.vars['proschoice'] = 1
            self.participant.vars['nopleacharge'] = -1
            self.participant.vars['nopleaevidence'] = -1
            self.participant.vars['nopleapun'] = -1
            self.participant.vars['pleacharge'] = -1
            self.participant.vars['pleacrimelevel'] = -1
            self.participant.vars['pleapunishment'] = -1
            self.participant.vars['pleaevidence'] = -1
            self.participant.vars['pleathreat'] = -1
            self.participant.vars['threatcharge'] = -1
        if self.participant.vars['guiltlevel'] == 2:
            if self.participant.vars['crimelevel'] == 2:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 9, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 3:
            if self.participant.vars['crimelevel'] == 2:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 8, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 4:
            if self.participant.vars['crimelevel'] == 2:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 7, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 2:
            if self.participant.vars['crimelevel'] == 3:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 6, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 3:
            if self.participant.vars['crimelevel'] == 3:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 5, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 4:
            if self.participant.vars['crimelevel'] == 3:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 4, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 2:
            if self.participant.vars['crimelevel'] == 4:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 3, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 3:
            if self.participant.vars['crimelevel'] == 4:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 2, 'threat'].item()
        if self.participant.vars['guiltlevel'] == 4:
            if self.participant.vars['crimelevel'] == 4:
                self.participant.vars['proschoice'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'choice'].item()
                self.participant.vars['nopleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'no_plea_charge'].item()
                self.participant.vars['nopleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'pros_evid_NP'].item()
                self.participant.vars['nopleapun'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'crime_pun_NP'].item()
                self.participant.vars['pleacharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'plea'].item()
                self.participant.vars['pleacrimelevel'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'crime_P'].item()
                self.participant.vars['pleapunishment'] = round(self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'pun_P'].item(), 1)
                self.participant.vars['pleaevidence'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'pros_evid_P'].item()
                self.participant.vars['pleathreat'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'threat_P'].item()
                self.participant.vars['threatcharge'] = self.session.vars['prosecutordecisions'].loc[self.session.vars['prosecutordecisions']['onetonine'] == 1, 'threat'].item()
        self.proschoice = self.participant.vars['proschoice']
        self.no_plea_charge = self.participant.vars['nopleacharge']
        self.no_plea_evidence = self.participant.vars['nopleaevidence']
        self.no_plea_pun = self.participant.vars['nopleapun']
        self.plea_charge = self.participant.vars['pleacharge']
        self.plea_crime_level = self.participant.vars['pleacrimelevel']
        self.plea_punishment = self.participant.vars['pleapunishment']
        self.plea_evidence = self.participant.vars['pleaevidence']
        self.plea_threat = self.participant.vars['pleathreat']
        self.threat_charge = self.participant.vars['threatcharge']

    def set_payoff(self):
        self.payoff = self.payoff1 + self.payoff2
        self.participant.vars['payoffmodule2'] = self.payoff
        self.payoffmodule2 = self.participant.vars['payoffmodule2']

    def record_number(self):
        self.participant.vars['thesecondone'] = [self.session.config['app_sequence'].index('criminal_theft')]