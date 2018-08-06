import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


def shift_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst


author = 'Jason Ralston'

doc = """
A simple program that sets groups of arbitrary size. also displays a welcome screen.
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_wrapper'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            list = self.get_players()
            oddsubjlist = list[0:][::2]
            evensubjlist = list[1:][::2]
            size = len(evensubjlist)
            for i in range(1, size):
                evensubjlist = shift_right(evensubjlist)
            evensubjlist1 = evensubjlist
            evensubjlist2 = shift_right(evensubjlist1)
            evensubjlist3 = shift_right(evensubjlist2)
            evensubjlist4 = shift_right(evensubjlist3)
            newsubjlist1 = []
            newsubjlist2 = []
            newsubjlist3 = []
            newsubjlist4 = []
            for i in range(1, size + 1):
                newsubjlist1.append(oddsubjlist[i - 1])
                newsubjlist1.append(evensubjlist1[i - 1])
                newsubjlist2.append(oddsubjlist[i - 1])
                newsubjlist2.append(evensubjlist2[i - 1])
                newsubjlist3.append(evensubjlist3[i - 1])
                newsubjlist3.append(oddsubjlist[i - 1])
                newsubjlist4.append(oddsubjlist[i - 1])
                newsubjlist4.append(evensubjlist4[i - 1])
            grouplist1 = [newsubjlist1[i * Constants.players_per_group:(i + 1) * Constants.players_per_group] for i in range((len(newsubjlist1) + Constants.players_per_group - 1) // Constants.players_per_group)]
            grouplist2 = [newsubjlist2[i * Constants.players_per_group:(i + 1) * Constants.players_per_group] for i in range((len(newsubjlist2) + Constants.players_per_group - 1) // Constants.players_per_group)]
            grouplist3 = [newsubjlist3[i * Constants.players_per_group:(i + 1) * Constants.players_per_group] for i in range((len(newsubjlist3) + Constants.players_per_group - 1) // Constants.players_per_group)]
            grouplist4 = [newsubjlist4[i * Constants.players_per_group:(i + 1) * Constants.players_per_group] for i in range((len(newsubjlist4) + Constants.players_per_group - 1) // Constants.players_per_group)]
            listofsubjlists = [grouplist1, grouplist2, grouplist3, grouplist4]
            self.session.vars['subjlists'] = listofsubjlists

            # The following code must be modified whe I get a usable list of prosecutors and their decisions over
            # the different levels of evidence.

            # Here there will be an import function where we import an excel table of prosecutors and their decisions
            # We will be able to search the table to find prosecutors decisions under various conditions
            # in the criminal_plea game, we will use this table to match the representative prosecutors decisions with
            # the levels of evidence generated from the decisions of each subject in criminal_theft.

            # Below we import jury decisions.
            self.session.vars['juryprobs'] = pd.read_excel('GuiltyProbs_jr_08022018.xlsx', 'Sheet1')


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
