from pprint import pprint
class Person:
    def __init__(self, name, year_birth, role, skill, power):
        self.name, self.year_birth, self.role, self.skill, self.power = name, year_birth, role, skill, power
        self.key = (name, year_birth, role)
    def __repr__(self):
        return "Person('%s',%s,'%s','%s',%s)" % (self.name, self.year_birth, self.role, self.skill, self.power)

merlin = Person('Merlin', 450, 'wizard', 'wiseacre', 99)
arthur = Person('Arthur', 472, 'king', 'knight', 83)
morgan = Person('Morgan', 465, 'fairy', 'dark magic', 75)

persons = {
    merlin.key: merlin,
    arthur.key: arthur,
    morgan.key: morgan,
}

pprint(persons)