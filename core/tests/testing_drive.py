
import unittest
from core.drive import copy
from core.aesthetics import *

class TestingDrivepy(unittest.TestCase):

    def test_copy_function(self):
        source_tests = [
            r"D:\Alexzander__\programming\python\Python2Executable",
            r"D:\Alexzander__\programming\python\byzantion",
            r"D:\Alexzander__\programming\python\BizidayNews",
            r"D:\Alexzander__\programming\python\bitcoin",
            r"D:\Alexzander__\programming\python\core",
            r"",
            r"",
        ]

        destination_tests = [
            r"D:\Alexzander__\programming\python\testing_copy_func",
            r"D:\Alexzander__\programming\python\testing_copy_func",
            r"D:\Alexzander__\programming\python\testing_copy_func",
            r"D:\Alexzander__\programming\python\testing_copy_func",
            r"D:\Alexzander__\programming\python\testing_copy_func",
            r"",
            r"",
        ]

        for index, (source, destination) in enumerate(
            zip(source_tests, destination_tests),
            start=1
        ):
            if source != r"" and destination != r"":
                try:
                    result = self.assertEqual(
                        copy(
                            source,
                            destination,
                            open_destination_when_done=False,
                            __print=False),
                        True
                    )
                    if result is None:
                        print(f"Test #{index} {green_bold('passed')}.")

                except BaseException as exception:
                    print(red_bold(type(exception)))
                    print(red_bold(exception))
                    print(f"Test #{index} DIDNT pass!")


if __name__ == '__main__':
    unittest.main()
