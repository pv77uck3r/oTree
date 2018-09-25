import random, math, statistics, itertools
import numpy as np

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""

# def rank_simple(vector):
#     return sorted(range(len(vector)), key=vector.__getitem__)
#
# def rankdata(a):
#     n = len(a)
#     ivec=rank_simple(a)
#     svec=[a[rank] for rank in ivec]
#     sumranks = 0
#     dupcount = 0
#     newarray = [0]*n
#     for i in range(n):
#         sumranks += i
#         dupcount += 1
#         if i==n-1 or svec[i] != svec[i+1]:
#             averank = sumranks / float(dupcount) + 1
#             for j in range(i-dupcount+1,i+1):
#                 newarray[ivec[j]] = averank
#             sumranks = 0
#             dupcount = 0
#     return newarray

class Constants(BaseConstants):
    name_in_url = 'Innovate_vs_Imitate'
    players_per_group = None
    num_players = 10
    num_rounds = 10*num_players

    trianglea = 0
    triangleb = 100
    trianglemode = 50

    endowment = 10


class Subsession(BaseSubsession):

    modeheight = models.FloatField(initial=2 / (Constants.triangleb - Constants.trianglea))
    trianglea = models.FloatField(initial=Constants.trianglea)
    triangleb = models.FloatField(initial=Constants.triangleb)
    trianglemode = models.FloatField(initial=Constants.trianglemode)
    NewHighDrawIndicator = models.IntegerField()
    StepCounter = models.IntegerField(initial=0)



    def UpdateModeHeight(self):
        if self.round_number > 1:
            self.trianglemode = self.in_round(self.round_number - 1).trianglemode + 0.5 * self.StepCounter
        self.modeheight = 2/(self.triangleb - self.trianglea) + 0.5*self.StepCounter
        if self.round_number > 1:
            self.triangleb = self.in_round(self.round_number-1).triangleb + 0.5*self.StepCounter


    def creating_session(self):
        if self.round_number == 1:
            randomchoice = np.random.choice(range(1,Constants.num_players+1), Constants.num_players, replace=False)
            self.session.vars['randomchoice'] = randomchoice
            randomchoice2 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players, replace=False)
            self.session.vars['randomchoice2'] = randomchoice2
            randomchoice3 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice3'] = randomchoice3
            randomchoice4 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice4'] = randomchoice4
            randomchoice5 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice5'] = randomchoice5
            randomchoice6 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice6'] = randomchoice6
            randomchoice7 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice7'] = randomchoice7
            randomchoice8 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice8'] = randomchoice8
            randomchoice9 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice9'] = randomchoice9
            randomchoice10 = np.random.choice(range(1, Constants.num_players + 1), Constants.num_players,replace=False)
            self.session.vars['randomchoice10'] = randomchoice10
            randomroll = np.random.uniform(0, 1, Constants.num_players+1)
            self.session.vars['randomroll'] = randomroll
            randomroll2 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll2'] = randomroll2
            randomroll3 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll3'] = randomroll3
            randomroll4 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll4'] = randomroll4
            randomroll5 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll5'] = randomroll5
            randomroll6 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll6'] = randomroll6
            randomroll7 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll7'] = randomroll7
            randomroll8 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll8'] = randomroll8
            randomroll9 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll9'] = randomroll9
            randomroll10 = np.random.uniform(0, 1, Constants.num_players + 1)
            self.session.vars['randomroll10'] = randomroll10
            self.session.vars['randompayround'] = np.random.choice(range(1, Constants.num_players + 1))
            self.session.vars['endowment'] = 7
            self.session.vars['conversionrate'] = .15


    HighDraw = models.FloatField(initial=0)
    OldHighDraw = models.FloatField(initial=0)

    SuperRound = models.IntegerField(initial=1)

    def UpdateHighDraw(self):
        self.Draws = [p.Draw for p in self.get_players()]
        self.HighDraw = max(self.Draws)
        if (self.round_number - 1) % Constants.num_players + 1 == Constants.num_players:
            self.HighDraw = 0

    def HighDrawLastPeriod(self):
        if self.round_number >= 2:
            if (self.round_number - 1)%Constants.num_players + 1 == 1:
                self.SuperRound = self.in_round(self.round_number - 1).SuperRound + 1
            else:
                self.SuperRound = self.in_round(self.round_number - 1).SuperRound
        if self.round_number >= 2:
            self.OldHighDraw = round(self.in_round(self.round_number - 1).HighDraw, 2)

    def NewHighDrawIndicatorUpdate(self):
        if self.round_number > 1:
            if self.HighDraw > self.OldHighDraw:
                self.NewHighDrawIndicator = 1
            else:
                self.NewHighDrawIndicator = 0

    def IncreaseStepCounter(self):
        if self.NewHighDrawIndicator == 1:
            self.StepCounter = self.in_round(self.round_number-1).StepCounter + 1
        else:
            self.StepCounter = self.in_round(self.round_number-1).StepCounter

