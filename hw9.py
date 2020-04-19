from random import choice, randint

def give_answer():
	return choice(['Да', 'Нет'])

print("Я отвечу только 'Да' или 'Нет'!")
i = randint(2, 10)
while (i > 0):
	i -= 1
	input("Задай свой вопрос: ")
	print(give_answer())

print("Я устал отвечать на глупые вопросы! Уходи!")