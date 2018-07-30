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

def trial_decision(label):
    return models.IntegerField(
        choices=[
            [1, 'Go to trial and present your evidence of innocence'],
            [2, 'Go to trial and exercise right to not present your evidence of innocence']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

class Constants(BaseConstants):
    name_in_url = 'criminal_plea'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    quiz1 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='If you accept a plea bargain you are not contesting your guilt (in other words you are not claiming '
              'innocence)'
    )

    quiz2 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'True'],
            [2, 'False']
        ],
        label='If you accept a plea bargain or are found guilty at the experimental trial, then the monetary penalty '
              'will reduce your experimental payment today.'
    )

    quiz3 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'The prosecutor has to present the evidence of guilt you see in the plea bargain trial threat'],
            [2, 'You have to present your evidence of innocence'],
            [3, 'There is no monetary penalty if you are found guilty']
        ],
        label='At trial, which of the following is true?'
    )

    plea_decision1 = plea_decision('If the monetary penalty for being found guilty at trial is between $0.40 and $0.60 '
                                   '(a Small Crime) you will')
    plea_decision2 = plea_decision('If the monetary penalty for being found guilty at trial is between $0.60 and $0.80 '
                                   '(a Medium Crime) you will')
    plea_decision3 = plea_decision('If the monetary penalty for being found guilty at trial is between $0.90 and $1.10 '
                                   '(a Medium Crime) you will')
    plea_decision4 = plea_decision('If the monetary penalty for being found guilty at trial is between $1.10 and $1.30 '
                                   '(a Large Crime) you will')
    plea_decision5 = plea_decision('If the monetary penalty for being found guilty at trial is between $1.40 and $1.60 '
                                   '(a Large Crime) you will')

    trial_decision1 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.40 and $0.60 '
                                   '(a Small Crime) you will')
    trial_decision2 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.60 and $0.80 '
                                   '(a Medium Crime) you will')
    trial_decision3 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.90 and $1.10 '
                                   '(a Medium Crime) you will')
    trial_decision4 = trial_decision('If the monetary penalty for being found guilty at trial is between $1.10 and $1.30 '
                                   '(a Large Crime) you will')
    trial_decision5 = trial_decision('If the monetary penalty for being found guilty at trial is between $1.40 and $1.60 '
                                   '(a Large Crime) you will')
