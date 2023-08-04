class BlackjackError(Exception):
    pass

class NotEnoughChipsError(BlackjackError):
    pass

class InvalidBetError(BlackjackError):
    pass

# More custom exception classes if needed

