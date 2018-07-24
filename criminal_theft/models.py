import numpy as np
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_theft'
    players_per_group = 2
    num_rounds = 10


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()
        # Wdraws = [None]*len(self.get_players())
        # xdraws = [None]*len(self.get_players())
        # ydraws = [None]*len(self.get_players())
        # zdraws = [None]*len(self.get_players())
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['Wdraws'] = np.random.choice(np.arange(3.90, 7.00, 0.10), 10, replace=False)
                p.participant.vars['xdraws'] = np.random.choice(np.arange(0.10, 1.10, 0.10), 10, replace=False)
                p.participant.vars['ydraws'] = np.random.choice(np.arange(1.00, 2.10, 0.10), 10, replace=False)
                p.participant.vars['zdraws'] = np.random.choice(np.arange(2.00, 3.10, 0.10), 10, replace=False)


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

    ThiefChoice = models.IntegerField(
        widget=widgets.RadioSelect,
        label='Please Report the Division'
    )


class Player(BasePlayer):

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

