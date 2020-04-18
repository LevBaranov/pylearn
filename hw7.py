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

def search_key_dict(s):
    #Для этого задание будет использован только чёткие и определённые критерии
    list_search_string = s.split();
    result = ''
    for item in persons:
        if 'name' in list_search_string:
            for word in list_search_string:
                if word == persons[item].name:
                        result += str(item)
        elif 'role' in list_search_string:
            for word in list_search_string:
                    if word == persons[item].role:
                        result += str(item)
        elif 'power' in list_search_string:
            for i in list_search_string:
                if i.isdigit():
                    powernum = int(i)
            if 'more' in list_search_string and powernum < persons[item].power:
                result += str(item)
            elif 'less' in list_search_string and powernum > persons[item].power:
                result += str(item)
            elif powernum == persons[item].power:
                result += str(item)
    return result

#Три запроса на проверку
qu1 = 'name Arthur Merlin'
qu2 = 'role king'
qu3 = 'power less 76'

pprint(search_key_dict(qu1))
pprint(search_key_dict(qu2))
pprint(search_key_dict(qu3))