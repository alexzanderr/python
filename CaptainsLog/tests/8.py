

flag = [True]

from module import Test

print(flag)
t = Test(flag)
flag[0] = False
print(t.flag)
# print(flag)
