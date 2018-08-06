import numpy as np
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

    def creating_session(self):
        self.group_randomly()
        # Wdraws = [None]*len(self.get_players())
        # xdraws = [None]*len(self.get_players())
        # ydraws = [None]*len(self.get_players())
        # zdraws = [None]*len(self.get_players())
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['Wdraws'] = np.random.choice(np.arange(3.90, 7.00, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['xdraws'] = np.random.choice(np.arange(0.10, 1.10, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['ydraws'] = np.random.choice(np.arange(1.00, 2.10, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['zdraws'] = np.random.choice(np.arange(2.00, 3.10, 0.10), Constants.numdraws, replace=False)
                p.participant.vars['randround'] = np.random.choice(range(1, 11))


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


class Group(BaseGroup):
    kept = models.FloatField()

    def group_decisions(self):
        self.subsession.set_group_matrix(self.session.vars['subjlists'][1])
        for p in self.get_players():
            if p.id_in_group == 1:
                if p.participant.vars['theftchoice'] == 1:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number]
                if p.participant.vars['theftchoice'] == 2:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number] + p.participant.vars['xdraws'][self.subsession.round_number]
                if p.participant.vars['theftchoice'] == 3:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number] + p.participant.vars['ydraws'][self.subsession.round_number]
                if p.participant.vars['theftchoice'] == 4:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number] + p.participant.vars['zdraws'][self.subsession.round_number]
                p.payoff1 = self.kept
            if p.id_in_group == 2:
                p.payoff1 = 10 - self.kept
        self.subsession.set_group_matrix(self.session.vars['subjlists'][2])
        for p in self.get_players():
            if p.id_in_group == 1:
                if p.participant.vars['theftchoice'] == 1:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number]
                if p.participant.vars['theftchoice'] == 2:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number] + \
                                p.participant.vars['xdraws'][self.subsession.round_number]
                if p.participant.vars['theftchoice'] == 3:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number] + \
                                p.participant.vars['ydraws'][self.subsession.round_number]
                if p.participant.vars['theftchoice'] == 4:
                    self.kept = p.participant.vars['Wdraws'][self.subsession.round_number] + \
                                p.participant.vars['zdraws'][self.subsession.round_number]
                p.payoff2 = self.kept
            if p.id_in_group == 2:
                p.payoff2 = 10 - self.kept
        for p in self.subsession.get_players():
            p.set_payoff()

class Player(BasePlayer):

    payoff1 = models.FloatField()
    payoff2 = models.FloatField()

    quiz1 = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='If you report the division of money accurately it is impossible for there to be evidence suggesting you '
              'are guilty.'
    )

    quiz2 = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='If you report the division of money inaccurately (and take some of your counterpart\'s money), there is '
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

    def record_choice(self):

        # LEVELS OF EVIDENCE CODING:
        # 1 - no evidence of ______
        # 2 - small evidence of ______
        # 3 - medium evidence of ______
        # 4 - large evidence of ______

        for p in self.get_players():
            if self.subsession.round_number == p.participant.vars['randround']:
                p.participant.vars['theftchoice'] = self.ThiefChoice
                if self.ThiefChoice == 1:
                    p.participant.vars['amountstolen'] = 0
                if self.ThiefChoice == 2:
                    p.participant.vars['amountstolen'] = p.participant.vars['xdraws'][self.subsession.round_number - 1]
                if self.ThiefChoice == 3:
                    p.participant.vars['amountstolen'] = p.participant.vars['ydraws'][self.subsession.round_number - 1]
                if self.ThiefChoice == 4:
                    p.participant.vars['amountstolen'] = p.participant.vars['zdraws'][self.subsession.round_number - 1]
                if self.participant.vars['amountstolen'] == 0:
                    p.participant.vars['trulyinnocent'] = True
                    p.participant.vars['innocencelevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.2, .4, .25, .15])
                    p.participant.vars['guiltlevel'] = np.random.choice([1, 2, 3 , 4], 1, replace=False, p=[.7, .15, .1, .05])
                else:
                    p.participant.vars['trulyinnocent'] = False
                    p.participant.vars['innocencelevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.7, .15, .1, .05])
                    p.participant.vars['guiltlevel'] = np.random.choice([1, 2, 3, 4], 1, replace=False, p=[.3, .3, .25, .15])

    def set_payoff(self):
        self.payoff = self.payoff1 + self.payoff2