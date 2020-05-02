class Person():
    #Все персонажи имеют стандарнтые свойства имя, возраст, сила
    
    def __init__(self, name, age, power):
        self.name, self.age, self.power = name, age, power
        self.key = (name, age, power)

    def __repr__(self):
        return "Person('%s',%s,%s)" % (self.name, self.age, self.power)


class Magican(Person):
    'Набор методов характерных только для мага'
    
    def use_magic(self, person):
        #Другим персонажам магия не доступна
        pass
    
    def use_potion(self, person):
        #Другим персонажам зелье не доступна
        pass
    
    def summon_dragon():
        #Другие не могут призвать дракона
        pass


class King(Person):
    'Набор методов характерных только для короля'
    def give_order(order, person):
        #Только король может отдавать приказы
        pass

    def call_vassal(vassal):
        #Другие персонажи не имеют слуг
        pass

    def make_feast(self):
        #Устроить пир Остальные не могут
        pass


class Khight(Person):
    'Набор методов характерных только для рыцаря'
    def use_sword(self, person):
        #Только рыцарь использует мечь
        pass

    def ride_horse(self, horse):
        #Остальные пешеходы
        pass

    def put_armor(self):
        #Броня другим не доступна
        pass