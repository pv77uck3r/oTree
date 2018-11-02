from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_VCM'
    players_per_group = 3
    num_rounds = 1

    multiplier = 0.5
    endowment = 10

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        self.session.vars['module1groupmatrix'] = self.get_group_matrix()


class Group(BaseGroup):

    totalcontribution1 = models.IntegerField()

    totalcontribution2 = models.IntegerField()

    totalcontribution3 = models.IntegerField()

    totalcontribution4 = models.IntegerField()

    totalcontribution5 = models.IntegerField()

    totalcontribution6 = models.IntegerField()

    individualshare1 = models.FloatField()

    individualshare2 = models.FloatField()

    individualshare3 = models.FloatField()

    individualshare4 = models.FloatField()

    individualshare5 = models.FloatField()

    individualshare6 = models.FloatField()

    def sum_and_store(self):
        players = self.get_players()

        ## We use the same local variable (contributions) to sum for each condition and calculate individual shares ##

        contributions = [p.contribution1 for p in players]
        self.total_contribution1 = sum(contributions)
        self.individual_share1 = self.total_contribution1 * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.participant.vars['VCMPayoff1'] = Constants.endowment - p.contribution1 + self.individual_share1

        contributions = [p.contribution2 for p in players]
        self.total_contribution2 = sum(contributions)
        self.individual_share2 = self.total_contribution2 * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.participant.vars['VCMPayoff2'] = Constants.endowment - p.contribution2 + self.individual_share2

        contributions = [p.contribution3 for p in players]
        self.total_contribution3 = sum(contributions)
        self.individual_share3 = self.total_contribution3 * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.participant.vars['VCMPayoff3'] = Constants.endowment - p.contribution3 + self.individual_share3

        contributions = [p.contribution4 for p in players]
        self.total_contribution4 = sum(contributions)
        self.individual_share4 = self.total_contribution4 * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.participant.vars['VCMPayoff4'] = Constants.endowment - p.contribution4 + self.individual_share4

        contributions = [p.contribution5 for p in players]
        self.total_contribution5 = sum(contributions)
        self.individual_share5 = self.total_contribution5 * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.participant.vars['VCMPayoff5'] = Constants.endowment - p.contribution5 + self.individual_share5

        contributions = [p.contribution6 for p in players]
        self.total_contribution6 = sum(contributions)
        self.individual_share6 = self.total_contribution6 * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.participant.vars['VCMPayoff6'] = Constants.endowment - p.contribution6 + self.individual_share6


class Player(BasePlayer):

    contribution1 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='If your 3 person group is composed with partners according to the table above, how many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider()
    )

    contribution2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='If your 3 person group is composed with partners according to the table above, how many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider()
    )

    contribution3 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='If your 3 person group is composed with partners according to the table above, how many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider()
    )

    contribution4 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='If your 3 person group is composed with partners according to the table above, how many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider()
    )

    contribution5 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='If your 3 person group is composed with partners according to the table above, how many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider()
    )

    contribution6 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='If your 3 person group is composed with partners according to the table above, how many dollars from '
              'your endowment would you like to contribute to the group account?',
        widget=widgets.Slider()
    )

    belief1 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='What do you believe a participant who has never been accused of taking ANY'
              'amount of money from their partner will contribute to the group account on average?',
        widget=widgets.Slider()
    )

    belief2 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='What do you believe a participant who HAS been accused of taking some amount of money from their '
              'partner, '
              'but never found '
              'guilty, '
              'will contribute to the group account on average?',
        widget=widgets.Slider()
    )

    belief3 = models.IntegerField(
        choices=[
            [0, '$0'],
            [2, '$2'],
            [4, '$4'],
            [6, '$6'],
            [8, '$8'],
            [10, '$10']
        ],
        label='What do you believe a participant who HAS been accused and HAS been found guilty '
              'of taking some amount of money from their '
              'partner will contribute to the group account on average?',
        widget=widgets.Slider()
    )

    quiz1 = models.IntegerField(
        choices=[
            [1, '(a) You are each endowed with with 5.'],
            [2, '(b) You are endowed with 10 and your partners endowed with with 0.'],
            [3, '(c) Your partners are endowed with 10 and you start with 0.'],
            [4, '(d) You are each endowed with 10.']
        ],
        widget=widgets.RadioSelect,
        label="Question 1: How many dollars are you and your partners endowed with for this part of the experiment?"
    )

    quiz2 = models.IntegerField(
        choices=[
            [1, '(a) Everyone will earn $2 ($4 x 0.5) from your contribution.'],
            [2, '(b) Everyone will earn $4 ($4 x 1.0) from your contribution.'],
            [3, '(c) Everyone will earn $1 ($4 x 0.25) from your contribution.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 2: If you contribute $4 to the Group Account "
    )

    quiz3 = models.IntegerField(
        choices=[
            [1, '(a) $0 is held in your Private Account.'],
            [2, '(b) $4 is held in your Private Account.'],
            [3, '(c) $6 is held is your Private Account.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 3: If you contribute $4 to the Group Account "
    )

    quiz4 = models.IntegerField(
        choices=[
            [1, '(a) All partners you could interact with in this part of the experiment are guaranteed to have '
                'taken money from others previously.'],
            [2, '(b) Some partners who were truly innocent may have been found guilty of taking money from another '
                'subject.'],
            [3, '(c) Partners who were found guilty of taking money from another participant faced no monetary '
                'penalty from their guilty finding.'],
        ],
        widget=widgets.RadioSelect,
        label="Question 4: Which of the following is true "
    )

    def keep_role(self):
        self.participant.vars['module1role'] = self.id_in_group

    def keep_contributions(self):
        self.participant.vars['contribution1'] = self.contribution1
        self.participant.vars['contribution2'] = self.contribution2
        self.participant.vars['contribution3'] = self.contribution3
        self.participant.vars['contribution4'] = self.contribution4
        self.participant.vars['contribution5'] = self.contribution5
        self.participant.vars['contribution6'] = self.contribution6