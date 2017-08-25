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

        exp_log = self.participant.vars['exp_log']
        self.participant.vars['paid_period'] = random.randint(1,len(exp_log))

        return self.round_number == 1



class end(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        exp_log = self.participant.vars['exp_log']
        paid_period = self.participant.vars['paid_period']
        var_pay = exp_log[(paid_period-1)]['period_score']
        self.player.payoff = var_pay 

        self.session.config['participation_fee'] = c(self.session.config['participation_fee']).to_real_world_currency(self.session)
        self.session.config['real_world_currency_per_point'] = decimal.Decimal(1.00)
        
        return{
            'exp_log':exp_log,
            'debug':settings.DEBUG,
            'paid_period':self.participant.vars['paid_period'],
            'participation_fee':self.session.config['participation_fee'],
            'var_pay':var_pay,
            'total_pay':(var_pay+self.session.config['participation_fee']),

        }



page_sequence = [
    WaitPage,
    end
    ]






