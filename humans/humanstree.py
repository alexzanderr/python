
from core.aesthetix import *
from core.system import *

class Human:
    def __init__(self, name=None, gender=None, aged=None):
        self.name = name
        self.gender = gender
        self.aged = aged
        self.connection = None
        self.childs = {}
        self.parents = {}
        self.child_objects = []
        self.parent_objects = []

    def SetConnectionTo(self, partner):
        """ Sets a bonded connection between to existences. """
        if self.gender is None or partner.gender is None:
            raise ValueError
        if self.gender == partner.gender:
            raise AttributeError("Dude thats homo gay stuff lmao")

        self.connection = partner
        partner.connection = self

    def SetChild(self, child):
        if self.connection is None:
            raise ValueError

        self.child_objects.append(child)
        child.parent_objects.append(self)

        if self.childs:
            self.childs[self.connection.name] += [child.name]
            self.connection.childs[self.name] += [child.name]
            if self.gender == "Male":
                child.parents["Father"] = self.name
                child.parents["Mother"] = self.connection.name
            elif self.gender == "Female":
                child.parents["Father"] = self.connection.name
                child.parents["Mother"] = self.name
        else:
            self.childs[self.connection.name] = [child.name]
            self.connection.childs[self.name] = [child.name]
            if self.gender == "Male":
                child.parents["Father"] = self.name
                child.parents["Mother"] = self.connection.name
            elif self.gender == "Female":
                child.parents["Father"] = self.connection.name
                child.parents["Mother"] = self.name

    def SetParent(self, parent):
        if parent.connection is None:
            raise ValueError

        self.parent_objects.append(parent)
        parent.child_objects.append(self)
        if parent.gender == "Male":
            self.parents["Father"] = parent.name
            self.parents["Mother"] = parent.connection.name
            if parent.childs:
                parent.childs[parent.connection.name] += [self.name]
                parent.connection.childs[parent.name] += [self.name]
            else:
                parent.childs[parent.connection.name] = [self.name]
                parent.connection.childs[parent.name] = [self.name]
        elif parent.gender == "Female":
            self.parents["Father"] = parent.connection.name
            self.parents["Mother"] = parent.name
            if parent.childs:
                parent.childs[parent.connection.name] += [self.name]
                parent.connection.childs[parent.name] += [self.name]
            else:
                parent.childs[parent.connection.name] = [self.name]
                parent.connection.childs[parent.name] = [self.name]

    def __str__(self):
        not_defined = "not defined yet"

        name = not_defined
        gender = not_defined
        aged = not_defined
        conn = not_defined
        childs = not_defined
        parents = not_defined

        if self.name:
            name = self.name
        if self.gender:
            gender = self.gender
        if self.aged:
            aged = self.aged
        if self.connection:
            conn = self.connection.name
        if self.childs:
            childs = ", ".join(self.childs[list(self.childs.keys())[0]])
        if self.parents:
            parents = self.parents

        result = \
        f"""
        Name: {name}
        Sex: {gender}
        Aged: {aged}
        Connection: {conn} 
        Childs: {childs}
        Parents: {parents}
        """
        return result

class HumansTree:

    humans = []
    unknown_wives = []

    def __init__(self):
        from generator import GenerateHumans
        GenerateHumans(self)

    # unicode(9472 -> 9599) useful connection symbols
    conect_symbol = f"{chr(9552)}{chr(9523)}{chr(9552)}"
    child_symbol = f"{chr(9495)}{chr(9552)}"

    def Display(self):
        print(f"Adam {self.conect_symbol} Eva")
        starting_space = ' ' * 7
        for i in range(2, 5):
            self.Tree(self.humans[i], starting_space)

    def Tree(self, root, spacing_tool= ''):
        if root.connection:
            print(spacing_tool + f"{self.child_symbol} {root.name} {self.conect_symbol} {root.connection.name}")
            for child in root.child_objects:
                self.Tree(child, spacing_tool + 5 * ' ' + len(root.name) * ' ')
        else:
            print(spacing_tool + f"{self.child_symbol} {root.name}")

    def GetRoot(self):
        if self.humans:
            return self.humans[0]
        return None

def DisplayEndMessage(message, times=3, iterations=5):
    print("\n\n")
    for t in range(times):
        for i in range(iterations):
            print(message, end=" ")
        print()
    input()

if __name__ == '__main__':
    clearscreen()
    tree = HumansTree()
    tree.Display()

    # aesthetics
    print_message = "The entire human hierarchy from universe origins to present."
    DisplayEndMessage(print_message)

    # TODO
    # add some functionalities:
    # 1. add manually people to the tree from keyborad
    # 2. have multiple trees separated from the original and a function that connects them to the original
    # we need this program to be available for my future family tree