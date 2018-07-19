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
        if self.round_number == 1:
            W = 


class Group(BaseGroup):
    pass


class Player(BasePlayer):


