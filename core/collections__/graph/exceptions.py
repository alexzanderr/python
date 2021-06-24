

class GraphException(Exception):
    def __init__(self, message=""):
        self.message = message


class VertexNotFoundError(GraphException):
    pass