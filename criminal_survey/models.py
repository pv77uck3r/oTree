from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


def make_field(label):
    return models.IntegerField(
        choices=[
            [1, ''],
            [2, ''],
            [3, ''],
            [4, ''],
            ],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field2(label):
    return models.IntegerField(
        choices=[
            [1, ''],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, '']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field3(label):
    return models.IntegerField(
        choices=[
            [1, ''],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, '']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

author = 'Jason Ralston'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    psycheval1 = make_field('My heart beats fast.')
    psycheval2 = make_field('My muscles are tense.')
    psycheval3 = make_field('I feel agonized over my problems.')
    psycheval4 = make_field('I think that others won\'t aprrove of me.')
    psycheval5 = make_field('I feel like I\'m missing out on things because I cant\'t make up my mind soon enough.')
    psycheval6 = make_field('I feel dizzy.')
    psycheval7 = make_field('My muscles feel weak.')
    psycheval8 = make_field('I feel trembly and shaky.')
    psycheval9 = make_field('I picture some future misfortune.')
    psycheval10 = make_field('I can\'t get some thought out of my mind.')
    psycheval11 = make_field('I have trouble remembering things.')
    psycheval12 = make_field('My face feels hot.')
    psycheval13 = make_field('I think that the worst will happen.')
    psycheval14 = make_field('My arms and legs feel stiff.')
    psycheval15 = make_field('My throat feels dry.')
    psycheval16 = make_field('I keep busy to avoid uncomfortable thoughts.')
    psycheval17 = make_field('I cannot concentrate without irrelevant thoughts intruding.')
    psycheval18 = make_field('My breathing is fast and shallow.')
    psycheval19 = make_field('I worry that I cannot control my thoughts as well as I would like to.')
    psycheval20 = make_field('I have butterflies in my stomach.')
    psycheval21 = make_field('My palms feel clammy.')

    characteristic1 = make_field2('I consider how things might be in the future, and try to influence those things with '
                                  'my day to day behavior.')
    characteristic2 = make_field2('Often I engage in particular behavior in order to achieve outcomes that may not '
                                  'result for many years.')
    characteristic3 = make_field2('I only act ot satisfy immediate concerns, figuring the future will take care of '
                                  'itself.')
    characteristic4 = make_field2('My behavior is only influenced by immediate (i.e., a matter of days or weeks) '
                                  'outcomes of my actions.')
    characteristic5 = make_field2('My convenience is a big factor in the decisions I make or the actions I take.')
    characteristic6 = make_field2('I am willing to sacrifice my immediate happiness or well-being in order to achieve '
                                  'future outcomes.')
    characteristic7 = make_field2('I think it is important to take warnings about negative outcomes seriously even '
                                  'if the negative outcome will not occur for many years.')
    characteristic8 = make_field2('I think it is more important to perform a behavior with important distant '
                                  'consequences than a behavior with less-important immediate consequences.')
    characteristic9 = make_field2('I generally ignore warnings about possible future problems because I think the '
                                  'problems will be resolved before they reach crisis level.')
    characteristic10 = make_field2('I think that sacrificing now is usually unnecessary since future outcomes can '
                                   'be dealt with at a later time.')

    opinions1 = make_field3('Never tell anyone the real reason you did something unless it is useful to do so.')
    opinions2 = make_field3('The best way to handle people is to tell them what they want to hear.')
    opinions3 = make_field3('One should take action only when sure it is morally right.')
    opinions4 = make_field3('Most people are basically good and kind.')
    opinions5 = make_field3('It is safe to assume that all people have a vicious streak and it will come out when they '
                            'are given a chance.')
    opinions6 = make_field3('Honesty is the best policy in all cases.')
    opinions7 = make_field3('There is no excuse for lying to someone else.')
    opinions8 = make_field3('It is hard to get ahead without cutting corners here and there.')
    opinions9 = make_field3('All in all, it is better to be humble and honest than important and dishonest.')
    opinions10 = make_field3('When you ask someone to do something for you, it is best to give the real reasons for '
                             'wanting it rather than giving reasons that carry more weight')
    opinions11 = make_field3('Most people who get ahead in the world lead clean, moral lives.')
    opinions12 = make_field3('Anyone who completely trusts anyone else is asking for trouble.')
    opinions13 = make_field3('The biggest difference between most criminals and other people is that criminals are '
                             'stupid enough to get caught.')
    opinions14 = make_field3('Most men are brave.')
    opinions15 = make_field3('It is wise to flatter important people.')
    opinions16 = make_field3('It is possible to be good in all respects.')
    opinions17 = make_field3('Barnum was very wrong when he said that there\'s a sucker born every minute.')
    opinions18 = make_field3('Generally speaking, men wont work hard unless they are forced to do so.')
    opinions19 = make_field3('People suffering from incurable diseases should have the choice of being put painlessly '
                             'to death.')
    opinions20 = make_field3('Most men forget more easily the death of their father than the loss of their property.')

    Age = models.IntegerField(
        choices=[
            [1, '18-22'],
            [2, '23-30'],
            [3, '30-40'],
            [4, '40 or above']
        ],
        label='Age',
        widget=widgets.RadioSelect()
    )

    Gender = models.IntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female']
        ],
        label='Gender',
        widget=widgets.RadioSelect()
    )

    RaceOrEthnicity = models.IntegerField(
        choices=[
            [1, 'White'],
            [2, 'Black or African American'],
            [3, 'Asian'],
            [4, 'Indian or Pacific Islander'],
            [5, 'Hispanic'],
            [6, 'Other Race']
        ],
        label='Race or Ethnicity',
        widget=widgets.RadioSelect()
    )

    SubjectOfStudy = models.StringField(
        label='What subject do you study?'
    )

    PoliticalViews = models.IntegerField(
        choices=[
            [1, 'Very conservative'],
            [2, 'Conservative'],
            [3, 'Moderate'],
            [4, 'Liberal'],
            [5, 'Very liberal']
        ],
        label='How would you describe your political views?',
        widget=widgets.RadioSelect()
    )

    VotingBehavior = models.IntegerField(
        choices=[
            [1, 'I do not vote'],
            [2, 'I have not voted previously but plan to vote in the future'],
            [3, 'I voted previously but do not plan to vote in the future'],
            [4, 'I vote only in minor elections'],
            [5, 'I vote only in major elections'],
            [6, 'I vote in all elections'],
            [7, 'Other']
        ],
        label='Which of the following best describes your voting behavior?',
        widget=widgets.RadioSelect()
    )

    PartyAffiliation = models.IntegerField(
        choices=[
            [1, 'Republican'],
            [2, 'Democrat'],
            [3, 'Libertarian'],
            [4, 'Independent'],
            [5, 'None/Don\'t Know']
        ],
        label='Generally speaking, do you usually think of yourself as a Republican, Democrat, Libertarian, or '
              'Independent?',
        widget=widgets.RadioSelect()
    )

    ReligiousServices = models.IntegerField(
        choices=[
            [1, 'Never'],
            [2, 'Less than once a year'],
            [3, 'Once a year'],
            [4, 'A few times a year'],
            [5, 'Once a month'],
            [6, 'Two to three times per month'],
            [7, 'Once per week'],
            [8, 'More than once per week']
        ],
        label='Aside from weddings, funerals, and mandatory chapel services, about how often do you attend religious '
              'services?',
        widget=widgets.RadioSelect()
    )

    Congregation = models.LongStringField(
        label='What is the name of the religious congregation whose services you most often attend? How far do you '
             'travel to attend?'
    )

    Confusion = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [2, 'No']
        ],
        label='Were you confused by anything in the experiment?',
        widget=widgets.RadioSelect()
    )

    WhatConfusion = models.LongStringField(
        label='If yes, what confused you?'
    )

    FamilyIncome = models.IntegerField(
        choices=[
            [1, 'significantly higher'],
            [2, 'somewhat higher'],
            [3, 'about the same'],
            [4, 'somewhat below'],
            [5, 'significantly below']
        ],
        label='What is your household (family) income relative to other students at Baylor?',
        widget=widgets.RadioSelectHorizontal()
    )

    EconClasses = models.IntegerField(
        choices=[
            [0, 'None'],
            [1, 'One'],
            [2, 'Two'],
            [3, 'Three'],
            [4, 'Four or more']
        ],
        label='How many Economics classes have you taken at the university level?',
        widget=widgets.RadioSelectHorizontal()
    )

    Work = models.IntegerField(
        choices=[
            [1, 'Work a full-time job'],
            [2, 'Work a part-time job'],
            [3, 'Do not have a job']
        ],
        label='In addition to school, do you...',
        widget=widgets.RadioSelectHorizontal()
    )

    psychevalagain1 = make_field('My heart beats fast.')
    psychevalagain2 = make_field('My muscles are tense.')
    psychevalagain3 = make_field('I feel agonized over my problems.')
    psychevalagain4 = make_field('I think that others won\'t aprrove of me.')
    psychevalagain5 = make_field('I feel like I\'m missing out on things because I cant\'t make up my mind soon enough.')
    psychevalagain6 = make_field('I feel dizzy.')
    psychevalagain7 = make_field('My muscles feel weak.')
    psychevalagain8 = make_field('I feel trembly and shaky.')
    psychevalagain9 = make_field('I picture some future misfortune.')
    psychevalagain10 = make_field('I can\'t get some thought out of my mind.')
    psychevalagain11 = make_field('I have trouble remembering things.')
    psychevalagain12 = make_field('My face feels hot.')
    psychevalagain13 = make_field('I think that the worst will happen.')
    psychevalagain14 = make_field('My arms and legs feel stiff.')
    psychevalagain15 = make_field('My throat feels dry.')
    psychevalagain16 = make_field('I keep busy to avoid uncomfortable thoughts.')
    psychevalagain17 = make_field('I cannot concentrate without irrelevant thoughts intruding.')
    psychevalagain18 = make_field('My breathing is fast and shallow.')
    psychevalagain19 = make_field('I worry that I cannot control my thoughts as well as I would like to.')
    psychevalagain20 = make_field('I have butterflies in my stomach.')
    psychevalagain21 = make_field('My palms feel clammy.')

    ClarityOfInstructions = models.LongStringField(
        label='Please comment on the clarity of the instructions.'
    )

    PercentTakeSmall = models.IntegerField(
        label='What percentage of Baylor students who participate in the experiment do you believe will choose to take '
              'a small amount from their other Baylor student counterpart participant?'
    )

    PercentTakeMedium = models.IntegerField(
        label='What percentage of Baylor students who participate in the experiment do you believe will choose to take '
              'a medium amount from their other Baylor student counterpart participant?'
    )

    PercentTakeLarge = models.IntegerField(
        label='What percentage of Baylor students who participate in the experiment do you believe will choose to take '
              'a large amount from their other Baylor student counterpart participant?'
    )

    ReasonableDoubt = models.IntegerField(
        label='What percentage "doubt" do you think qualifies as "reasonable doubt"? In other words, if there is a 1% '
              'chance you think someone is innocent, is that "reasonable doubt"? What is the smallest chance of '
              'innocence where you\'d switch your determination from "guilty" to "not guilty"?'
    )

    ReasonableDoubtJuror = models.IntegerField(
        label='What percentage "doubt" do you think qualifies as "reasonable doubt" for a juror? In other words, if '
              'there is a 1% '
              'chance a juror thought someone is innocent, is that "reasonable doubt" to them? What is the smallest '
              'chance of '
              'innocence where a juror would switch their determination from "guilty" to "not guilty"?'
    )

    PleadFifth = models.IntegerField(
        choices=[
            [1, 'It would make them think the defendant is more likely to be guilty'],
            [2, 'It would not influence their decision'],
            [3, 'It would bmake them think the defendant is more likely to be not guilty']
        ],
        label='Do you think observing that a defendant chose not to provide evidence of their own innocence affects '
              'juror\'s decision to find them guilty or not guilty?',
        widget=widgets.RadioSelect()
    )

    InnocentPleadFifth = models.IntegerField(
        label='What percentage of truly innocent defendants, who have some evidence of innocence, do you think choose '
              'to exercise their right not to provide evidence on their own behalf?'
    )

    GuiltyPleadFifth = models.IntegerField(
        label='What percentage of truly guilty defendants, who have some evidence of innocence, do you think choose '
              'to exercise their right not to provide evidence on their own behalf?'
    )

    Opinion = models.LongStringField(
        label='Is there anything else you would like to tell the experimenters about this experiment?'
    )
