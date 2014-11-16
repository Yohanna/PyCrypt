class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class TypeError(Error):
    """Exception raised for errors in function modes.

    Attributes:
        type -- Type which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, type, msg):
        self.type = type
        self.msg = msg