class Group(BaseGroup):
    pass



class Player(BasePlayer):

    Innovate = models.BooleanField(
        widget=widgets.CheckboxInput,
        blank=True
    )

    NoInnovate = models.BooleanField(
        widget=widgets.CheckboxInput,
        blank=True
    )

    InnovateorImitateButton = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        min=0,
        max=100,
        blank=True
    )

    Draw = models.FloatField(initial=0)
    payout = models.FloatField(initial=0)

    def InnovateRoll(self):
        if self.Innovate == True:
            self.InnovateorImitateButton = 100
        if self.NoInnovate == True:
            self.InnovateorImitateButton = 0
        if (self.subsession.SuperRound == 1 and self.InnovateorImitateButton >= self.session.vars['randomroll'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 2 and self.InnovateorImitateButton >= self.session.vars['randomroll2'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 3 and self.InnovateorImitateButton >= self.session.vars['randomroll3'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 4 and self.InnovateorImitateButton >= self.session.vars['randomroll4'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 5 and self.InnovateorImitateButton >= self.session.vars['randomroll5'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 6 and self.InnovateorImitateButton >= self.session.vars['randomroll6'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 7 and self.InnovateorImitateButton >= self.session.vars['randomroll7'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 8 and self.InnovateorImitateButton >= self.session.vars['randomroll8'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 9 and self.InnovateorImitateButton >= self.session.vars['randomroll9'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 10 and self.InnovateorImitateButton >= self.session.vars['randomroll10'][(self.subsession.round_number - 1)%Constants.num_players]*100):
            self.Draw = round(np.random.triangular(self.subsession.trianglea,self.subsession.trianglemode,self.subsession.triangleb),2)
        else:
            self.Draw = round(self.subsession.OldHighDraw,2)

    def setpayoff(self):
        if self.Innovate == True:
            self.InnovateorImitateButton = 100
        if self.NoInnovate == True:
            self.InnovateorImitateButton = 0
        if (self.subsession.SuperRound == 1 and self.InnovateorImitateButton >= self.session.vars['randomroll'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 2 and self.InnovateorImitateButton >= self.session.vars['randomroll2'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 3 and self.InnovateorImitateButton >= self.session.vars['randomroll3'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 4 and self.InnovateorImitateButton >= self.session.vars['randomroll4'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 5 and self.InnovateorImitateButton >= self.session.vars['randomroll5'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 6 and self.InnovateorImitateButton >= self.session.vars['randomroll6'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 7 and self.InnovateorImitateButton >= self.session.vars['randomroll7'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 8 and self.InnovateorImitateButton >= self.session.vars['randomroll8'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 9 and self.InnovateorImitateButton >= self.session.vars['randomroll9'][(self.subsession.round_number - 1)%Constants.num_players]*100)\
                or (self.subsession.SuperRound == 10 and self.InnovateorImitateButton >= self.session.vars['randomroll10'][(self.subsession.round_number - 1)%Constants.num_players]*100):
            self.payout = round(self.Draw,2)
        if (self.subsession.SuperRound == 1 and self.InnovateorImitateButton < self.session.vars['randomroll'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 2 and self.InnovateorImitateButton < self.session.vars['randomroll2'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 3 and self.InnovateorImitateButton < self.session.vars['randomroll3'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 4 and self.InnovateorImitateButton < self.session.vars['randomroll4'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 5 and self.InnovateorImitateButton < self.session.vars['randomroll5'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 6 and self.InnovateorImitateButton < self.session.vars['randomroll6'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 7 and self.InnovateorImitateButton < self.session.vars['randomroll7'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 8 and self.InnovateorImitateButton < self.session.vars['randomroll8'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 9 and self.InnovateorImitateButton < self.session.vars['randomroll9'][(self.subsession.round_number - 1) % Constants.num_players] * 100) \
                or (self.subsession.SuperRound == 10 and self.InnovateorImitateButton < self.session.vars['randomroll10'][(self.subsession.round_number - 1) % Constants.num_players] * 100):
            self.payout = round(self.Draw,2) + Constants.endowment
        if self.subsession.SuperRound == self.session.vars['randompayround']:
            self.participant.vars['ExpEarnings'] = self.payout

    def retainDraws(self):
        if (self.subsession.round_number - 1)%Constants.num_players + 1 == 1:
            self.Draw = 0
        else:
            self.Draw = self.in_round((self.subsession.round_number - 1)).Draw

    def retainPayoffs(self):
        if (self.subsession.round_number - 1)%Constants.num_players + 1 == 1:
            self.payout = 0
        else:
            self.payout = self.in_round((self.subsession.round_number - 1)).payout