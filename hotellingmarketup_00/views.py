from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, check_and_ok
from django.conf import settings
import time
import random

class holdon(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return {
            'debug':settings.DEBUG,
        }


class Init(Page):

    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'debug':settings.DEBUG,
        }



page_sequence = [
    holdon,
    Init,
    ]






