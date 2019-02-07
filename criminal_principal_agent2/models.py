from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


def make_field(label):
    return models.FloatField(
        choices=[
            [0, ''],
            [0.1, ''],
            [0.2, ''],
            [0.3, ''],
            [0.4, ''],
            [0.5, ''],
            [0.6, ''],
            [0.7, ''],
            [0.8, ''],
            [0.9, ''],
            [1, '']
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

doc = """
The principal offers a contract to the agent, who can decide if to reject or
accept. The agent then chooses an effort level. The implementation is based on
<a href="http://www.nottingham.ac.uk/cedex/documents/papers/2006-04.pdf">
    Gaechter and Koenigstein (2006)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'criminal_principal_agent2'
    players_per_group = 2
    num_rounds = 1

    instructions_template_A = 'criminal_principal_agent2/Instructions_Agent.html'
    instructions_template_P = 'criminal_principal_agent2/Instructions_Principal.html'

    min_fixed_payment = c(0)
    max_fixed_payment = c(120)

    # """Amount principal gets if contract is rejected"""
    reject_principal_pay = c(0)

    reject_agent_pay = c(0)

    # agent_return_share_choices = [
    #     [percent / 100.0, '{}%'.format(percent)]
    #     for percent in range(10, 100 + 1, 10)]

    # EFFORT_TO_RETURN = {
    #     1: 2.33,
    #     2: 4.67,
    #     3: 7,
    #     4: 9,
    #     5: 11.67,
    #     6: 14,
    #     7: 16.33,
    #     8: 18.67,
    #     9: 21,
    #     10: 23.33}

    EFFORT_TO_COST = {
        .1: 0,
        .2: 1,
        .3: 2,
        .4: 4,
        .5: 6,
        .6: 8,
        .7: 10,
        .8: 12,
        .9: 15,
        1: 18}


def cost_from_effort(effort):
    return c(Constants.EFFORT_TO_COST[effort])

# def return_from_effort(effort):
#     return c(Constants.EFFORT_TO_RETURN[effort])


class Subsession(BaseSubsession):

    def set_groups_1(self):
        self.set_group_matrix(self.session.vars['subjlists'][0])
        for group in self.get_groups():
            players = group.get_players()
            group.set_players(players)

    def set_groups_2(self):
        self.set_group_matrix(self.session.vars['subjlists'][3])
        for group in self.get_groups():
            players = group.get_players()
            group.set_players(players)


class Group(BaseGroup):

    amount_offered = models.CurrencyField()
    effort = models.FloatField()
    effort_cost = models.CurrencyField()
    accept = models.BooleanField()

    total_return = models.CurrencyField(
        doc="""Total return from agent's effort = [Return for single unit of
            agent's work effort] * [Agent's work effort]"""
    )

    agent_fixed_pay_1 = models.CurrencyField(
        choices=range(0, 120 + 1, 10),
        widget=widgets.RadioSelectHorizontal(),
        doc="""Amount offered as fixed pay to agent.""",
        min=Constants.min_fixed_payment, max=Constants.max_fixed_payment,
        label="What fixed payment will you offer to Participant B "
              "if they WERE NEVER ACCUSED of taking a small, "
              "medium, or large amount of money that belonged to another "
              "participant?"
    )

    agent_fixed_pay_2 = models.CurrencyField(
        choices=range(0, 120 + 1, 10),
        widget=widgets.RadioSelectHorizontal(),
        doc="""Amount offered as fixed pay to agent.""",
        min=Constants.min_fixed_payment, max=Constants.max_fixed_payment,
        label="What fixed payment will you offer to Participant B "
              "if they WERE ACCUSED but FOUND NOT-GUILTY of taking a small, "
              "medium, or large amount of money that belonged to another "
              "participant?"
    )

    agent_fixed_pay_3 = models.CurrencyField(
        choices=range(0, 120 + 1, 10),
        widget=widgets.RadioSelectHorizontal(),
        doc="""Amount offered as fixed pay to agent.""",
        min=Constants.min_fixed_payment, max=Constants.max_fixed_payment,
        label="What fixed payment will you offer to Participant B "
              "if they WAS FOUND GUILTY of taking a SMALL amount of money that belonged to another "
              "participant?"
    )

    agent_fixed_pay_4 = models.CurrencyField(
        choices=range(0, 120 + 1, 10),
        widget=widgets.RadioSelectHorizontal(),
        doc="""Amount offered as fixed pay to agent.""",
        min=Constants.min_fixed_payment, max=Constants.max_fixed_payment,
        label="What fixed payment will you offer to Participant B "
              "if they WAS FOUND GUILTY of taking a MEDIUM amount of money that belonged to another "
              "participant?"
    )

    agent_fixed_pay_5 = models.CurrencyField(
        choices=range(0, 120 + 1, 10),
        widget=widgets.RadioSelectHorizontal(),
        doc="""Amount offered as fixed pay to agent.""",
        min=Constants.min_fixed_payment, max=Constants.max_fixed_payment,
        label="What fixed payment will you offer to Participant B "
              "if they WAS FOUND GUILTY of taking a LARGE amount of money that belonged to another "
              "participant?"
    )

    # agent_return_share = models.FloatField(
    #     choices=Constants.agent_return_share_choices,
    #     doc="""Agent's share of total return""",
    #     widget=widgets.RadioSelectHorizontal
    # )

    agent_work_effort_1 = make_field('What amount of effort would you select if Participant A\'s contract were for 10 '
                                     'dimes in fixed payment?')

    agent_work_cost_1 = models.CurrencyField(
        doc="""Agent's cost of work effort""",
        label="Would you accept a contract for 0 dimes in fixed payment?"
    )

    agent_work_effort_2 = make_field('What amount of effort would you select if Participant A\'s contract were for 0 '
                                     'dimes in fixed payment?')

    agent_work_effort_3 = make_field('What amount of effort would you select if Participant A\'s contract were for 20 '
                                     'dimes in fixed payment?')

    agent_work_effort_4 = make_field('What amount of effort would you select if Participant A\'s contract were for 30 '
                                     'dimes in fixed payment?')

    agent_work_effort_5 = make_field('What amount of effort would you select if Participant A\'s contract were for 40 '
                                     'dimes in fixed payment?')

    agent_work_effort_6 = make_field('What amount of effort would you select if Participant A\'s contract were for 50 '
                                     'dimes in fixed payment?')

    agent_work_effort_7 = make_field('What amount of effort would you select if Participant A\'s contract were for 60 '
                                     'dimes in fixed payment?')

    agent_work_effort_8 = make_field('What amount of effort would you select if Participant A\'s contract were for 70 '
                                     'dimes in fixed payment?')

    agent_work_effort_9 = make_field('What amount of effort would you select if Participant A\'s contract were for 80 '
                                     'dimes in fixed payment?')

    agent_work_effort_10 = make_field('What amount of effort would you select if Participant A\'s contract were for 90 '
                                      'dimes in fixed payment?')

    agent_work_effort_11 = make_field(
        'What amount of effort would you select if Participant A\'s contract were for 100 '
        'dimes in fixed payment?')

    agent_work_effort_12 = make_field(
        'What amount of effort would you select if Participant A\'s contract were for 110 '
        'dimes in fixed payment?')

    agent_work_effort_13 = make_field(
        'What amount of effort would you select if Participant A\'s contract were for 120 '
        'dimes in fixed payment?')

    agent_work_cost_2 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_3 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_4 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_5 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_6 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_7 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_8 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_9 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_10 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_11 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_12 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    agent_work_cost_13 = models.CurrencyField(
        doc="""Agent's cost of work effort"""
    )

    contract_accepted_1 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 0 dimes in fixed payment from Participant A?'
    )

    contract_accepted_2 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 10 dimes in fixed payment from Participant A?'
    )

    contract_accepted_3 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 20 dimes in fixed payment from Participant A?'
    )

    contract_accepted_4 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 30 dimes in fixed payment from Participant A?'
    )

    contract_accepted_5 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 40 dimes in fixed payment from Participant A?'
    )

    contract_accepted_6 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 50 dimes in fixed payment from Participant A?'
    )

    contract_accepted_7 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 60 dimes in fixed payment from Participant A?'
    )

    contract_accepted_8 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 70 dimes in fixed payment from Participant A?'
    )

    contract_accepted_9 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 80 dimes in fixed payment from Participant A?'
    )

    contract_accepted_10 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 90 dimes in fixed payment from Participant A?'
    )

    contract_accepted_11 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 100 dimes in fixed payment from Participant A?'
    )

    contract_accepted_12 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 110 dimes in fixed payment from Participant A?'
    )

    contract_accepted_13 = models.BooleanField(
        doc="""Whether agent accepts proposal""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Accept'],
            [False, 'Reject'],
        ],
        label='Would you accept a contract for 120 dimes in fixed payment from Participant A?'
    )

    def set_accepts(self):
        if self.agent_work_effort_1 == 0:
            self.contract_accepted_1 = False
        else:
            self.contract_accepted_1 = True
        if self.agent_work_effort_2 == 0:
            self.contract_accepted_2 = False
        else:
            self.contract_accepted_2 = True
        if self.agent_work_effort_3 == 0:
            self.contract_accepted_3 = False
        else:
            self.contract_accepted_3 = True
        if self.agent_work_effort_4 == 0:
            self.contract_accepted_4 = False
        else:
            self.contract_accepted_4 = True
        if self.agent_work_effort_5 == 0:
            self.contract_accepted_5 = False
        else:
            self.contract_accepted_5 = True
        if self.agent_work_effort_6 == 0:
            self.contract_accepted_6 = False
        else:
            self.contract_accepted_6 = True
        if self.agent_work_effort_7 == 0:
            self.contract_accepted_7 = False
        else:
            self.contract_accepted_7 = True
        if self.agent_work_effort_8 == 0:
            self.contract_accepted_8 = False
        else:
            self.contract_accepted_8 = True
        if self.agent_work_effort_9 == 0:
            self.contract_accepted_9 = False
        else:
            self.contract_accepted_9 = True
        if self.agent_work_effort_10 == 0:
            self.contract_accepted_10 = False
        else:
            self.contract_accepted_10 = True
        if self.agent_work_effort_11 == 0:
            self.contract_accepted_11 = False
        else:
            self.contract_accepted_11 = True
        if self.agent_work_effort_12 == 0:
            self.contract_accepted_12 = False
        else:
            self.contract_accepted_12 = True
        if self.agent_work_effort_13 == 0:
            self.contract_accepted_13 = False
        else:
            self.contract_accepted_13 = True

    def keep_decisions(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        p1.participant.vars['agent_fixed_pay_1'] = self.agent_fixed_pay_1
        p1.participant.vars['agent_fixed_pay_2'] = self.agent_fixed_pay_2
        p1.participant.vars['agent_fixed_pay_3'] = self.agent_fixed_pay_3
        p1.participant.vars['agent_fixed_pay_4'] = self.agent_fixed_pay_4
        p1.participant.vars['agent_fixed_pay_5'] = self.agent_fixed_pay_5

        p2.participant.vars['agent_work_effort_1'] = self.agent_work_effort_1
        p2.participant.vars['agent_work_effort_2'] = self.agent_work_effort_2
        p2.participant.vars['agent_work_effort_3'] = self.agent_work_effort_3
        p2.participant.vars['agent_work_effort_4'] = self.agent_work_effort_4
        p2.participant.vars['agent_work_effort_5'] = self.agent_work_effort_5
        p2.participant.vars['agent_work_effort_6'] = self.agent_work_effort_6
        p2.participant.vars['agent_work_effort_7'] = self.agent_work_effort_7
        p2.participant.vars['agent_work_effort_8'] = self.agent_work_effort_8
        p2.participant.vars['agent_work_effort_9'] = self.agent_work_effort_9
        p2.participant.vars['agent_work_effort_10'] = self.agent_work_effort_10
        p2.participant.vars['agent_work_effort_11'] = self.agent_work_effort_11
        p2.participant.vars['agent_work_effort_12'] = self.agent_work_effort_12
        p2.participant.vars['agent_work_effort_13'] = self.agent_work_effort_13

        p2.participant.vars['contract_accepted_1'] = self.contract_accepted_1
        p2.participant.vars['contract_accepted_2'] = self.contract_accepted_2
        p2.participant.vars['contract_accepted_3'] = self.contract_accepted_3
        p2.participant.vars['contract_accepted_4'] = self.contract_accepted_4
        p2.participant.vars['contract_accepted_5'] = self.contract_accepted_5
        p2.participant.vars['contract_accepted_6'] = self.contract_accepted_6
        p2.participant.vars['contract_accepted_7'] = self.contract_accepted_7
        p2.participant.vars['contract_accepted_8'] = self.contract_accepted_8
        p2.participant.vars['contract_accepted_9'] = self.contract_accepted_9
        p2.participant.vars['contract_accepted_10'] = self.contract_accepted_10
        p2.participant.vars['contract_accepted_11'] = self.contract_accepted_11
        p2.participant.vars['contract_accepted_12'] = self.contract_accepted_12
        p2.participant.vars['contract_accepted_13'] = self.contract_accepted_13

    def set_payoffs_1(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if not (p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3):
            amount_offered = p1.participant.vars['agent_fixed_pay_1']
            if amount_offered == 0:
                accept = p2.participant.vars['contract_accepted_1']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_1']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 10:
                accept = p2.participant.vars['contract_accepted_2']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_2']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 20:
                accept = p2.participant.vars['contract_accepted_3']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_3']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 30:
                accept = p2.participant.vars['contract_accepted_4']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_4']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 40:
                accept = p2.participant.vars['contract_accepted_5']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_5']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 50:
                accept = p2.participant.vars['contract_accepted_6']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_6']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 60:
                accept = p2.participant.vars['contract_accepted_7']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_7']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 70:
                accept = p2.participant.vars['contract_accepted_8']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_8']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 80:
                accept = p2.participant.vars['contract_accepted_9']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_9']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 90:
                accept = p2.participant.vars['contract_accepted_10']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_10']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 100:
                accept = p2.participant.vars['contract_accepted_11']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_11']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 110:
                accept = p2.participant.vars['contract_accepted_12']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_12']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0
            if amount_offered == 120:
                accept = p2.participant.vars['contract_accepted_13']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_13']
                    self.effort = effort
                    p1.participant.vars['payoffmodule1'] = (120 - amount_offered)*(effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule1'] = 0
                    p2.participant.vars['payoffmodule1'] = 0

        if p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3:
            if p2.participant.vars['ending_guilt_level'] == 0:
                amount_offered = p1.participant.vars['agent_fixed_pay_2']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
            if p2.participant.vars['ending_guilt_level'] == 1:
                amount_offered = p1.participant.vars['agent_fixed_pay_3']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
            if p2.participant.vars['ending_guilt_level'] == 2:
                amount_offered = p1.participant.vars['agent_fixed_pay_4']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
            if p2.participant.vars['ending_guilt_level'] == 3:
                amount_offered = p1.participant.vars['agent_fixed_pay_5']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule1'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule1'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule1'] = 0
                        p2.participant.vars['payoffmodule1'] = 0
        self.amount_offered = amount_offered
        p1.payoffmodule1 = p1.participant.vars['payoffmodule1'] * .10 + 2
        p2.payoffmodule1 = p2.participant.vars['payoffmodule1'] * .10 + 2

    def set_payoffs_2(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if not (p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3):
            amount_offered = p1.participant.vars['agent_fixed_pay_1']
            if amount_offered == 0:
                accept = p2.participant.vars['contract_accepted_1']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_1']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 10:
                accept = p2.participant.vars['contract_accepted_2']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_2']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 20:
                accept = p2.participant.vars['contract_accepted_3']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_3']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 30:
                accept = p2.participant.vars['contract_accepted_4']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_4']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 40:
                accept = p2.participant.vars['contract_accepted_5']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_5']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 50:
                accept = p2.participant.vars['contract_accepted_6']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_6']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 60:
                accept = p2.participant.vars['contract_accepted_7']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_7']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 70:
                accept = p2.participant.vars['contract_accepted_8']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_8']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 80:
                accept = p2.participant.vars['contract_accepted_9']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_9']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 90:
                accept = p2.participant.vars['contract_accepted_10']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_10']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 100:
                accept = p2.participant.vars['contract_accepted_11']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_11']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 110:
                accept = p2.participant.vars['contract_accepted_12']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_12']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0
            if amount_offered == 120:
                accept = p2.participant.vars['contract_accepted_13']
                self.accept = accept
                if accept == True:
                    effort = p2.participant.vars['agent_work_effort_13']
                    self.effort = effort
                    p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                    effort_cost = cost_from_effort(effort)
                    self.effort_cost = effort_cost
                    p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                else:
                    p1.participant.vars['payoffmodule4'] = 0
                    p2.participant.vars['payoffmodule4'] = 0

        if p2.participant.vars['proschoice'] == 2 or p2.participant.vars['proschoice'] == 3:
            if p2.participant.vars['ending_guilt_level'] == 0:
                amount_offered = p1.participant.vars['agent_fixed_pay_2']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
            if p2.participant.vars['ending_guilt_level'] == 1:
                amount_offered = p1.participant.vars['agent_fixed_pay_3']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
            if p2.participant.vars['ending_guilt_level'] == 2:
                amount_offered = p1.participant.vars['agent_fixed_pay_4']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
            if p2.participant.vars['ending_guilt_level'] == 3:
                amount_offered = p1.participant.vars['agent_fixed_pay_5']
                if amount_offered == 0:
                    accept = p2.participant.vars['contract_accepted_1']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_1']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 10:
                    accept = p2.participant.vars['contract_accepted_2']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_2']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 20:
                    accept = p2.participant.vars['contract_accepted_3']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_3']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 30:
                    accept = p2.participant.vars['contract_accepted_4']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_4']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 40:
                    accept = p2.participant.vars['contract_accepted_5']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_5']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 50:
                    accept = p2.participant.vars['contract_accepted_6']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_6']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 60:
                    accept = p2.participant.vars['contract_accepted_7']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_7']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 70:
                    accept = p2.participant.vars['contract_accepted_8']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_8']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 80:
                    accept = p2.participant.vars['contract_accepted_9']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_9']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 90:
                    accept = p2.participant.vars['contract_accepted_10']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_10']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 100:
                    accept = p2.participant.vars['contract_accepted_11']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_11']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 110:
                    accept = p2.participant.vars['contract_accepted_12']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_12']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
                if amount_offered == 120:
                    accept = p2.participant.vars['contract_accepted_13']
                    self.accept = accept
                    if accept == True:
                        effort = p2.participant.vars['agent_work_effort_13']
                        self.effort = effort
                        p1.participant.vars['payoffmodule4'] = (120 - amount_offered) * (effort / 10)
                        effort_cost = cost_from_effort(effort)
                        self.effort_cost = effort_cost
                        p2.participant.vars['payoffmodule4'] = amount_offered - effort_cost + 20
                    else:
                        p1.participant.vars['payoffmodule4'] = 0
                        p2.participant.vars['payoffmodule4'] = 0
        self.amount_offered = amount_offered
        p1.payoffmodule4 = p1.participant.vars['payoffmodule4'] * .10 + 2
        p2.payoffmodule4 = p2.participant.vars['payoffmodule4'] * .10 + 2

    # def set_payoffs(self):
    #     principal = self.get_player_by_role('principal')
    #     agent = self.get_player_by_role('agent')
    #
    #     if self.contract_accepted:
    #         self.agent_work_cost = cost_from_effort(self.agent_work_effort)
    #         # self.total_return = return_from_effort(self.agent_work_effort)
    #         # money_to_agent = self.agent_return_share * self.total_return + self.agent_fixed_pay
    #         agent.payoff = self.agent_fixed_pay - self.agent_work_cost - 20
    #         principal.payoff = (120 - self.agent_fixed_pay) * (self.agent_work_effort / 10)
    #     else:
    #         principal.payoff = Constants.reject_principal_pay
    #         agent.payoff = Constants.reject_agent_pay
    #
    # def return_share_as_percentage(self):
    #     return int(self.agent_return_share * 100)


class Player(BasePlayer):

    payoffmodule1 = models.CurrencyField()
    payoffmodule4 = models.CurrencyField()

    principal_quiz1 = models.IntegerField(
        choices=[
            [1, '(a) 50 dimes.'],
            [2, '(b) 100 dimes'],
            [3, '(c) 120 dimes']
        ],
        widget=widgets.RadioSelect,
        label="Question 1: What is the maximum amount of fixed payment you can send to Participant B?"
    )

    principal_quiz2 = models.FloatField(
        label="Question 2: If you offered Participant B 60 dimes and Participant B picks effort level 0.6, what is your "
              "payoff?"
    )

    principal_quiz3 = models.FloatField(
        label="Question 3: If you offered Participant B 60 dimes and Participant B picks effort level 0.6, what is "
              "Participant B's payoff?"
    )

    principal_quiz4 = models.IntegerField(
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

    agent_quiz1 = models.IntegerField(
        choices=[
            [1, '(a) 50 dimes'],
            [2, '(b) 10 dimes'],
            [3, '(c) 0 dimes']
        ],
        widget=widgets.RadioSelect,
        label="Question 1: What payoff do you and Participant A receive if you do not accept Participant B's proposal?"
    )

    agent_quiz2 = models.FloatField(
        label="Question 2: If Participant A offered you 60 dimes and you pick effort level 0.6, what is your "
              "payoff (in dimes)?"
    )

    agent_quiz3 = models.FloatField(
        label="Question 3: If Participant A offered you 60 dimes and you pick effort level 0.6, what is "
              "Participant A's payoff (in dimes)?"
    )

    def role(self):
        if self.id_in_group == 1:
            return 'principal'
        if self.id_in_group == 2:
            return 'agent'
