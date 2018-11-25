from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class QuizA(Page):

    def is_displayed(self):
        return self.player.role() == 'agent'

    form_model = 'player'
    form_fields = ['agent_quiz1', 'agent_quiz2', 'agent_quiz3']


class QuizB(Page):

    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'player'
    form_fields = ['principal_quiz1', 'principal_quiz2', 'principal_quiz3', 'principal_quiz4']


class Offer(Page):
    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'group'
    form_fields = ['agent_fixed_pay1', 'agent_fixed_pay2', 'agent_fixed_pay3', 'agent_fixed_pay4', 'agent_fixed_pay5']


# class OfferWaitPage(WaitPage):
#     def vars_for_template(self):
#         if self.player.role() == 'agent':
#             body_text = "You are Participant B. Waiting for Participant A to propose a contract."
#         else:
#             body_text = "Waiting for Participant B."
#         return {'body_text': body_text}


class Accept(Page):
    def is_displayed(self):
        return self.player.role() == 'agent'

    form_model = 'group'
    form_fields = ['contract_accepted_1', 'agent_work_effort_1', 'contract_accepted_2', 'agent_work_effort_2',
                   'contract_accepted_3', 'agent_work_effort_3', 'contract_accepted_4', 'agent_work_effort_4',
                   'contract_accepted_5', 'agent_work_effort_5', 'contract_accepted_6', 'agent_work_effort_6',
                   'contract_accepted_7', 'agent_work_effort_7', 'contract_accepted_8', 'agent_work_effort_8',
                   'contract_accepted_9', 'agent_work_effort_9', 'contract_accepted_10', 'agent_work_effort_10',
                   'contract_accepted_11', 'agent_work_effort_11', 'contract_accepted_12', 'agent_work_effort_12',
                   'contract_accepted_13', 'agent_work_effort_13', ]

    #timeout_seconds = 3 * 60
    timeout_submission = {
        'contract_accepted': False,
        'agent_work_effort': 1,
    }

    def error_message(self, values):
        if values['contract_accepted'] and values['agent_work_effort'] == None:
            return 'If you accept the contract, you must select a level of effort.'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [Introduction,
                 QuizA,
                 QuizB,
                 Offer,
                 Accept
                 ]
