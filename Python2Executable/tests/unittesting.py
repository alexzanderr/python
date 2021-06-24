
import os
import unittest
from Python2Executable.build import PyinstallerScript


project_folder = "D:/Alexzander__/programming/python/Python2Executable"
os.chdir(project_folder)

test_file = "D:/Alexzander__/programming/python/Python2Executable/simulate/simple_package/main.py"


class TestingPython2Executable(unittest.TestCase):

    def test_pyinstaller_script_function(self):
        # self.assertEqual(PyinstallerScript(test_file), True, "function is not returning True")
        pass




if __name__ == '__main__':
    unittest.main()
