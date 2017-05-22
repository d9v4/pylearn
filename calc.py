act = input("add(\'сложение\')\nsubtract(\'вычетание\')\nmultiply(\'умножение\')\ndivide(\'деление\')\n")

if act == "add":
	num1 = input("Первое слагаемое: ")
	num2 = input("Второе слагаемое: ")
	print("Сумма: " + str(float(num1) + float(num2)))

elif act == "subtract":
	num1 = input("Уменьшаемое: ")
	num2 = input("Вычитаемое: ")
	print("Разность: " + str(float(num1) - float(num2)))

elif act == "multiply":
	num1 = input("Уменьшаемое: ")
	num2 = input("Вычитаемое: ")
	print("Разность: " + str(float(num1) * float(num2)))
else:
	print("ERROR")
input()