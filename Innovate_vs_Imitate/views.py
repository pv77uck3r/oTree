from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = models.Player
    form_fields = ['InnovateorImitateButton', 'Innovate', 'NoInnovate']

    def is_displayed(self):
        return (self.subsession.SuperRound == 1 and self.player.id_in_group == self.session.vars['randomchoice'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 2 and self.player.id_in_group == self.session.vars['randomchoice2'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 3 and self.player.id_in_group == self.session.vars['randomchoice3'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 4 and self.player.id_in_group == self.session.vars['randomchoice4'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 5 and self.player.id_in_group == self.session.vars['randomchoice5'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 6 and self.player.id_in_group == self.session.vars['randomchoice6'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 7 and self.player.id_in_group == self.session.vars['randomchoice7'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 8 and self.player.id_in_group == self.session.vars['randomchoice8'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 9 and self.player.id_in_group == self.session.vars['randomchoice9'][(self.subsession.round_number - 1)%Constants.num_players])\
                or (self.subsession.SuperRound == 10 and self.player.id_in_group == self.session.vars['randomchoice10'][(self.subsession.round_number - 1)%Constants.num_players])

    def vars_for_template(self):
        return {'ImitateValue':round(self.subsession.OldHighDraw,2), 'trianglemode':Constants.trianglemode, 'trianglemodeheight':self.subsession.modeheight, 'Max':self.subsession.OldHighDraw}

    def error_message(self, values):
        if (values["InnovateorImitateButton"] != None and values["Innovate"] == True and values["NoInnovate"] == True) or (values["InnovateorImitateButton"] != None and values["Innovate"] == True and values["NoInnovate"] == False) or (values["InnovateorImitateButton"] != None and values["Innovate"] == False and values["NoInnovate"] == True) or (values["InnovateorImitateButton"] == None and values["Innovate"] == True and values["NoInnovate"] == True) or (values["InnovateorImitateButton"] == None and values["Innovate"] == False and values["NoInnovate"] == False):
            return 'You must only select one of the two checkboxes or enter a value for a probability.'

    def before_next_page(self):
        self.player.InnovateRoll()
        self.player.setpayoff()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class UpdateDaStuff(WaitPage):

    def after_all_players_arrive(self):
        self.subsession.HighDrawLastPeriod()

class retainDraws(Page):
    timeout_seconds = 1

    def before_next_page(self):
        self.player.retainDraws()
        self.player.retainPayoffs()

class Results(Page):

    def is_displayed(self):
        return (self.subsession.SuperRound == 1 and self.player.id_in_group == self.session.vars['randomchoice'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 2 and self.player.id_in_group == self.session.vars['randomchoice2'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 3 and self.player.id_in_group == self.session.vars['randomchoice3'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 4 and self.player.id_in_group == self.session.vars['randomchoice4'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 5 and self.player.id_in_group == self.session.vars['randomchoice5'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 6 and self.player.id_in_group == self.session.vars['randomchoice6'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 7 and self.player.id_in_group == self.session.vars['randomchoice7'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 8 and self.player.id_in_group == self.session.vars['randomchoice8'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 9 and self.player.id_in_group == self.session.vars['randomchoice9'][(self.subsession.round_number - 1)%Constants.num_players]) \
               or (self.subsession.SuperRound == 10 and self.player.id_in_group == self.session.vars['randomchoice10'][(self.subsession.round_number - 1)%Constants.num_players])
    def vars_for_template(self):
        if self.subsession.SuperRound == 1:
            randprob = round(self.session.vars['randomroll'][(self.subsession.round_number - 1)%Constants.num_players]*100,0)
        else:
            if self.subsession.SuperRound == 2:
                randprob = round(self.session.vars['randomroll2'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
            else:
                if self.subsession.SuperRound == 3:
                    randprob = round(self.session.vars['randomroll3'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                else:
                    if self.subsession.SuperRound == 4:
                        randprob = round(self.session.vars['randomroll4'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                    else:
                        if self.subsession.SuperRound == 5:
                            randprob = round(self.session.vars['randomroll5'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                        else:
                            if self.subsession.SuperRound == 6:
                                randprob = round(self.session.vars['randomroll6'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                            else:
                                if self.subsession.SuperRound == 7:
                                    randprob = round(
                                        self.session.vars['randomroll7'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                                else:
                                    if self.subsession.SuperRound == 8:
                                        randprob = round(
                                            self.session.vars['randomroll8'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                                    else:
                                        if self.subsession.SuperRound == 9:
                                            randprob = round(
                                                self.session.vars['randomroll9'][(self.subsession.round_number - 1)%Constants.num_players] * 100, 0)
                                        else:
                                            if self.subsession.SuperRound == 10:
                                                randprob = round(
                                                    self.session.vars['randomroll10'][(self.subsession.round_number - 1)%Constants.num_players] * 100,
                                                    0)
        return {'Prob': self.player.InnovateorImitateButton, 'RandProb':randprob, 'buttontrue': self.player.Innovate, 'buttonfalse': self.player.NoInnovate, 'Choice': self.subsession.OldHighDraw, 'Draw': self.player.Draw, 'payoff': round((self.player.Draw + Constants.endowment),2), 'SuperRound':self.subsession.SuperRound}

    def before_next_page(self):
        self.subsession.UpdateHighDraw()
        self.subsession.UpdateModeHeight()

class FinalResults(Page):

    def is_displayed(self):
        return self.subsession.round_number == self.subsession.SuperRound*10

    def vars_for_template(self):
        return {'Draw': self.player.Draw, 'payoff': self.player.payout, 'possible_payoff': round(self.player.payout * self.session.vars['conversionrate'], 2), 'total_payoff': self.player.payout + Constants.endowment}

class EndOfSuperGamesResults(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {'randomround': self.session.vars['randompayround'], 'total_payoff':self.participant.vars['ExpEarnings'] + Constants.endowment}

class EndOfSuperGameWaitPage(WaitPage):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    wait_for_all_groups = True

page_sequence = [
    UpdateDaStuff,
    retainDraws,
    Decision,
    Results,
    ResultsWaitPage,
    FinalResults,
    # EndOfSuperGamesResults,
    EndOfSuperGameWaitPage
]
