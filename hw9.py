from random import choice, randint

def give_answer():
	return choice(['Да', 'Нет'])

questions = dict()
print("Я отвечу только 'Да' или 'Нет'!")
i = randint(2, 10)
while (i > 0):
	i -= 1
	question = input("Задай свой вопрос: ")
	if question in questions.keys():
		answer = questions[question]
	else:
		answer = give_answer()
		questions[question] = answer
	print(answer)

print("Я устал отвечать на глупые вопросы! Уходи!")