

import 


print("hello world")

long_string = "salutare si bine te-am gasit"
print(long_string)
print(long_string[::-1])
print(long_string.replace("a", "___-asdasd").replace("si", "SI MAI MARE"))


class JustAClass:
    def __init__(self):
        self.variable = "my name is andrew"


    def function_in_class(self):
        for _ in range(100):
            print("im just a range(100)")


from math import sqrt
def square_root(x):
    return sqrt(x)


if __name__ == '__main__':
    j = JustAClass()
    print(j)
    print(j.__init__)
    print(j.variable)
    j.function_in_class()
