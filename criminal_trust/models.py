from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_trust'
    players_per_group = 2
    num_rounds = 1

    endowment = 10
    multiplier = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    investor_decision = models.IntegerField(min=0, max=10,
                                            choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal)


class Player(BasePlayer):
    pass
