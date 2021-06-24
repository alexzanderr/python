

class DictException(Exception):
    def __init__(self, message=""):
        self.message = message


class EmptyDictError(DictException):
    pass