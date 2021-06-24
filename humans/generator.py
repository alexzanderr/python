
from humanstree import *
from copy import deepcopy

path_to_files = r"\humans\files"

def GenerateHumans(self):
    # unknown wives from bible
    for counter in range(1, 2001):
        exec(f"unknown{counter} = Human(name=\"?\", sex=\"Female\", aged=500)")
        self.unknown_wives.append(eval(f"unknown{counter}"))

    self.iter_wives = iter(self.unknown_wives)

    adam = Human(name="Adam", sex="Male", aged=950)
    eva = Human(name="Eva", sex="Female", aged=900)
    self.humans.append(adam)
    self.humans.append(eva)
    adam.SetConnectionTo(eva)

    cain = Human(name="Cain", sex="Male", aged=700)
    abel = Human(name="Abel", sex="Male", aged=700)
    set = Human(name="Set", sex="Male", aged=700)
    self.humans.append(cain)
    self.humans.append(abel)
    self.humans.append(set)
    cain.SetParent(adam)
    abel.SetParent(adam)
    set.SetParent(adam)

    # cain's family
    cain.SetConnectionTo(self.iter_wives.__next__())

    enoh = Human(name="Enoh", sex="Male", aged=700)
    enoh.SetParent(cain)
    enoh.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(enoh)

    irad = Human(name="Irad", sex="Male", aged=700)
    irad.SetParent(enoh)
    irad.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(irad)

    maleleil1 = Human(name="Maleleil", sex="Male", aged=700)
    maleleil1.SetParent(irad)
    maleleil1.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(maleleil1)

    matusal = Human(name="Matusal", sex="Male", aged=700)
    matusal.SetParent(maleleil1)
    matusal.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(matusal)

    lameh1 = Human(name="Lameh", sex="Male", aged=700)
    lameh1.SetParent(matusal)
    self.humans.append(lameh1)
    lameh2 = Human(name="Lameh", sex="Male", aged=700)
    lameh2.SetParent(matusal)
    self.humans.append(lameh2)

    ada = Human(name="Ada", sex="Female", aged=700)
    lameh1.SetConnectionTo(ada)
    self.humans.append(ada)

    iabal = Human(name="Iabal", sex="Male", aged=700)
    iabal.SetParent(lameh1)
    self.humans.append(iabal)
    iubal = Human(name="Iubal", sex="Male", aged=700)
    iubal.SetParent(lameh1)
    self.humans.append(iubal)

    sela = Human(name="Sela", sex="Female", aged=700)
    lameh2.SetConnectionTo(sela)
    self.humans.append(sela)

    noema = Human(name="Noema", sex="Male", aged=700)
    noema.SetParent(lameh2)
    self.humans.append(noema)

    tubalcain = Human(name="Tubalcain", sex="Male", aged=700)
    tubalcain.SetParent(lameh2)
    self.humans.append(tubalcain)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # set's family
    set.SetConnectionTo(self.iter_wives.__next__())

    enos = Human(name="Enos", sex="Male", aged=700)
    enos.SetParent(set)
    enos.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(enos)

    cainan = Human(name="Cainan", sex="Male", aged=700)
    cainan.SetParent(enos)
    cainan.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(cainan)

    maleleil2 = Human(name="Maleleil", sex="Male", aged=700)
    maleleil2.SetParent(cainan)
    maleleil2.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(maleleil2)

    iared = Human(name="Iared", sex="Male", aged=700)
    iared.SetParent(maleleil2)
    iared.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(iared)

    enoh2 = Human(name="Enoh", sex="Male", aged=700)
    enoh2.SetParent(iared)
    enoh2.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(enoh2)

    matusalem = Human(name="Matusalem", sex="Male", aged=700)
    matusalem.SetParent(enoh2)
    matusalem.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(matusalem)

    lameh3 = Human(name="Lameh", sex="Male", aged=700)
    lameh3.SetParent(matusalem)
    lameh3.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(lameh3)

    noe = Human(name="Noe", sex="Male", aged=950)
    noe.SetParent(lameh3)
    noe.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(noe)

    sem = Human(name="Sem", sex="Male", aged=700)
    sem.SetParent(noe)
    sem.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(sem)

    ham = Human(name="Ham", sex="Male", aged=700)
    ham.SetParent(noe)
    ham.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(ham)

    iafet = Human(name="Iafet", sex="Male", aged=700)
    iafet.SetParent(noe)
    iafet.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(iafet)

    canaan = Human(name="Canaan", sex="Male", aged=700)
    canaan.SetParent(ham)
    canaan.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(canaan)

    # iafet sons
    with open(path_to_files + "iafet_sons.txt") as iafet_sons_file:
        next_son = iafet_sons_file.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(iafet)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = iafet_sons_file.readline()

    # gomer sons
    with open(path_to_files + "gomer_sons.txt") as gomer_sons_file:
        next_son = gomer_sons_file.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(gomer)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = gomer_sons_file.readline()

    # iavan sons
    with open(path_to_files + "iavan_sons.txt") as iavan_sons_file:
        next_son = iavan_sons_file.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(iavan)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = iavan_sons_file.readline()

    # ham sons
    with open(path_to_files + "ham_sons.txt") as ham_sons_file:
        next_son = ham_sons_file.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(ham)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = ham_sons_file.readline()

    # cush sons
    with open(path_to_files + "cush_sons.txt") as cush_sons:
        next_son = cush_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(cush)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = cush_sons.readline()

    # rama sons
    with open(path_to_files + "rama_sons.txt") as rama_sons:
        next_son = rama_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(rama)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = rama_sons.readline()

    # miztraim sons
    with open(path_to_files + "mitzraim_sons.txt") as mitzraim_sons:
        next_son = mitzraim_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(mitzraim)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = mitzraim_sons.readline()

    # canaan sons
    with open(path_to_files + "canaan_sons.txt") as canaan_sons:
        next_son = canaan_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(canaan)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = canaan_sons.readline()

    # sem sons
    with open(path_to_files + "sem_sons.txt") as sem_sons:
        next_son = sem_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(sem)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = sem_sons.readline()

    # aram sons
    with open(path_to_files + "aram_sons.txt") as aram_sons:
        next_son = aram_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(aram)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = aram_sons.readline()

    cainan2 = Human(name="Cainan", sex="Male", aged=120)
    cainan2.SetParent(eval("arfaxad"))
    cainan2.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(cainan2)

    shelah = Human(name="Shelah", sex="Male", aged=120)
    shelah.SetParent(cainan2)
    shelah.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(shelah)

    eber = Human(name="Eber", sex="Male", aged=120)
    eber.SetParent(shelah)
    eber.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(eber)

    peleg = Human(name="Peleg", sex="Male", aged=120)
    peleg.SetParent(eber)
    peleg.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(peleg)

    ioctan = Human(name="Ioctan", sex="Male", aged=120)
    ioctan.SetParent(eber)
    ioctan.SetConnectionTo(self.iter_wives.__next__())
    self.humans.append(ioctan)

    # ioctan sons
    with open(path_to_files + "ioctan_sons.txt") as ioctan_sons:
        next_son = ioctan_sons.readline()
        while next_son:
            if next_son != "__END__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(ioctan)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                self.humans.append(eval(f"{obj_name}"))
            next_son = ioctan_sons.readline()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # after a very long time

    # creating a shopping_list_path down from 'Peleg'
    small_sequence = []
    with open(path_to_files + "another_list.txt") as from_ragav:
        next_son = from_ragav.readline()
        while next_son:
            if next_son != "__end__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                small_sequence.append(eval(f"{obj_name}"))
            next_son = from_ragav.readline()

    # parent sequence creation
    for index in range(1, len(small_sequence)):
        small_sequence[index].SetParent(small_sequence[index - 1])
    # adding to humans
    for index in range(len(small_sequence)):
        self.humans.append(small_sequence[index])
    # connecting to the rest of the hierarchy
    peleg.SetChild(small_sequence[0])

    temp = []
    with open(path_to_files + "terah_sons.txt") as terah_sons:
        next_son = terah_sons.readline()
        while next_son:
            if next_son != "__end__":
                obj_name = deepcopy(next_son[:len(next_son) - 1])
                name = deepcopy(next_son.title()[:len(next_son) - 1])
                exec(f"{obj_name} = Human(name=\'{name}\', sex=\'Male\', aged=120)")
                exec(f"{obj_name}.SetParent(terah)")
                exec(f"{obj_name}.SetConnectionTo(self.iter_wives.__next__())")
                temp.append(eval(f"{obj_name}"))
            next_son = terah_sons.readline()

    serai = Human(name="Sarai", sex="Female", aged=100)
    # here we have an override, my friends
    serai.SetConnectionTo(eval("avram"))

    milca = Human(name="Milca", sex="Female", aged=100)
    milca.SetConnectionTo(eval("nahor"))

    lot = Human(name="Lot", sex="Male", aged=100)
    lot.SetParent(eval("haran"))

    # recreating a new one (visually creating)
    milca = Human(name="Milca", sex="Female", aged=100)
    milca.SetParent(eval("haran"))

    isca = Human(name="Isca", sex="Female", aged=100)
    isca.SetParent(eval("haran"))