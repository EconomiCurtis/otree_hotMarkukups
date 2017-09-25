from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, check_and_ok
from django.conf import settings
import time
import random
import decimal

class WaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number == 1



class end(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        self.session.config['participation_fee'] = c(self.session.config['participation_fee']).to_real_world_currency(self.session)
        
        var_pay = 0

        # get period scores
        period_scores = self.participant.vars['period_scores']
        for period in period_scores:
            period['paid_period'] = False
        period_scores[self.player.paidPeriod-1]['paid_period'] = True

        var_pay = period_scores[self.player.paidPeriod-1]['score'] 
        var_pay_cash = decimal.Decimal(var_pay) * decimal.Decimal(self.session.config['real_world_currency_per_point'])
        var_pay_cash = c(var_pay_cash).to_real_world_currency(self.session)

        total_pay = c(var_pay_cash + self.session.config['participation_fee']).to_real_world_currency(self.session)
        
        self.player.payoff = total_pay

        return{
            'debug':settings.DEBUG,
            'participation_fee':self.session.config['participation_fee'],
            'total_pay':total_pay,
            'period_scores':period_scores,
            'paid_period':self.player.paidPeriod,
            'var_pay':var_pay,
            'real_world_currency_per_point':self.session.config['real_world_currency_per_point'],
            'var_pay_cash':var_pay_cash,

        }



page_sequence = [
    WaitPage,
    end
    ]






