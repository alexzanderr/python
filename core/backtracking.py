
"""
    core/backtracking.py

    this is the old style of C++
    in using backtracking implemented
    in python3

    author: @alexzander
"""


class Permutations:
    def __init__(self, dimension=3):
        self.dimension = dimension # old 'N'
        self.position = 0 # old 'K'
        self.solution = [0 for _ in range(self.dimension)] # old 'stiva'
        # these are old elements from c++

    def Init(self):
        self.solution[self.position] = 0

    def HasSuccesor(self):
        if self.solution[self.position] < self.dimension:
            self.solution[self.position] += 1
            return True
        else:
            return False

    def ValidSolution(self):
        for index in range(0, self.position):
            if self.solution[index] == self.solution[self.position]:
                return False
        return True

    def Solution(self):
        return self.dimension - 1 == self.position

    def Permutations(self):
        self.__permutations()
        self.__init__()

    def __permutations(self):
        self.position = 0
        self.Init()
        while self.position > -1:
            while True:
                succesor = self.HasSuccesor()
                if not succesor or self.ValidSolution():
                    break
            if succesor:
                if self.Solution():
                    print(self.solution)
                else:
                    self.position += 1
                    self.Init()
            else:
                self.position -= 1


class Arrangements:
    def __init__(self, dimension, solution_size):
        self.dimension = dimension  # old 'N'
        self.position = 0  # old 'K'
        self.solution = [0 for _ in range(self.dimension)]  # old 'stiva'
        # these are old elements from c++
        # we have in extra a different size for every solution
        self.solution_size = solution_size

    def Init(self):
        self.solution[self.position] = 0

    def HasSuccesor(self):
        if self.solution[self.position] < self.dimension:
            self.solution[self.position] += 1
            return True
        else:
            return False

    def ValidSolution(self):
        for index in range(self.position):
            if self.solution[index] == self.solution[self.position]:
                return False
        return True

    def Solution(self):
        return self.solution_size - 1 == self.position

    def Arragements(self):
        self.__arrangements()
        self.__init__(self.dimension, self.solution_size)

    def __arrangements(self):
        self.position = 0
        self.Init()
        while self.position > -1:
            while True:
                succesor = self.HasSuccesor()
                if not succesor or self.ValidSolution():
                    break
            if succesor:
                if self.Solution():
                    print(self.solution[:self.solution_size])
                else:
                    self.position += 1
                    self.Init()
            else:
                self.position -= 1


class Combinations:
    def __init__(self, dimension, solution_size):
        self.dimension = dimension  # old 'N'
        self.position = 0  # old 'K'
        self.solution = [0 for _ in range(self.dimension)]  # old 'stiva'
        # these are old elements from c++
        # we have in extra a different size for every solution
        self.solution_size = solution_size

    def Init(self):
        if self.position == 0:
            self.solution[0] = 0
        else:
            self.solution[self.position] = self.solution[self.position - 1]

    def HasSuccesor(self):
        if self.solution[self.position] < self.dimension:
            self.solution[self.position] += 1
            return True
        return False

    def ValidSolution(self):
        for index in range(self.position):
            if self.solution[index] == self.solution[self.position]:
                return False
        return True

    def Solution(self):
        return self.solution_size - 1 == self.position

    def Combinations(self):
        self.__combinations()
        self.__init__(self.dimension, self.solution_size)

    def __combinations(self):
        self.position = 0
        self.Init()
        while self.position > -1:
            while True:
                succesor = self.HasSuccesor()
                if not succesor or self.ValidSolution():
                    break
            if succesor:
                if self.Solution():
                    print(self.solution[:self.solution_size])
                else:
                    self.position += 1
                    self.Init()
            else:
                self.position -= 1


class NumberSumPartitions:
    def __init__(self, number):
        self.number = number
        self.dimension = number
        self.position = 0
        self.solution = [0 for _ in range(number)]
        self.index = 0
        self.solutions = []

    def Init(self):
        self.solution[self.position] = 0

    def HasSuccesor(self):
        if self.solution[self.position] < self.dimension:
            self.solution[self.position] += 1
            return True
        return False

    def Solution(self):
        partition_sum = 0
        for index in range(len(self.solution)):
            partition_sum += self.solution[index]
            if partition_sum == self.number:
                self.index = index
                solut = sorted(self.solution[:index + 1])
                if solut not in self.solutions:
                    print(solut)
                    self.solutions.append(solut)
                return True
        return False

    def Partitions(self):
        self.__partitions()
        self.__init__(self.number)

    def __partitions(self):
        while self.position > -1:
            succesor = self.HasSuccesor()
            if succesor:
                if self.Solution():
                    # automatically prints solution
                    pass
                else:
                    if self.position < len(self.solution) - 1:
                        self.position += 1
                        self.Init()
            else:
                self.position -= 1


class MadameBacktracking:
    def __init__(self, dimension=3):
        self.dimension = dimension
        self.position = 0
        self.solution = [0 for _ in range(self.dimension)]

    def Init(self):
        self.solution[self.position] = 0

    def HasSuccesor(self):
        if self.solution[self.position] < self.dimension:
            self.solution[self.position] += 1
            return True
        return False

    def ValidSolution(self):
        for index in range(self.position):
            if self.solution[index] == self.solution[self.position] \
                or abs(self.solution[self.position] - self.solution[index]) == self.position - index:
                return False
        return True

    def Solution(self):
        return self.dimension - 1 == self.position

    def MadameBacktracking(self):
        self.__madame_backtracking()
        self.__init__(self.dimension)

    def __madame_backtracking(self):
        self.position = 0
        self.Init()
        while self.position > -1:
            while True:
                succesor = self.HasSuccesor()
                if not succesor or self.ValidSolution():
                    break
            if succesor:
                if self.Solution():
                    solution = list(map(lambda item: item - 1, self.solution))
                    mat_visualize = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
                    for x, y in zip(range(self.dimension), solution):
                        mat_visualize[x][y] = 1
                    for line in mat_visualize:
                        print(line)
                    print()
                else:
                    self.position += 1
                    self.Init()
            else:
                self.position -= 1


class PermutationsRecursive:
    def __init__(self, dimension):
        self.dimension = dimension
        self.position = 0
        self.solution = [0 for _ in range(self.dimension)]
        self.solutions = []
        self.__permutations(self.position)

    def Continue(self, position):
        for index in range(position):
            if self.solution[index] == self.solution[position]:
                return False
        return True

    def __permutations(self, position):
        if position == self.dimension:
            self.solutions.append(list(self.solution))
        else:
            for index in range(1, self.dimension + 1):
                self.solution[position] = index
                if self.Continue(position):
                    self.__permutations(position + 1)

    def __iter__(self):
        if self.solutions:
            return iter(self.solutions)
        return []

    def __str__(self):
        if self.solutions:
            for permutation in self:
                print(permutation)
        else:
            print()
        return ""

    def __set__(self, __object):
        if self.solutions:
            from copy import deepcopy
            __object = deepcopy(self.solutions)
        else:
            __object = []



# TESTING
if __name__ == '__main__':
    Permutations(6).Permutations()