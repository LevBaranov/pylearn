from pprint import pprint
from utils import compare, int_val
from itertools import product

ADDRESS_WORDS = {'дом','улица','живет', 'квартира'}
NAME_WORDS    = {'имя','зовут','фамилия', 'отчество'}
AGE_WORDS     = {'возраст', 'старше', 'младше', 'лет'} # лет - для ровного счёта

class Person:
    def __init__(self, first_name, middle_name, last_name, age, street, house, apartment):
        self.first_name, self.middle_name, self.last_name = first_name, middle_name, last_name
        self.street, self.house, self.apartment = street, house, apartment
        self.age = age
        self.key = (self.first_name, self.middle_name, self.last_name, self.street, self.house, self.apartment)
    
    def __repr__(self):
        return "Person('%s','%s','%s',%s,'%s','%s','%s')" % (self.first_name, self.middle_name, self.last_name, self.age, self.street, self.house, self.apartment)
    
    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.first_name, self.middle_name, self.last_name, self.age, self.street, self.house, self.apartment) == (obj.first_name, obj.middle_name, obj.last_name, obj.age, obj.street, obj.house, obj.apartment)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()
        
    def __fuzzy_compare(self, query):
        def by_address(Q):
            if 'улица' in Q or 'живет' in Q:
                W = set(self.street.split())
                rez = []
                Q = Q - ADDRESS_WORDS
                for a, b in product(Q, W):
                    rez += [(compare(a,b),a,b)]
                return max(rez)[0]
            elif 'дом' in Q:
                query_house = max([ int_val(q) for q in Q ])
                return query_house == self.house
            elif 'квартира' in Q:
                query_apartment = max([ int_val(q) for q in Q ])
                return query_apartment == self.apartment
            return 0
        
        def by_name(Q):
            if "имя" in Q:
                W = set(self.first_name.split())
            elif 'отчество' in Q:
                W = set(self.middle_name.split())
            elif 'фамилия' in Q:
                W = set(self.last_name.split())
            else:
                W = set(self.first_name.split()).union(self.middle_name.split(), self.last_name.split())
            rez = []
            Q = Q - NAME_WORDS
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]
        
        def by_age(Q):
            query_age = max([ int_val(q) for q in Q ])
            if 'старше' in Q:
                return query_age < self.age 
            if 'младше' in Q:
                return query_age > self.age 
            return query_age + 5 >= self.age >= query_age - 5
        
        q_words = set(query.split())
        score = 0
        for m_words, method in zip([ADDRESS_WORDS, NAME_WORDS, AGE_WORDS],
                                   [by_address,    by_name,    by_age]):
            if m_words & q_words:
                score += method(q_words)
                
        return score > 0.49

lena = Person("Елена",   "Ивановна",  "Воронова",  19, "Пушкина",  14, 115)
oleg = Person("Олег",    "Петрович",  "Синицын",   34, "Ленскoго", 10, 11)
olga = Person("Ольга",   "Фёдоровна", "Воробей",   28, "Онегина",  11, 12)
nata = Person("Наталья", "Игоревна",  "Кукушкина", 17, "Ростова",  16, 15)

queries = [
    'имя Ольга', 
    'возраст 30', 
    'старше 20', 
    'младше 20', 
    'живет на Пушкина', 
    'дом 10',
    'фамилия ростова',
    'зовут Лена',
]

people = {
    lena.key: lena,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata,
}


good_queries = set()
for query, person in product(queries, people.values()):
    if person == query:
        pprint((query, person))
        good_queries.add(query)
print('Запросы вернувшие пустой результат:')
pprint(set(queries) - good_queries)