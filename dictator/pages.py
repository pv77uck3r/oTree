from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'player'
    form_fields = ['dictatorchoice']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def before_next_page(self):
        self.group.translate()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        return {
            'offer': Constants.endowment - self.group.kept,
        }


page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results
]
