"""Handles errors for project.

This module defines error exceptions and allows views to call upon
classes to handle errors returned by those exceptions. All error text
is passed through a translation engine despite translations being
available or not. 
"""

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

class UserError(Exception):
    def __init__(self, *codes):
        self.codes = codes
    
    def __str__(self):
        return repr(self.codes)


class UserHandler(object):
    def __init__(self, codes):
        self.codes = codes
    
    def original(self):
        count = len(self.codes)
        count_str = ungettext(
            '%(count)d error occurred.',
            '%(count)d errors occurred.',
            count
        ) % {
            'count': count
        }
        
        return count_str, self.codes
    
    def translated(self):
        new_codes = list()
        
        count = len(self.codes)
        count_str = ungettext(
            '%(count)d error occurred.',
            '%(count)d errors occurred.',
            count
        ) % {
            'count': count
        }
        
        for code in self.codes:
            new_codes.append(_(code))
        
        return count_str, new_codes