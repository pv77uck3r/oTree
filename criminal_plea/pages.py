from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class InfoDump(WaitPage):

    def is_displayed(self):
        return self.subsession.round_number == 1

    def after_all_players_arrive(self):
        self.subsession.gen_info_sets()

class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3']

    def quiz1_error_message(self, value):
        if value != 1:
            return 'Question 1 is incorrect. Please try again.'

    def quiz2_error_message(self, value):
        if value != 1:
            return 'Question 2 is incorrect. Please try again.'

    def quiz3_error_message(self, value):
        if value != 1:
            return 'Question 3 is incorrect. Please try again.'


class Preparation(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Plea_Decisions(Page):

    form_model = 'player'
    def get_form_fields(self):
        if self.subsession.round_number % 3 == 1:
            return ['plea_decision2', 'plea_decision3', 'plea_decision4', 'plea_decision5', 'plea_decision6']
        if self.subsession.round_number % 3 == 2:
            return ['plea_decision4', 'plea_decision5', 'plea_decision6']
        if self.subsession.round_number % 3 == 0:
            return ['plea_decision6']

    def vars_for_template(self):
        innocence = self.participant.vars['trulyinnocent']
        if innocence == True:
            innocencestring = 'INNOCENT'
        if innocence == False:
            innocencestring = 'GUILTY'
        innocenceevidence = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0]
        if innocenceevidence == 1:
            innocenceevidencestring = 'NONEXISTENT'
        if innocenceevidence == 2:
            innocenceevidencestring = 'WEAK'
        if innocenceevidence == 3:
            innocenceevidencestring = 'MEDIUM'
        if innocenceevidence == 4:
            innocenceevidencestring = 'STRONG'
        guiltevidence = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1]
        if guiltevidence == 1:
            guiltevidencestring = 'NONEXISTENT'
        if guiltevidence == 2:
            guiltevidencestring = 'WEAK'
        if guiltevidence == 3:
            guiltevidencestring = 'MEDIUM'
        if guiltevidence == 4:
            guiltevidencestring = 'STRONG'
        punlevel = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2]
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == .2 or self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == .5:
            crimelevel = 'SMALL CRIME'
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == .7 or self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == 1:
            crimelevel = 'MEDIUM CRIME'
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == 1.2:
            crimelevel = 'LARGE CRIME'

        return {'innocence': innocencestring,
                'innocenceevidence': innocenceevidencestring,
                'guiltevidence': guiltevidencestring,
                'punlevel': punlevel,
                'crimelevel': crimelevel}

    def before_next_page(self):
        self.player.set_payoff()


class Trial_Decisions(Page):

    form_model = 'player'
    form_fields = ['trial_decision1', 'trial_decision2', 'trial_decision3', 'trial_decision4', 'trial_decision5',
                   'trial_decision6']

    def is_displayed(self):
        return self.subsession.round_number % 3 == 0

    def vars_for_template(self):
        innocence = self.participant.vars['trulyinnocent']
        if innocence == True:
            innocencestring = 'INNOCENT'
        if innocence == False:
            innocentstring = 'GUILTY'
        innocenceevidence = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][0]
        if innocenceevidence == 1:
            innocenceevidencestring = 'NONEXISTENT'
        if innocenceevidence == 2:
            innocenceevidencestring = 'WEAK'
        if innocenceevidence == 3:
            innocenceevidencestring = 'MEDIUM'
        if innocenceevidence == 4:
            innocenceevidencestring = 'STRONG'
        guiltevidence = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][1]
        if guiltevidence == 2:
            guiltevidencestring = 'WEAK'
        if guiltevidence == 3:
            guiltevidencestring = 'MEDIUM'
        if guiltevidence == 4:
            guiltevidencestring = 'STRONG'
        punlevel = self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2]
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == .2 or \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == .5:
            crimelevel = 'SMALL CRIME'
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == .7 or \
                self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == 1:
            crimelevel = 'MEDIUM CRIME'
        if self.participant.vars['allpossibleinfo'][self.subsession.round_number - 1][2] == 1.2:
            crimelevel = 'LARGE CRIME'
        return {'innocence': innocencestring,
                'innocenceevidence': innocenceevidencestring,
                'guiltevidence': guiltevidencestring,
                'punlevel': punlevel,
                'crimelevel': crimelevel,
                'innocencenumber': innocenceevidence,
                'guiltnumber': guiltevidence
                }

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        if self.player.ending_guilt_level == 1:
            crime = 'SMALL'
        if self.player.ending_guilt_level == 2:
            crime = 'MEDIUM'
        if self.player.ending_guilt_level == 3:
            crime = 'LARGE'
        if self.participant.vars['proschoice'] == 3 and self.participant.vars['relevantchoice'] == 1:
            trial = 'Plea Bargain'
        else:
            trial = 'Jury Trial'

        return {'crimelevel': crime,
                'punishment': self.player.ending_punishment,
                'trialornot': trial}


page_sequence = [
    InfoDump,
    Instructions,
    Quiz,
    Preparation,
    Plea_Decisions,
    Trial_Decisions,
    Results
]
