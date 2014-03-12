"""Handles errors for project.

This module allows views to call upon classes to handle errors returned
by custom exceptions. All error text is passed through a translation
engine despite translations being available or not.
"""

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

class UserHandler(object):
    """Handles the capture and translation of user errors.
    
    Accepts unpacked list of error codes as only arguments.
    """
    
    def __init__(self, *args):
        self.codes = args
    
    def count(self):
        """Returns count of errors.
        
        Essentially wrapper for len(inst.codes).
        """
        
        return len(self.codes)
    
    def count_string(self):
        """Returns translated string of count of errors."""
        count = len(self.codes)
        count_str = ungettext(
            '%(count)d error occurred.',
            '%(count)d errors occurred.',
            count
        ) % {
            'count': count
        }
        
        return count_str
    
    def originals(self):
        """Returns tuple of error codes.
        
        Currently an alias for self.codes. May push more functionality
        in the future.
        """
        
        return self.codes
    
    def translations(self):
        """Returns tuple of correctly translated error strings."""
        
        translated = list()
        
        for code in self.codes:
            # _(code) indicates a translation of code be provided
            translated.append(_(code))
        
        return tuple(translated)
    
    def code_translations(self):
        """Returns dict containing strings with associated codes."""
        
        translated = dict()
        
        for code in self.codes:
            translated[code] = _(code)
        
        return translated
    
    def verbose(self):
        """Returns dictionary of verbose data.
        
        verbose()['count'] is count of errors.
        verbose()['count_string'] is count string.
        verbose()['original'] is original tuple of codes.
        verbose()['translated'] is new tuple of translated codes.
        
        Currently a wrapper for all other functions but may provide
        extended verbosity.
        """
        
        verbose_return = {
            'count': self.count()
            'count_string': self.count_string()
            'originals': self.original()
            'translations': self.translations()
            'code_translations': self.code_translations()
        }
        
        return verbose_return