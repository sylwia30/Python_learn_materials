# integer - liczba całkowita
num = 3
print(type(num))

# float - liczba zmiennoprzecinkowa
num = 3.14
print(type(num))

# Arithmetic Operators/Operacje arytmetyczne:
# Addition:       3 + 2
print(3 + 2)
# Subtraction:    3 - 2
print(3 - 2)
# Multiplication: 3 * 2
print(3 * 2)
# Division:       3 / 2
print(3 / 2)            # w Pythonie 3 wynikiem dzielenia jest 1,5 w Pythonie 2 liczba cąłkowita 1
# Floor Division: 3 // 2
print(3 // 2)
# Exponent:       3 ** 2
print(3 ** 2)
# Modulus:        3 % 2
print(3 % 2)

# kolejność obliczeń
print(3 * 2 + 1)
print(3 * (2 + 1))

# inkrementacja
num = 1
num += 10
# to to samo co:
num = 1 + 10
print(num)

# wartość bezwzględna
print(abs(-6))

# zaokrąglenia do liczby całkowitej
print(round(3.75))

# zaokrąglenia do 1 miejsca po przecinku
print(round(3.75, 1))

# zaokrąglenia do 2 miejsc po przecinku
print(round(3.756, 2))

# Comparisons/Porównania:
num1 = 3
num2 = 2
# Equal:            3 == 2
print(num1 == num2)
# Not Equal:        3 != 2
print(num1 != num2)
# Greater Than:     3 > 2
print(num1 > num2)
# Less Than:        3 < 2
print(num1 < num2)
# Greater or Equal: 3 >= 2
print(num1 >= num2)
# Less or Equal:    3 <= 2
print(num1 <= num2)

# operacje na stringach
num_1 = '100'
num_2 = '200'

print(num_1 + num_2)    # błędny wynik: 100200

num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)    # poprawny wynik: 300

# mnożenie stringów
multipy = 3
text = 'Python'

print(multipy * text)   # wynik: PythonPythonPython
