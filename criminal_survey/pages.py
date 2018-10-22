from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Quiz1(Page):
    form_model = 'player'
    form_fields = ['psycheval1', 'psycheval2', 'psycheval3', 'psycheval4', 'psycheval5', 'psycheval6', 'psycheval7',
                   'psycheval8', 'psycheval9', 'psycheval10', 'psycheval11', 'psycheval12', 'psycheval13', 'psycheval14',
                   'psycheval15', 'psycheval16', 'psycheval17', 'psycheval18', 'psycheval19', 'psycheval20', 'psycheval21']


class Quiz2(Page):
    form_model = 'player'
    form_fields = ['characteristic1', 'characteristic2', 'characteristic3', 'characteristic4', 'characteristic5',
                   'characteristic6', 'characteristic7', 'characteristic8', 'characteristic9', 'characteristic10', ]


class Quiz3(Page):
    form_model = 'player'
    form_fields = ['opinions1', 'opinions2', 'opinions3', 'opinions4', 'opinions5', 'opinions6', 'opinions7',
                   'opinions8', 'opinions9', 'opinions10', 'opinions11', 'opinions12', 'opinions13', 'opinions14',
                   'opinions15', 'opinions16', 'opinions17', 'opinions18', 'opinions19', 'opinions20']


class Quiz4(Page):
    form_model = 'player'
    form_fields = ['Age', 'Gender', 'RaceOrEthnicity', 'SubjectOfStudy', 'PoliticalViews', 'VotingBehavior',
                   'PartyAffiliation', 'ReligiousServices', 'Congregation', 'Confusion', 'WhatConfusion',
                   'FamilyIncome', 'EconClasses', 'Work']


class Quiz5(Page):
    form_model = 'player'
    form_fields = ['psychevalagain1', 'psychevalagain2', 'psychevalagain3', 'psychevalagain4', 'psychevalagain5',
                   'psychevalagain6', 'psychevalagain7', 'psychevalagain8', 'psychevalagain9', 'psychevalagain10',
                   'psychevalagain11', 'psychevalagain12', 'psychevalagain13', 'psychevalagain14', 'psychevalagain15',
                   'psychevalagain16', 'psychevalagain17', 'psychevalagain18', 'psychevalagain19', 'psychevalagain20',
                   'psychevalagain21']


class Quiz6(Page):
    form_model = 'player'
    form_fields = ['ClarityOfInstructions', 'PercentTakeSmall', 'PercentTakeMedium', 'PercentTakeLarge',
                   'ReasonableDoubt', 'ReasonableDoubtJuror', 'PleadFifth', 'InnocentPleadFifth', 'GuiltyPleadFifth',
                   'Opinion']


class End(Page):

    def vars_for_template(self):
        return {
            'ID': self.participant.id_in_session
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Intro,
    Quiz1,
    Quiz2,
    Quiz3,
    Quiz4,
    Quiz5,
    Quiz6,
    End
]
