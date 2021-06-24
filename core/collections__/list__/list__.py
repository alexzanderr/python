
"""
    This module contains an upgraded version of the
        primitive built-in list from python.
    This module also contains a custom-built error
        used only for the class List.

    Current state: in development.
"""


# python
import random
from sys import getsizeof

# core
from typing import Any, List, Union

from exceptions import EmptyListError

class List:
    """ This is the implementation of a better python list.
        Made in python ofc. """

    def __init__(self, *objects):
        self.container = []
        if len(objects) == 1:
            collection = objects[0]
            if type(collection) == list:
                self.container = list(collection)

            elif type(collection) == List:
                self.container = [x for x in collection.container]

            elif type(collection) == str:
                self.container = list(collection)

            elif type(collection) == int:
                while collection != 0:
                    self.container.append(collection % 10)
                    collection //= 10
                self.container = self.container[::-1]

        elif len(objects) > 1:
            for obj in objects:
                self.container.append(obj)


        # keeping dimension in a variable
        # for not calling __len__ so many times
        # it's inefficient...
        self.dimension = len(self.container)


    def append(self, argument, *arguments, **keywordArguments):
        """
            Adds an element to the end of the list, is
                compulsory to pass at least one argument to
                append List method.
            Adds multiple elements to the end of the list,
                if existent.
            With python built-in list you can't do that, fools.
            Adds multiple keyword arguments to the end
                of the list, if existent.
            Complexity: Dependent of the length of the
                *arguments and **keywordArguments.
        """
        counter = 0
        self.container.append(argument)
        for obj in arguments:
            self.container.append(obj)
            counter += 1
        if keywordArguments != {}:
            dictionary = {}
            for key, arg in keywordArguments.items():
                dictionary.update({key: arg})
            self.container.append(dictionary)
            counter += 1
        self.dimension += counter


    def append_front(self, argument, *arguments, **keywordArguments):
        """
            Adds an element to the beginning of the list,
                is compulsory to pass at least one argument to the append_front List method.
            Adds multiple elements to the beginning of the
                list, if existent.
            With python built-in list you can't do that, fools.
            Adds multiple keyword arguments to the
                beginning of the list, if existent.
            Complexity: Dependent of the length of the
                *arguments and **keywordArguments.
        """
        self.container.insert(0, argument)
        if arguments:
            counter = 1
            for obj in arguments:
                self.container.insert(counter, obj)
                counter += 1
        times = counter
        if keywordArguments != {}:
            dictionary = {}
            for key, argument in keywordArguments.items():
                dictionary.update({key: argument})
            self.container.insert(counter, dictionary)
            times += 1
        self.dimension += times


    def extend(self, iterable):
        if type(iterable) == List:
            self.container.extend(iterable.container)
        else:
            self.container.extend(iterable)


    def insert(self, index: int, *arguments, **keywordArguments):
        """ Inserting elements on the specified @param index.
            if index == len(self.container):
                then we append the element
            This function is capable of inserting an infinite number
            of arguments on the specified position and also keyword arguments.
        """
        if index == len(self.container):
            for argument in arguments:
                self.container.append(argument)
            if keywordArguments != {}:
                dictionary = {}
                for key, argument in keywordArguments.items():
                    dictionary.update({key: argument})
                self.container.append(dictionary)
        else:
            # we cant insert in an empty list on
            # a bigger index than zero
            if self.container == [] and index > 0:
                raise IndexError
            counter = 0
            for argument in arguments:
                self.container.insert(index + counter, argument)
                counter += 1
            if keywordArguments != {}:
                dictionary = {}
                for key, argument in keywordArguments.items():
                    dictionary.update({key: argument})
                self.container.insert(counter, dictionary)


    def remove(self, item):
        if self.container:
            raise EmptyListError
        self.container.remove(item)


    def pop(self, index=None):
        if self.container:
            raise EmptyListError

        if index is None:
            index = len(self.container) - 1
        if not (0 <= index < len(self.container)):
            raise IndexError

        self.dimension -= 1
        return self.container.pop(index)


    def clear(self):
        self.container.clear()
        self.dimension = 0


    def index(self, item, start=None, stop=None):
        """ Just the old list.index method with the same
            implementation. """
        if start is None and stop is None:
            return self.container.index(item)
        elif start is not None and stop is None:
            if type(start) != int:
                raise TypeError("@param start is not int.")
            if 0 <= start < len(self.container):
                return self.container.index(item, start=start)
            else:
                raise IndexError
        elif start is not None and stop is not None:
            if type(start) != int or type(stop) != int:
                raise TypeError("@params start and stop are not int")
            if 0 <= start < stop < len(self.container):
                return self.container.index(item, start, stop)
            else:
                raise IndexError
        else:
            raise TypeError


    def count(self, item):
        if self.container:
            raise EmptyListError
        return self.container.count(item)


    def sort(self, key=None, reverse=False):
        if self.container:
            raise EmptyListError
        self.container.sort(key=key, reverse=reverse)


    def reverse(self):
        if self.container:
            raise EmptyListError
        self.container.reverse()


    def copy(self):
        return self.container.copy()


    def __setitem__(self, *args):
        if len(args) == 1:
            instance = args[0]
            if type(instance) == list:
                self.container = instance
            elif type(instance) == List:
                self.container = instance.container
            else:
                raise TypeError

        elif len(args) == 2:
            if type(args[0]) == slice:
                if self.container:
                    raise EmptyListError

                sl = args[0]
                start, stop, step = sl.start, sl.stop, sl.step
                temporary = args[1]
                if type(temporary) == List:
                    temporary = temporary.container

                elif    type(temporary) != list and \
                        type(temporary) != tuple and \
                        type(temporary) != dict and \
                        type(temporary) != set:
                    self.container.append(temporary)
                    return

                if stop is None:
                    self.container[start::step] = temporary
                else:
                    self.container[start:stop - 1:step] = temporary
            elif type(args[0]) == int:
                if not (0 <= args[0] < len(self.container)):
                    raise IndexError
                self.container[args[0]] = args[1]


    def __delitem__(self, index):
        if type(index) == int:
            del self.container[index]
        elif type(index) == slice:
            start, stop, step = index.start, index.stop, index.step
            counter = 0
            if stop is None:
                for _ in range(start, len(self.container), step):
                    counter += 1
                del self.container[start::step]
            else:
                for _ in range(start, stop, step):
                    counter += 1
                del self.container[start:stop - 1:step]
            self.dimension -= counter
        else:
            raise TypeError


    def last_item(self):
        """ Returns the last element of the list.
            If its a stack its top of the list.
            If the list is empty raises EmptyListError"""
        if self.container:
            raise EmptyListError

        return self.container[len(self.container) - 1]


    def __str__(self):
        return self.container.__str__()


    def __repr__(self):
        return self.container.__repr__()


    def __eq__(self, instance):
        """
            equal
            ==
        """
        if type(instance) == list:
            return self.container == instance
        elif type(instance) == List:
            return self.container == instance.container
        else:
            raise TypeError


    def __gt__(self, instance):
        """
            greater than
            >

            :param instance:
            :return: None
        """
        if type(instance) == list:
            return self.container > instance
        elif type(instance) == List:
            return self.container > instance.container
        else:
            raise TypeError


    # less than <
    def __lt__(self, instance):
        if type(instance) == list:
            return self.container < instance
        elif type(instance) == List:
            return self.container < instance.container
        else:
            raise TypeError


    # less equal <=
    def __le__(self, instance):
        if type(instance) == list:
            return self.container <= instance
        elif type(instance) == List:
            return self.container <= instance.container
        else:
            raise TypeError


    # greater equal >=
    def __ge__(self, instance):
        if type(instance) == list:
            return self.container >= instance
        elif type(instance) == List:
            return self.container >= instance.container
        else:
            raise TypeError


    # not equal (not ==)
    def __ne__(self, instance):
        if isinstance(instance, list):
            return self.container != instance
        elif type(instance) == List:
            return self.container != instance.container
        else:
            raise TypeError


    def __del__(self):
        pass


    def format(self, *arguments):
        """
            Formating on list.
            This mechanism is applied only to empty dictionaries present in list.
        """
        empty_dicts = []
        for index in range(len(self.container)):
            if self.container[index] == {}:
                empty_dicts.append(index)
        for index, argument in zip(empty_dicts, arguments):
            self.container[index] = argument


    # calling str.format(List)
    def __format__(self, format_spec):
        return "<List self.container={}>".format(self.container)


    def __sizeof__(self):
        return object.__sizeof__(self) + \
            sum(getsizeof(value) for value in self.__dict__.values()) + \
            sum(getsizeof(item) for item in self.container)


    def __getitem__(self, index: int):
        if self.container:
            if type(index) == slice:
                start, stop, step = (index.start, index.stop, index.step)

                #TODO fix this
                # if (type(start) != int and type(start) != None) or (type(stop) != int and type(stop) != None) or (type(step) != int and type(step) != None):
                #     raise TypeError("Neither int or None")

                if stop is not None:
                    return self.container[start:stop:step]
                return self.container[start::step]

            elif type(index) == int:
                if 0 <= index < len(self.container):
                    return self.container[index]
                else:
                    raise IndexError
        else:
            raise EmptyListError("You cannot get an item of an empty list.")


    def __len__(self):
        return self.container.__len__()


    def __add__(self, instance):
        """ Returns the concatenation of both self and instance
            as a new List object.
            Example:
                l1 = [1, 2, 3, 4]
                l2 = [5, 6, 7, 8]
                l1 + l2 == [1, 2, 3, 4, 5, 6, 7, 8]
        """
        iterable = instance
        if type(instance) == List:
            iterable = instance.container
        elif type(instance) == tuple:
            pass
        elif type(instance) != list:
            raise TypeError

        return List(self.container + iterable)


    def __sub__(self, instance):
        """ Returns the elements which are existent in
            @param self and NOT existent in @param instance.
            Example:
                self=[4, 5, 6, 7]
                instance=[4, 5, 8, 9]
                self - instance == [6, 7]
        """
        if self.container == []:
            raise EmptyListError

        iterable = instance
        if type(instance) == List:
            iterable = instance.container
        elif type(instance) == tuple:
            pass
        elif type(instance) != list:
            raise TypeError

        return List([x for x in self.container if x not in iterable])


    def __mul__(self, instance):
        """ Application of * on List.
            if instance is integer:
                then we return multiplication of the
                self.container times integer

                Example:
                [1, 2] * 4 == [1, 2, 1, 2, 1, 2, 1, 2]

            if instance is list or List:
                then we return parallel multiplication of every
                element from self.container and instance

                Example:
                [3, 4] * [4, 5] == [12, 20]

                if their lengths are not equal
                    zip function is taking care of

                    Example:
                    [1, 2, 3, 4] * [2, 2] == [2, 4]
                    [5, 5] * [6, 7, 7, 7] == [30, 35]

            if we want to multiply the strings the list

                Example:
                ["s", "S", "a"] * 3 == ["sss", "SSS", "aaa"]
        """
        if self.container == []:
            raise EmptyListError

        if type(instance) == int:
            return List(self.container * instance)
        else:
            iterable = instance
            if type(instance) == List:
                iterable = instance.container
            elif type(iterable) == tuple:
                pass
            elif type(instance) != list:
                raise TypeError

            allstr_self = all(type(x) == str for x in self.container)
            allint_iterable = all(type(x) == int for x in iterable)

            # [1, 2, 3] * ["s1", "s2", "s3"]
            if allstr_self and allint_iterable:
                return List(list(map(lambda x: x[0] * x[1], zip(self.container, iterable))))
            else:
                allint_self = all(type(x) == int for x in self.container)
                allstr_iterable = all(type(x) == str for x in iterable)

                # ["s1", "s2", "s3"] * [1, 2, 3]
                if allint_self and allstr_iterable:
                    return List([tp[0] * tp[1] for tp in zip(self.container, iterable)])
                else:
                    allreal_self = all(type(x) == int or type(x) == float for x in self.container)
                    allreal_instance = all(type(x) == int or type(x) == float for x in self.container)

                    if allreal_self and allreal_instance:
                        return List([tp[0] * tp[1] for tp in zip(self.container, iterable)])
                    else:
                        raise ValueError("cant multiply non ints")


    def __div(self, instance, operator='/'):
        if self.container == []:
            raise EmptyListError

        instance_type = type(instance)
        if instance_type == int or instance_type == float:
            allreal_self = all(type(x) == int or type(x) == float for x in self.container)

            if allreal_self:
                if operator == '//':
                    return List([x // instance for x in self.container])
                return List([x / instance for x in self.container])
            else:
                raise ValueError("cant floor div non ints")
        else:
            iterable = instance
            if type(instance) == List:
                iterable = instance.container
            elif type(iterable) == tuple:
                pass
            elif type(instance) != list:
                raise TypeError

            allreal_self = all(type(x) == int or type(x) == float for x in self.container)
            allreal_iterable = all(type(x) == int or type(x) == float for x in self.container)

            if allreal_self and allreal_iterable:
                if operator == '//':
                    return List([tp[0] // tp[1] for tp in zip(self.container, iterable)])
                return List([tp[0] / tp[1] for tp in zip(self.container, iterable)])
            else:
                raise ValueError("cant floor div non ints by non ints")


    def __div__(self, instance):
        """ Dividing every int element of the
                self.container with instance.
            Or dividing every int or float elem
                of the self.container with every
                element of the instance.
        """
        return self.__div(instance)


    def __floordiv__(self, instance):
        """ Dividing every int element of the
                self.container with instance.
            Or dividing every int or float elem
                of the self.container with every
                element of the instance.
        """
        return self.__div(instance, operator='//')


    def __mod__(self):
        raise NotImplementedError


    def __pow__(self):
        raise NotImplementedError


    def __rshift__(self, instance):
        if self.container == []:
            raise EmptyListError

        instance_type = type(instance)
        if instance_type != int:
            raise TypeError
        if instance < 0:
            raise ValueError
        result = self.container.copy()

        if instance == 0:
            return List(result)
        times = instance % len(self.container)
        if times == 0:
            return List(result)

        for _ in range(times):
            last = result[len(result) - 1]
            result = [last] + result[:len(result) - 1]
        return List(result)


    def __lshift__(self, instance):
        if self.container == []:
            raise EmptyListError

        instance_type = type(instance)
        if instance_type != int:
            raise TypeError
        if instance < 0:
            raise ValueError

        result = self.container.copy()
        if instance == 0:
            return List(result)
        times = instance % len(self.container)
        if times == 0:
            return List(result)

        for _ in range(times):
            first = result[0]
            result = result[1: ] + [first]
        return List(result)

    # common elements from both lists
    def __and__(self, instance):
        iterable = instance
        if type(instance) == List:
            iterable = instance.container
        elif type(iterable) == tuple:
            pass
        elif type(instance) != list:
            raise TypeError

        return List([x for x in self.container if x in iterable])

    # simmetric difference
    def __xor__(self, instance):
        iterable = instance
        if type(instance) == List:
            iterable = instance.container
        elif type(iterable) == tuple:
            pass
        elif type(instance) != list:
            raise TypeError

        from_self = List([x for x in self.container if x not in iterable])
        from_iterable = List([x for x in iterable if x not in self.container])
        return from_self + from_iterable


    def __or__(self, instance):
        raise NotImplementedError


    # plus equal (+=)
    def __iadd__(self, instance):
        self = self + instance
        return self


    # minus equal (-=)
    def __isub__(self, instance):
        self = self - instance
        return self


    def __imul__(self, instance):
        self = self * instance
        return self


    def __idiv__(self, instance):
        self = self / instance
        return self


    def __ifloordiv__(self, instance):
        self = self // instance
        return self


    def __imod__(self, instance):
        self = self % instance
        return self

    def __pow__(self, instance):
        self = self ** instance
        return self


    def __irshift__(self, instance):
        self = self >> instance
        return self


    def __ilshift__(self, instance):
        self = self << instance
        return self


    def __iand__(self, instance):
        self = self & instance
        return self


    def __ixor__(self, instance):
        self = self ^ instance
        return self


    def __ior__(self, instance):
        self = self | instance
        return self


    def __filter(self, operator='>'):
        result = []
        for x in self.container:
            if isinstance(x, (float, int)):
                if operator == '>':
                    if x > 0:
                        # making negatives from positives
                        result.append(-x)
                    else:
                        result.append(x)
                elif operator == '<':
                    if x < 0:
                        # making positives from negatives
                        result.append(-x)
                    else:
                        result.append(x)
                else:
                    raise TypeError("bad operator...")
            else:
                result.append(x)
        return List(result)


    def __neg__(self):
        """ Negative version of all positive int elements.
            If non int elements are existent then
                we do nothing to them.
            Does not modify in-place!
        """
        return self.__filter()


    def __pos__(self):
        """ Positive version of all negative int elements.
            If non int elements are existent then
                we do nothing to them.
            Does not modify in-place!
        """
        return self.__filter(operator='<')


    def __abs__(self):
        return self.__pos__()


    # applies ~ to every integer in the self.container
    def __invert__(self):
        for index in range(len(self.container)):
            if type(self.container[index]) == int:
                self.container[index] = ~self.container[index]
        return self


    def __complex__(self):
        # for index in range(len(self.container)):
        #     if type(self.container[index]) == int or \
        #        type(self.container[index]) == float:
        #         self.container[index] = complex(self.container[index])
        # return self
        raise NotImplementedError


    def __int__(self):
        raise NotImplementedError


    def __long__(self):
        raise NotImplementedError


    def __float__(self):
        raise NotImplementedError


    def __oct__(self):
        raise NotImplementedError


    def __hex__(self):
        raise NotImplementedError


    def __iter__(self):
        return iter(self.container)


    def __dir__(self):
        return dir(List)


    def sorted(self, *, key=None, reverse=False):
        return sorted(self.container, key=key, reverse=reverse)


    def type(self):
        return "<class 'List'>"


    def __contains__(self, item):
        """ 'in' operator """
        if not self.container:
            raise EmptyListError
        return item in self.container


    def __delattr__(self, name):
        if name == 'container':
            raise PermissionError("How dare you delete the best list ever!?")
        else:
            print("eh, that dimension was useless...")
            object.__delattr__(self, name)


    def __hash__(self):
        pass


if __name__ == '__main__':
    # ultra_list = List("12312312")
    # ultra_list.append(123)
    # ultra_list.append_front(random.randrange(0, 10))
    # print(ultra_list.count(123))
    # print(ultra_list.last_item())
    # print(ultra_list.__dict__)
    # print(ultra_list.count(123))
    # print(ultra_list)
    pass
