""" Utilities module for pytt_events"""


class FormatError(Exception):
    def __init__(self, value, message) -> None:
        self.value = value
        self.message = message
        super().__init__(value, message)


class ContextFormatError(FormatError):
    pass


class PropertiesFormatError(FormatError):
    pass
