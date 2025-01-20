import random
digit = '1234567890'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lower = 'qwertyuiopasdfghjklzxcvbnm'
symbol = "'[]/:;№.,>?&^%$#@!*()_-+=<`~"
char = []
digquestion = input('Включить цифры? [Да/Нет] ').lower()
if digquestion == 'да':
	digquestion1 = int(input('Сколько?: '))
	for _ in range(1, digquestion1 + 1):
		char.append(random.choice(digit))
upquestion = input('Включить заглавные буквы? [Да/Нет] ').lower()
if upquestion == 'да':
	upquestion1 = int(input('Сколько?: '))
	for _ in range(1, upquestion1 + 1):
		char.append(random.choice(upper))
lowquestion = input('Включить строчные буквы? [Да/Нет] ').lower()
if lowquestion == 'да':
	lowquestion1 = int(input('Сколько?: '))
	for _ in range(1, lowquestion1 + 1):
		char.append(random.choice(lower))
symquestion = input('Включить символы? [Да/Нет] ').lower()
if symquestion == 'да':
	symquestion1 = int(input('Сколько?: '))
	for _ in range(1, symquestion1 + 1):
		char.append(random.choice(symbol))
question = int(input('Сколько паролей сгенерировать? \n'))
print('Ваши сгенерированные пароли: ')
for _ in range(1, question + 1):
	random.shuffle(char)
	password = ''.join(char)
	print()
	print(password)
