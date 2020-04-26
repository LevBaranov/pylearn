class Person():
    #Все персонажи имеют стандарнтые свойства имя, возраст, сила
    def __init__(self, name, age, power):
        self.name, self.age, self.power = name, age, power
        self.key = (name, age, power)

    def __repr__(self):
        return "Person('%s',%s,%s)" % (self.name, self.age, self.power)


class Magican(Person):
    'Набор методов характерных только для мага'
    def useMagic(self):
        #Другим персонажам магия не доступна
        pass
    def usePotion(self):
        #Другим персонажам зелье не доступна
        pass
    def summonDragon(self):
        #Другие не могут призвать дракона
        pass


class King(Person):
    'Набор методов характерных только для короля'
    def giveOrder():
        #Только король может отдавать приказы
        pass
    def callVassal(self):
        #Другие персонажи не имеют слуг
        pass
    def makeFeast(self):
        #Устроить пир Остальные не могут
        pass

class Khight(Person):
    'Набор методов характерных только для рыцаря'
    def useSword():
        #Только рыцарь использует мечь
        pass
    def rideHorse(self):
        #Остальные пешеходы
        pass
    def putArmor(self):
        #Броня другим не доступна
        pass