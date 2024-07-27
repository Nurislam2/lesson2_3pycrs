class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print("для сложения введите 1\n"
              "для вычитания введите 2\n"
              "для умножения введите 3\n"
              "для деления введите 4")
        n = input()
        if int(n) == 1:
            print(self.__cpu + self.__memory)
        elif int(n) == 2:
            print(self.__memory - self.__cpu)
        elif int(n) == 3:
            print(self.__memory * self.__cpu)
        else:
            print(self.__memory / self.__cpu)

    def __str__(self):
        return f"cpu:{self.__cpu} Memory: {self.__memory}"

    def __gt__(self, other):
        return self.__memory < other.__memory

    def __lt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - Beeline")

    def __str__(self):
        return f"sim card:{self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"до {location} маршрут проложен")

    def __str__(self):
        return super(SmartPhone, self).__str__() + f"sim card:{self.sim_cards_list}"


comp1 = Computer(12, 252)
phone = Phone([1, 2, 3, 4])
smph1 = SmartPhone(12, 156, [1, 2])
smph2 = SmartPhone(11, 196, [1, 2, 3])
obj = [comp1, phone, smph1, smph2]
for i in obj:
    print(i.__str__())
comp1.make_computations()
phone.call(1, "+996755005957")
smph1.use_gps("bishkek")
