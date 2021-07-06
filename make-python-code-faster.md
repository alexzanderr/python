

# make python code faster

### use built-in functions and modules

### asign multiple variables on the same line

wrong
```python
firstName = "John"
lastName = "Henry"
city = "Manchester"
```

correct
```python
firstName, lastName, city = "John", "Henry", "Manchester"
```

### use list comprehension instead of for loops
wrong
```python
newlist = []
for i in range(1, 100):
    if i % 2 == 0:
        newlist.append(i**2)
```

correct
```python
newlist = [i**2 for i in range(1, 100) if i%2==0]
```

### import only what you need
wrong
```python
import math
value = math.sqrt(50)
```

correct
```python
from math import sqrt
value = sqrt(50)
```



### use join instead of + concatenation
wrong
```python
output = "Programming" + "is" + "fun
```

correct
```python
output = " ".join(["Programming" , "is", "fun"])
```

### use while loop instead of for loop
wrong
```python
start = 0
for i in range (1, 1000):
    start += 1
```

correct
```python
start = 0
index = 0
while index < 1000:
    start += 1

```


### dont use global variables

### Use 1 for infinity loops

Use while 1 instead of while True. It will reduce some runtime.

wrong
```python
while True:
    print("hello world")
```

correct
```python
while 1:
    print("hello world")
```


### use generators


### pypy (JIT compiler)

install pypy

run your code with pypy

the problem is taht pypy may not have many pypi external modules available

but you can install some of them with a command


### Cython (cython language)


### Numba library

make your function machine code at runtime


first you need to call the function to make machine code
this will take some seconds

but after machine binary, you can call the functions so fast


### use C/C++ written modules in your python code
examples:

- Numpy
- Scipy
- Pandas

### run code on CUDA cores

la asta ma chinui acum

install cuda and cuda-tools
```shell
sudo pacman -S cuda cuda-tools
```
