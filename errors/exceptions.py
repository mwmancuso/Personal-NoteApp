"""Defines custom exceptions for project."""

class UserError(Exception):
    """Exception for raising user errors.

    User errors are errors invoked by users and which are caught by
    this exception to return valid error messages. Exception is called
    with arguments being a list of codes. Those codes may be retrieved
    by using inst.codes.
    """

    def __init__(self, *codes):
        self.codes = codes

    def __str__(self):
        return repr(self.codes)