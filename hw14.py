class Integer(int):
    def __add__(self, arg):
        return super().__add__(arg) + 1
        

i = Integer(2)
print(i.__add__(2))