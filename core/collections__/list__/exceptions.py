


class ListException(Exception):
    def __init__(self, message="", exception_type="ListException"):
        self.message = message
        self.exception_type = exception_type

    def __str__(self):
        return f"<{self.exception_type} message=\"{self.message}\">"


class EmptyListError(ListException):
    def __init__(self, message="", exception_type="EmptyListError") -> None:
        super().__init__(message, exception_type)



print("this is a very pleasure for programming, "
      "hello my name is andrew and i like "
      "programming")


if __name__ == '__main__':
    test = EmptyListError("test")
    print(test)
