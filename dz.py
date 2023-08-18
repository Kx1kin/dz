stroka = input('Введите слово: ').lower()


def check(stroka):
	if stroka == stroka[len(stroka)::-1]:
		print('True')
	else:
		print("False")

check(stroka)