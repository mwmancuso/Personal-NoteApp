"""Defines validators for use in rest of project.

Note that as a back-end, the validators in this project use Voluptuous.
This may be subject to change in the future, but currently the
Voluptuous library is used. For more information:
https://github.com/alecthomas/voluptuous

All custom validators should be implemented here and then used in
modules that require them. This module also defines helper functions
to use Voluptuous or other third-party validation engines. If the
project sprouts its own validation engine, it will be defined in this
module.

Wrap custom validators with message('<<<false message>>>') and truth
decorators:

@message('did-not-validate')
@truth
def TestFunction(string):
    ...
    return function_passed

Note that Voluptuous uses CamelCase validator names. To maintain
compatibility, CamelCase should be used for validators here.
"""

from voluptuous import message, truth

def list_errors(multiple_invalid_exception):
    """Helper function that extracts errors from MultipleInvalid.
    
    Takes the target assignment (e in except MultipleInvalid as e) and
    iterates error messages, returning tuple of error codes found.
    """
    
    error_list = []
    errors = multiple_invalid_exception.errors
    
    for error in errors:
        error_list.append(error.error_message)
    
    return tuple(error_list)