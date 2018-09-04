from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jason Ralston'

doc = """
Variant of trust game
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_trust_2'
    players_per_group = 2
    num_rounds = 1

    endowment = 10
    multiplier = 3


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            self.set_group_matrix(self.session.vars['subjlists'][0])


class Group(BaseGroup):
    #################INVESTOR DECISIONS#####################
    investor_decision1 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS NEVER ACCUSED of taking a small, "
                                                  "medium, or large amount of money that belonged to another "
                                                  "participant?  Anything you send to them will be tripled by the "
                                                  "experimenter and they can send back to you between 0 and that tripled"
                                                  " number of quarters.")

    investor_decision2 = models.IntegerField(min=0, max=10,
                                             choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                             widget=widgets.RadioSelectHorizontal,
                                             label="How many of your initial 10 quarters will you send to your "
                                                   "counterpart if your counterpart WAS ACCUSED but FOUND NOT-GUILTY of "
                                                   "taking a small, medium, or large amount of money that belonged to "
                                                   "another participant?  Anything you send to them will be tripled by "
                                                   "the experimenter and they can send back to you between 0 and that "
                                                   "tripled number of quarters.")

    investor_decision3 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS FOUND GUILTY of taking a SMALL "
                                                  "amount of money that belonged to another participant?  Anything you "
                                                  "send to them will be tripled by the experimenter and they can send "
                                                  "back to you between 0 and that tripled number of quarters.")

    investor_decision4 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS FOUND GUILTY of taking a MEDIUM "
                                                  "amount of money that belonged to another participant?  Anything you "
                                                  "send to them will be tripled by the experimenter and they can send "
                                                  "back to you between 0 and that tripled number of quarters.")

    investor_decision5 = models.IntegerField(min=0, max=10,
                                            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            widget=widgets.RadioSelectHorizontal,
                                            label="How many of your initial 10 quarters will you send to your "
                                                  "counterpart if your counterpart WAS FOUND GUILTY of taking a LARGE "
                                                  "amount of money that belonged to another participant?  Anything you "
                                                  "send to them will be tripled by the experimenter and they can send "
                                                  "back to you between 0 and that tripled number of quarters.")

    #################TRUSTEE DECISIONS#######################
    trustee_decision1 = models.IntegerField(min=0, max=3,
                                            label="If your counterpart sends you 1 quarter (tripled into 3 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 3)")

    trustee_decision2 = models.IntegerField(min=0, max=6,
                                            label="If your counterpart sends you 2 quarters (tripled into 6 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 6)")

    trustee_decision3 = models.IntegerField(min=0, max=9,
                                            label="If your counterpart sends you 3 quarters (tripled into 9 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 9)")

    trustee_decision4 = models.IntegerField(min=0, max=12,
                                            label="If your counterpart sends you 4 quarters (tripled into 12 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 12)")

    trustee_decision5 = models.IntegerField(min=0, max=15,
                                            label="If your counterpart sends you 5 quarters (tripled into 15 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 15)")

    trustee_decision6 = models.IntegerField(min=0, max=18,
                                            label="If your counterpart sends you 6 quarters (tripled into 18 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 18)")

    trustee_decision7 = models.IntegerField(min=0, max=21,
                                            label="If your counterpart sends you 7 quarters (tripled into 21 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 21)")

    trustee_decision8 = models.IntegerField(min=0, max=24,
                                            label="If your counterpart sends you 8 quarters (tripled into 24 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 24)")

    trustee_decision9 = models.IntegerField(min=0, max=27,
                                            label="If your counterpart sends you 9 quarters (tripled into 27 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 27)")

    trustee_decision10 = models.IntegerField(min=0, max=30,
                                            label="If your counterpart sends you 10 quarters (tripled into 30 quarters), "
                                                  "how many quarters will you send back to them? (Enter a number "
                                                  "between 0 and 30)")

    def keep_decisions(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.participant.vars['investor_decision1'] = self.investor_decision1
        p1.participant.vars['investor_decision2'] = self.investor_decision2
        p1.participant.vars['investor_decision3'] = self.investor_decision3
        p1.participant.vars['investor_decision4'] = self.investor_decision4
        p1.participant.vars['investor_decision5'] = self.investor_decision5
        p1.participant.vars['initial_role'] = p1.role

        p2.participant.vars['trustee_decision1'] = self.trustee_decision1
        p2.participant.vars['trustee_decision2'] = self.trustee_decision2
        p2.participant.vars['trustee_decision3'] = self.trustee_decision3
        p2.participant.vars['trustee_decision4'] = self.trustee_decision4
        p2.participant.vars['trustee_decision5'] = self.trustee_decision5
        p2.participant.vars['trustee_decision6'] = self.trustee_decision6
        p2.participant.vars['trustee_decision7'] = self.trustee_decision7
        p2.participant.vars['trustee_decision8'] = self.trustee_decision8
        p2.participant.vars['trustee_decision9'] = self.trustee_decision9
        p2.participant.vars['trustee_decision10'] = self.trustee_decision10
        p2.participant.vars['initial_role'] = p2.role


class Player(BasePlayer):

    investor_quiz1 = models.IntegerField(
        choices=[
            [1, '(a) You each start with 5.'],
            [2, '(b) You start with 10 and your counterpart starts with 0.'],
            [3, '(c) Your counterpart starts with 10 and you start with 0.'],
            [4, '(d) You each start with 10.']
        ],
        widget=widgets.RadioSelect,
        label="Question 1: How many quarters do you and your counterpart start with in this part of the experiment?"
    )

    investor_quiz2 = models.IntegerField(
        choices=[
            [1, '(a) It will triple to 12 quarters before reaching them.'],
            [2, '(b) It will double to 8 quarters before reaching them.'],
            [3, '(c) They will receive 4 quarters.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 2: If you send your counterpart 4 quarters "
    )

    investor_quiz3 = models.IntegerField(
        choices=[
            [1, '(a) Will be tripled before reaching you.'],
            [2, '(b) Will be doubled before reaching you.'],
            [3, '(c) Will not be multiplied before reaching you.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 3: Any quarters your counterpart returns to you "
    )

    investor_quiz4 = models.IntegerField(
        choices=[
            [1, '(a) All participants you could interact with in this part of the experiment are guaranteed to have '
                'taken money from others previously.'],
            [2, '(b) Some participants who were truly innocent may have been found guilty of taking money from another '
                'subject.'],
            [3, '(c) Participants who were found guilty of taking money from another participant faced no monetary '
                'penalty from their guilty finding.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 4: Which of the following is true "
    )

    trustee_quiz1 = models.IntegerField(
        choices=[
            [1, '(a) You each start with 5.'],
            [2, '(b) You start with 10 and your counterpart starts with 0.'],
            [3, '(c) Your counterpart starts with 10 and you start with 0.'],
            [4, '(d) You each start with 10.']
        ],
        widget=widgets.RadioSelect,
        label="Question 1: How many quarters do you and your counterpart start with? "
    )

    trustee_quiz2 = models.IntegerField(
        choices=[
            [1, '(a) It will triple to 12 quarters before reaching you.'],
            [2, '(b) It will double to 8 quarters before reaching you.'],
            [3, '(c) You will receive 4 quarters.']
        ],
        widget=widgets.RadioSelect,
        label="Question 2: If your counterpart sends you 4 quarters "
    )

    trustee_quiz3 = models.IntegerField(
        choices=[
            [1, '(a) Will be tripled before reaching them.'],
            [2, '(b) Will be doubled before reaching them.'],
            [3, '(c) Will not be multiplied before reaching them.']
        ],
        widget=widgets.RadioSelect,
        label="Question 3: Any quarters you return to your counterpart "
    )

    def role(self):
        if self.id_in_group == 1:
            self.participant.vars['firstrole'] = 'Investor'
            return 'Investor'
        if self.id_in_group == 2:
            self.participant.vars['firstrole'] = 'Trustee'
            return 'Trustee'
