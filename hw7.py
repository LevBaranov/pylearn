from pprint import pprint
import difflib # для нечёткого сравнения
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
#Добавим словарь с возможными ключами поиска
dict_keys = {
    'name': ['name', 'fname', 'nme', 'moniker'],
    'role': ['role', 'character', 'function', 'roe'],
    'power':['power', 'pwer', 'force', 'might']
}
#Добавим словарь с операторами сравнения
dict_operators = {
    'more': ['more', 'mo', 'mre', 'up', 'over'],
    'less': ['less', 'ls', 'les', 'under', 'down']
}
def search_prop(s, d):
    #Пробегаем по словарю с ключами и находим свойство по которому будет поиск. Находим только первое вхождение
    list_search_string = s.lower().split();
    for word in list_search_string:
        for item in d:
            if word in d[item]:
                return item
def similarity(s1, s2):
    #С помощью библиотеки difflib будем искать неточные совпдания слов
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    if matcher.ratio() > 0.67: # параметр сходства слов
        return True
    else:
        return False
def search_key_dict(s, prop):
    #Не много улучшил функцию. Уменьшил кол-во циклов.
    list_search_string = s.lower().split();
    result = ''
    for item in persons:
        for word in list_search_string:
            if prop == 'name' and similarity(word, persons[item].name):
                result += str(item)
            elif prop == 'role' and similarity(word, persons[item].role):
                result += str(item)
            elif prop =='power' and word.isdigit():
                powernum = int(word)
                operator = search_prop(s, dict_operators)
                #Предоставим право на ошибку на пару пунктов силы
                if operator == 'more' and powernum < persons[item].power + 2:
                    result += str(item)
                elif operator == 'less' and powernum > persons[item].power - 2:
                    result += str(item)
                elif powernum in range(persons[item].power - 2, persons[item].power + 2):
                    result += str(item)
    return result

#Три запроса на проверку
qu1 = 'nme Arhur mrlin'
qu2 = 'function kng'
qu3 = 'power les 81'

pprint(search_key_dict(qu1, search_prop(qu1, dict_keys)))
pprint(search_key_dict(qu2, search_prop(qu2, dict_keys)))
pprint(search_key_dict(qu3, search_prop(qu3, dict_keys)))