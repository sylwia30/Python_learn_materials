# Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs
# https://www.youtube.com/watch?v=daefaLgNkw0

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

# wyświetlanie wartości słowników
print(student.get('age'))
    # inny sposób wyświetlania wartości kluczy, jako indeksu
print(student['name'])
print(student['courses'])

# różnice gdy nie ma podanego klucza w słowniku WAŻNEEEEE!!!!
# print(student['phone'])
    # wynik: KeyError: 'phone'
print(student.get('phone'))
    # wynik: None !!!!!!!
# zamiast wyniku None możemy wyświetlić inną, swoją wartość
print(student.get('phone', 'Not Exist!!!'))

# dodawanie klucza i wartości do słownika
student['phone'] = '888-523-114'
print(student.get('phone'))

# zmiana wartości w słowniku
student.update({'name': 'Mary', 'age': 65, 'courses': ['Math', 'CompSci']})
print(student)
    # lub inny sposób
student['name'] = 'Michael'
print(student)

# usuwanie klucza i wartości ze słownika za pomocą: del
del student['age']
print(student)

# usuwanie klucza i wartości ze słownika za pomocą: pop
courses_pop = student.pop('courses')

print(courses_pop)
print(student)

# ilośc kluczy w słoniwku
print(len(student))

# lista nazw kluczy słownika
print(student.keys())

# lista nazw wartości słownika
print(student.values())

# lista nazw kluczy i wartości słownika
print(student.items())

print('----------------')
# iterowanie kluczy słownika
for key in student:
    print(key)

print('----------------')
# iterowanie wartości słownika
for key in student.values():
    print(key)

print('----------------')
# iterowanie kluczy i wartości słownika
for key, value in student.items():
    print(key, value)