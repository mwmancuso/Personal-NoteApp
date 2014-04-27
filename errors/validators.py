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
import re

# Authentication

# Validation regex constants
VALID_USERNAME_REGEX = re.compile(r'^[A-Za-z0-9_]{1,50}$')
VALID_NAME_REGEX = re.compile(r'^[A-Za-z0-9]{1,30}$')
VALID_EMAIL_REGEX = re.compile(r'^(?=[^@]+@[^@]+(\.[^@]+)+).{1,75}$')
VALID_PASSWORD_REGEX = re.compile(r"""
    ^
     (?P<phrase>     # Alternate condition: matches any character...
      [!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{\|}~ A-Za-z0-9]
      {16,50}        # ...As long as it is 16 to 50 characters
     )
    |
     (?=             # Condition 1 lookahead assertion
      .*             # Matches all characters until...
      (?P<lower>     # Group for checking lower case letters
       [a-z]         # ...Matches a lower case letter
      )
     )?              # Makes lookahead optional; will be checked later
     (?=             # Condition 2 lookahead assertion
      .*
      (?P<upper>     # Group for matching upper case letters
       [A-Z]
      )
     )?
     (?=             # Condition 3 lookahead assertion
      .*
      (?P<number>    # Group for matching digits
       [0-9]
      )
     )?
     (?=             # Condition 4 lookahead assertion
      .*
      (?P<special>   # Group for matching special characters
       [!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{\|}~ ]
      )
     )?
     [!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{\|}~ A-Za-z0-9]
     {8,50}        # Asserts that password is 8-50 characters
    $
""", re.VERBOSE)
VALID_TOKEN_REGEX = re.compile(r'^[A-Za-z0-9]{1,50}$')

def list_errors(multiple_invalid_exception):
    """Helper function that extracts errors from MultipleInvalid.

    Takes the target assignment (e in except MultipleInvalid as e) and
    iterates error messages, returning tuple of error codes found.
    """

    if multiple_invalid_exception.error_message == 'extra keys not allowed':
        raise multiple_invalid_exception

    error_list = []
    errors = multiple_invalid_exception.errors

    for error in errors:
        error_list.append(error.error_message)

    return tuple(error_list)


@truth
def Password(password):
    """Validator that checks to make sure a password is valid."""

    match = VALID_PASSWORD_REGEX.match(password.strip())

    if not match:
        return False

    captures = match.groupdict()
    condition_keys = ('lower', 'upper', 'number', 'special')
    num_conditions = 3 # Number of conditions required

    if captures['phrase']:
        return True
    else:
        # List comprehension that sums the number of met conditions
        count = sum(1 for key in captures.keys() if key in condition_keys\
                    and captures[key])

        if count >= num_conditions:
            return True

    return False