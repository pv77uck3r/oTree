from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_beliefs'
    players_per_group = None
    num_rounds = 18


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    belief = models.FloatField(
        min=0,
        max=100,
        widget=widgets.Slider(attrs={'step': '1.0'}),
        label=None
    )

    GuiltEv = models.IntegerField()
    InnocenceEv = models.IntegerField()
    CrimeLevel = models.IntegerField()
