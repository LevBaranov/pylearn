from pprint import pprint
import difflib

SEARCH_WORDS = {
    'name': ['name', 'fname', 'nme', 'moniker'],
    'role': ['role', 'character', 'function', 'roe'],
    'power':['power', 'pwer', 'force', 'might']
}
WORDS_OPERATORS = {
    'more': ['more', 'mo', 'mre', 'up', 'over'],
    'less': ['less', 'ls', 'les', 'under', 'down']
}

class Person:

    def __init__(self, name, year_birth, role, skill, power):
        self.name, self.year_birth, self.role = name, year_birth, role
        self.skill, self.power = skill, power
        self.key = (name, year_birth, role)

    def __repr__(self):
        return "Person('%s',%s,'%s','%s',%s)" % (
            self.name, self.year_birth, self.role, self.skill, self.power
            )


def search_prop(s, d):
    list_words = s.lower().split();
    for word in list_words:
        for item in d:
            if word in d[item]:
                return item

def is_same(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    if matcher.ratio() > 0.67:
        return True
    else:
        return False

def search_key_dict(s, prop):
    list_search_words = s.lower().split();
    result = ''
    for pers_key in persons:
        for word in list_search_words:
            if prop == 'name' and is_same(word, persons[pers_key].name):
                result += str(pers_key)
            elif prop == 'role' and is_same(word, persons[pers_key].role):
                result += str(pers_key)
            elif prop =='power' and word.isdigit():
                power_num = int(word)
                operator = search_prop(s, WORDS_OPERATORS)
                if operator == 'more' and power_num < persons[pers_key].power + 2:
                    result += str(pers_key)
                elif operator == 'less' and power_num > persons[pers_key].power - 2:
                    result += str(pers_key)
                elif power_num in range(persons[pers_key].power - 2, persons[pers_key].power + 2):
                    result += str(pers_key)
    return result

merlin = Person('Merlin', 450, 'wizard', 'wiseacre', 99)
arthur = Person('Arthur', 472, 'king', 'knight', 83)
morgan = Person('Morgan', 465, 'fairy', 'dark magic', 75)

persons = {
    merlin.key: merlin,
    arthur.key: arthur,
    morgan.key: morgan,
}

query1 = 'nme Arhur mrlin'
query2 = 'function kng'
query3 = 'power les 81'

pprint(search_key_dict(query1, search_prop(query1, SEARCH_WORDS)))
pprint(search_key_dict(query2, search_prop(query2, SEARCH_WORDS)))
pprint(search_key_dict(query3, search_prop(query3, SEARCH_WORDS)))