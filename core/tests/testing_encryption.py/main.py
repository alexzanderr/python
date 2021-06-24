

from core.encryption import *

class Testcase:
    def __init__(self, testcase, expected_result):
        self.testcase = testcase
        self.expected_result = expected_result



testcases = [
    Testcase(
        r"D:\Alexzander__\programming\python\core\tests\testing_encryption.py.py\90.png",
        None
    ),
    Testcase(r"D:\Alexzander__\programming\python\core\tests\testing_encryption.py.py\tree", None)
]


def test_all():
    for t in testcases:
        result = encrypt(t.testcase, 12)
        result = encrypt(t.testcase, 36)


if __name__ == '__main__':
    test_all()