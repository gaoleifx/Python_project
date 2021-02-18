####浅拷贝


class cpu:
    def __init__(self, name):
        self.name = name
        print('cpu name is......')
        #pass
class disk:
    def __init__(self, name):
        self.name = name
        print('disk name is......')
        #pass

class computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk
        
cpu1 = cpu('i9')
disk1 = disk('xijie')
comp1 = computer(cpu1, disk1)
print(cpu1.name)
print(comp1.cpu.name)

import copy
comp2 = copy.copy(comp1)
print(comp2.cpu.name)