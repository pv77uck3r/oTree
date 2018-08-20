import xlrd
import os.path
from itertools import product
import numpy as np
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
    num_rounds = 18


class Subsession(BaseSubsession):

    def gen_info_sets(self):
        if self.round_number == 1:
            for p in self.get_players():

                # Generating sets of innocence: 1 is the true level of innocence, the other is from higher/lower
                # category and is purely hypothetical

                if p.participant.vars['innocencelevel'] == 1 or p.participant.vars['innocencelevel'] == 2:
                    p.alt_innocence_level = np.random.choice([3, 4])
                else:
                    p.alt_innocence_level = np.random.choice([1, 2])
                p.participant.vars['conjinnocencelevels'] = [p.participant.vars['innocencelevel'], p.alt_innocence_level]

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

                p.participant.vars['infosets'] = [p.participant.vars['conjinnocencelevels'],
                                                  p.participant.vars['conjguiltlevels'],
                                                  p.participant.vars['conjpunlevel']
                                                  ]

                # Now create all possible cartesian products of 1. innocence level, 2. guilt levels, 3. punishment
                # levels

                tupleproduct = [[w, x, y] for w in p.participant.vars['conjinnocencelevels'] for x in p.participant.vars['conjguiltlevels'] for y in p.participant.vars['conjpunlevel']]
                p.participant.vars['allpossibleinfo'] = tupleproduct


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

    plea_decision2 = plea_decision('If the monetary penalty for being found guilty at trial is between $0.40 and $0.60 '
                                   '(a Small Crime) you will')
    plea_decision3 = plea_decision('If the monetary penalty for being found guilty at trial is between $0.60 and $0.80 '
                                   '(a Medium Crime) you will')
    plea_decision4 = plea_decision('If the monetary penalty for being found guilty at trial is between $0.90 and $1.10 '
                                   '(a Medium Crime) you will')
    plea_decision5 = plea_decision('If the monetary penalty for being found guilty at trial is between $1.10 and $1.30 '
                                   '(a Large Crime) you will')
    plea_decision6 = plea_decision('If the monetary penalty for being found guilty at trial is between $1.40 and $1.60 '
                                   '(a Large Crime) you will')

    trial_decision1 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.10 and $0.30 '
                                   '(a Small Crime) you will')
    trial_decision2 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.40 and $0.60 '
                                   '(a Small Crime) you will')
    trial_decision3 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.60 and $0.80 '
                                   '(a Medium Crime) you will')
    trial_decision4 = trial_decision('If the monetary penalty for being found guilty at trial is between $0.90 and $1.10 '
                                   '(a Medium Crime) you will')
    trial_decision5 = trial_decision('If the monetary penalty for being found guilty at trial is between $1.10 and $1.30 '
                                   '(a Large Crime) you will')
    trial_decision6 = trial_decision('If the monetary penalty for being found guilty at trial is between $1.40 and $1.60 '
                                   '(a Large Crime) you will')

    alt_innocence_level = models.IntegerField()

    alt_guilt_level = models.IntegerField()

    alt_pun_level1 = models.IntegerField()

    alt_pun_level2 = models.IntegerField()

    alt_pun_level3 = models.IntegerField()

    ending_guilt = models.BooleanField()

    ending_guilt_level = models.IntegerField()

    ending_punishment = models.FloatField()

    ending_trial_status = models.BooleanField()

    # Trial status:
    # True - went to trial
    # False - took plea


    def set_payoff(self):
        # WE RECORD DECISIONS ONLY WHEN THE INNOCENCE LEVEL, GUILT LEVEL, AND PLEA MATCH THOSE SEEN BY A JURY OR PLEA
        # OFFERED BY A PROSECUTOR
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0] == self.participant.vars['innocencelevel'] and \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1] == self.participant.vars['guiltlevel'] and \
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

                    # IF THE DEFENDANT GOES TO TRIAL WITH THEIR INNOCENCE LEVEL PROVIDED, INDICATED BY A 2, THEN WE
                    # GATHER THE THE THREATENED CRIME LEVEL (FROM PROSECUTOR), THREATENED EVIDENCE LEVEL (FROM
                    # PROSECUTOR), AND THE INNOCENCE LEVEL (FROM DEFENDANT) AND FIND THE APPROPRIATE ROW IN THE JURY
                    # DECISION TABLE, AND SIMULATE A TRIAL.

                    if self.participant.vars['relevantdecision'] == 2:
                        self.ending_trial_status = True
                        if self.participant.vars['pleathreat'] == 1:
                            trialcrime = 1
                            trialdefevid = self.participant.vars['innocencelevel']
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 2:
                            trialcrime = 2
                            trialdefevid = self.participant.vars['innocencelevel']
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 3:
                            trialcrime = 2
                            trialdefevid = self.participant.vars['innocencelevel']
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 4:
                            trialcrime = 3
                            trialdefevid = self.participant.vars['innocencelevel']
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 5:
                            trialcrime = 3
                            trialdefevid = self.participant.vars['innocencelevel']
                            trialprosevid = self.participant.vars['pleaevidence']

                        # HERE WE ACTUALLY SIMULATE THE GUILTY/NOT GUILTY FINDING FROM THE JURY TABLE

                        self.participant.vars['jurydecision'] = np.random.binomial(1, (self.session.vars['juryprobs'].loc[self.session.vars['juryprobs']['Crime'] == trialcrime & self.session.vars['juryprobs']['Defense evidence'] == trialdefevid & self.session.vars['juryprobs']['Prosecutor evidence'] == trialprosevid, 'Probability of a guilty findng at trial'].item()))

                        # IF JURY DECIDES NOT GUILTY, INDICATED BY A 0, THEN NO PUNISHMENT

                        if self.participant.vars['jurydecision'] == 0:
                            self.payoff = 0
                            self.ending_guilt = False
                            self.ending_guilt_level = 0
                            self.ending_punishment = 0

                        # IF JURY DECIDES GUILTY, THEN WE LOOK AT THE RELEVANT THREAT LEVEL AND GENERATE A PUNISHMENT

                        else:
                            self.ending_guilt = True
                            if self.participant.vars['pleathreat'] == 1:
                                self.payoff = -np.random.choice([.1, .2, .3])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 1
                            if self.participant.vars['pleathreat'] == 2:
                                self.payoff = -np.random.choice([.4, .5, .6])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 1
                            if self.participant.vars['pleathreat'] == 3:
                                self.payoff = -np.random.choice([.6, .7, .8])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 2
                            if self.participant.vars['pleathreat'] == 4:
                                self.payoff = -np.random.choice([.9, 1, 1.1])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 2
                            if self.participant.vars['pleathreat'] == 5:
                                self.payoff = -np.random.choice([1.1, 1.2, 1.3])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 3

                    # WE DO SOMETHING VERY SIMILAR FOR WHEN THE DEFENDANT DECIDES TO PLEA THE FIFTH, INDICATED BY A 3

                    if self.participant.vars['relevantdecision'] == 3:
                        self.ending_trial_status = True
                        if self.participant.vars['pleathreat'] == 1:
                            trialcrime = 1
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 2:
                            trialcrime = 2
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 3:
                            trialcrime = 2
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 4:
                            trialcrime = 3
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                        if self.participant.vars['pleathreat'] == 5:
                            trialcrime = 3
                            trialdefevid = 0
                            trialprosevid = self.participant.vars['pleaevidence']
                        self.participant.vars['jurydecision'] = np.random.binomial(1, (self.session.vars['juryprobs'].loc[self.session.vars['juryprobs']['Crime'] == trialcrime & self.session.vars['juryprobs']['Defense evidence'] == trialdefevid & self.session.vars['juryprobs']['Prosecutor evidence'] == trialprosevid, 'Probability of a guilty findng at trial'].item()))

                        if self.participant.vars['jurydecision'] == 0:
                            self.payoff = 0
                            self.ending_guilt = False
                            self.ending_guilt_level = 0
                            self.ending_punishment = 0
                        else:
                            self.ending_guilt = True
                            if self.participant.vars['pleathreat'] == 1:
                                self.payoff = -np.random.choice([.1, .2, .3])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 1
                            if self.participant.vars['pleathreat'] == 2:
                                self.payoff = -np.random.choice([.4, .5, .6])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 1
                            if self.participant.vars['pleathreat'] == 3:
                                self.payoff = -np.random.choice([.6, .7, .8])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 2
                            if self.participant.vars['pleathreat'] == 4:
                                self.payoff = -np.random.choice([.9, 1, 1.1])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 2
                            if self.participant.vars['pleathreat'] == 5:
                                self.payoff = -np.random.choice([1.1, 1.2, 1.3])
                                self.ending_punishment = self.payoff
                                self.ending_guilt_level = 3

        # NEXT WE CONSIDER WHEN THEIR IS NO PLEA OFFER AND THE PROSECUTOR GOES STRAIGHT TO TRIAL. THIS IS ALL VERY
        # SIMILAR TO WHAT IS DONE ABOVE WHEN THE DEFENDANT WANTS TO GO TO TRIAL AGAINST A THREAT

        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0] == self.participant.vars['innocencelevel'] and \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1] == self.participant.vars['guiltlevel']:
            if self.participant.vars['proschoice'] == 2:
                self.ending_trial_status = True
                if self.participant.vars['nopleapun'] == 1:
                    self.participant.vars['relevantdecision'] = self.trial_decision1
                    trialcrime = 1
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel']
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 2:
                    self.participant.vars['relevantdecision'] = self.trial_decision2
                    trialcrime = 1
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel']
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 3:
                    self.participant.vars['relevantdecision'] = self.trial_decision3
                    trialcrime = 2
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel']
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 4:
                    self.participant.vars['relevantdecision'] = self.trial_decision4
                    trialcrime = 2
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel']
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 5:
                    self.participant.vars['relevantdecision'] = self.trial_decision5
                    trialcrime = 3
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel']
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                if self.participant.vars['nopleapun'] == 6:
                    self.participant.vars['relevantdecision'] = self.trial_decision6
                    trialcrime = 3
                    if self.participant.vars['relevantdecision'] == 1:
                        trialdefevid = self.participant.vars['innocencelevel']
                    else:
                        trialdefevid = 0
                    trialprosevid = self.participant.vars['nopleaevidence']
                self.participant.vars['jurydecision'] = np.random.binomial(1, (self.session.vars['juryprobs'].loc[self.session.vars['juryprobs']['Crime'] == trialcrime & self.session.vars['juryprobs']['Defense evidence'] == trialdefevid & self.session.vars['juryprobs']['Prosecutor evidence'] == trialprosevid, 'Probability of a guilty findng at trial'].item()))
                if self.participant.vars['jurydecision'] == 0:
                    self.payoff = 0
                    self.ending_guilt = False
                    self.ending_guilt_level = 0
                    self.ending_punishment = 0
                else:
                    self.ending_guilt = True
                    if self.participant.vars['nopleapun'] == 1:
                        self.payoff = -np.random.choice([.1, .2, .3])
                        self.ending_punishment = self.payoff
                        self.ending_guilt_level = 1
                    if self.participant.vars['nopleapun'] == 2:
                        self.payoff = -np.random.choice([.4, .5, .6])
                        self.ending_punishment = self.payoff
                        self.ending_guilt_level = 1
                    if self.participant.vars['nopleapun'] == 3:
                        self.payoff = -np.random.choice([.6, .7, .8])
                        self.ending_punishment = self.payoff
                        self.ending_guilt_level = 2
                    if self.participant.vars['nopleapun'] == 4:
                        self.payoff = -np.random.choice([.9, 1, 1.1])
                        self.ending_punishment = self.payoff
                        self.ending_guilt_level = 2
                    if self.participant.vars['nopleapun'] == 5:
                        self.payoff = -np.random.choice([1.1, 1.2, 1.3])
                        self.ending_punishment = self.payoff
                        self.ending_guilt_level = 3
                    if self.participant.vars['nopleapun'] == 6:
                        self.payoff = -np.random.choice([1.4, 1.5, 1.6])
                        self.ending_punishment = self.payoff
                        self.ending_guilt_level = 3
            if self.participant.vars['proschoice'] == 1:
                self.ending_trial_status = False
                self.ending_guilt_level = False
                self.payoff = 0
                self.ending_guilt_level = 0
                self.ending_punishment = 0

        # Record this decision so it can be displayed on final page

        self.participant.vars['payoffmodule3'] = self.payoff

            # THINGS RECORDED:
            # payoff - the resulting punishment, if anything
            # ending_guilt_level - what level of crime they were determined to have committed, if any
            # ending_punishment - same thing as payoff in this module


