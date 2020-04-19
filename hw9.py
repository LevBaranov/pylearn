from random import choice, randint
import difflib

def give_answer():
	return choice(['Да', 'Нет'])

def is_same(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    if matcher.ratio() > 0.67:
        return True
    else:
        return False      

def get_key_answer(q, list_key):
	for q in list_key:
		if is_same(question, q):
			return questions[q]
	return False

questions = dict()
print("Я отвечу только 'Да' или 'Нет'!")
i = randint(2, 10)
while (i > 0):
	i -= 1
	question = input("Задай свой вопрос: ")
	if get_key_answer(question, questions.keys()):
		answer = get_key_answer(question, questions.keys())
	else:
		answer = give_answer()
		questions[question] = answer
	print(answer)

print("Я устал отвечать на глупые вопросы! Уходи!")