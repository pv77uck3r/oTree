from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def vars_for_template(self):
        app_seq = self.session.config['app_sequence']
        return {
            'Part': app_seq.index('criminal_principal_agent2_ALT_ORDER')
        }

    def before_next_page(self):
        self.player.record_number()


class QuizA(Page):

    def is_displayed(self):
        return self.player.role() == 'agent'

    form_model = 'player'
    form_fields = ['agent_quiz1', 'agent_quiz2', 'agent_quiz3']

    def agent_quiz1_error_message(self, value):
        if value != 3:
            return 'Question 1 is incorrect. Please try again.'

    def agent_quiz2_error_message(self, value):
        if value != 38:
            return 'Question 2 is incorrect. Please try again.'

    def agent_quiz3_error_message(self, value):
        if value != 36:
            return 'Question 3 is incorrect. Please try again.'


class QuizP(Page):

    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'player'
    form_fields = ['principal_quiz1', 'principal_quiz2', 'principal_quiz3', 'principal_quiz4']

    def principal_quiz1_error_message(self, value):
        if value != 3:
            return 'Question 1 is incorrect. Please try again.'

    def principal_quiz2_error_message(self, value):
        if value != 36:
            return 'Question 2 is incorrect. Please try again.'

    def principal_quiz3_error_message(self, value):
        if value != 38:
            return 'Question 3 is incorrect. Please try again.'

    def principal_quiz4_error_message(self, value):
        if value != 2:
            return 'Question 3 is incorrect. Please try again.'



class Offer(Page):
    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'group'
    form_fields = ['agent_fixed_pay_1', 'agent_fixed_pay_2', 'agent_fixed_pay_3', 'agent_fixed_pay_4',
                   'agent_fixed_pay_5']


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
    form_fields = ['agent_work_effort_1', 'agent_work_effort_2', 'agent_work_effort_3', 'agent_work_effort_4',
                   'agent_work_effort_5', 'agent_work_effort_6', 'agent_work_effort_7', 'agent_work_effort_8',
                   'agent_work_effort_9', 'agent_work_effort_10', 'agent_work_effort_11', 'agent_work_effort_12',
                   'agent_work_effort_13', ]

    #timeout_seconds = 3 * 60
    timeout_submission = {
        'contract_accepted': False,
        'agent_work_effort': 1,
    }

    # def error_message(self, values):
    #     if values['contract_accepted'] and values['agent_work_effort'] == None:
    #         return 'If you accept the contract, you must select a level of effort.'

    def before_next_page(self):
        self.group.set_accepts()


class KeepDecisions(WaitPage):

    def after_all_players_arrive(self):
        self.group.keep_decisions()


class SetGroups2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_groups_2()


class Results(Page):
    pass


page_sequence = [SetGroups2,
                 Introduction,
                 QuizA,
                 QuizP,
                 Offer,
                 Accept,
                 KeepDecisions
                 ]
