class Integer(int):
    'Измененный int, чтобы 2+2 =5'
    def __add__(self, arg):
        return super().__add__(arg) + 1
        
class List(list):
    'Измененный list, что больше 10 элементов нельзя положить'
    def __init__(self, arg):
        if len(arg) <= 10:
            return super().__init__(arg)
    
    def append(self, arg):
        if (self.__len__() + 1) <= 10:
            return super().append(arg)

    def extend(self, arg):
        if (self.__len__() + len(arg)) <= 10:
            return super().extend(arg)
    
    def insert(self, position, arg):
        if (self.__len__() + 1) <= 10:
            return super().insert(position, arg)

if __name__ == '__main__':
    l = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(l)
    l.append(4)
    print(l)
    l.extend([14, 35])
    print(l)
    l.insert(4, 45)
    print(l)
