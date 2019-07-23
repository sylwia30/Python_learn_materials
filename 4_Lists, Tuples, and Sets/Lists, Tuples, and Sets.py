# Python Tutorial for Beginners 4: Lists, Tuples, and Sets
# https://www.youtube.com/watch?v=W8KRzm-HUcc

# List------------------------------------------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']

# długość listy
print(len(courses))

# indeks elementu - pierwszy element listy
print(courses[0])

# indeks elementu - ostatni element listy
print(courses[-1])
    #lub sprytnie:
print(courses[len(courses)-1])

# indeks elementu - pierwsze 2 elementy listy
print(courses[0:2])
    #lub sprytnie
print(courses[:2])

# dodawanie elementu na koniec listy
courses.append('Art')
print(courses)

# dodawanie elementu w okreslone miejsce do listy
courses.insert(1, 'Biology')
print(courses)

# dodawanie listy do listy w określonym miejscu, indeks 0
courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Education', 'Religion']
courses.insert(0, courses2)
print(courses)

# dodawanie listy na koniec listy
courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Education', 'Religion']
courses.append(courses2)
print(courses)

# dodawanie listy na koniec listy, ale jako elementy a nie lista
courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Education', 'Religion']
courses.extend(courses2)
print(courses)

# usuwanie konkretnego elementu
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('History')
print(courses)

# usuwanie ostatniego elementu
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop()
print(courses)
    # jeślo chcemy sprawdzić co się usuneło za pomoca pop to możemy to sprawdzić za pomocą:

courses = ['History', 'Math', 'Physics', 'CompSci']
pop_check = courses.pop()
print(pop_check)
print(courses)

# wyświetlanie listy od końca
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

# sortowanie listy od A do Z
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [5, 7, 1, 3]

courses.sort()
nums.sort()

print(courses)
print(nums)

# sortowanie listy od Z do A
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [5, 7, 1, 3]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

# sortowanie listy od A do Z za pomocą funkcji sorted
nums = [5, 7, 1, 3]
sorted(nums)
print(nums)  # funcka nie zadziała dopóki nie nadamy zmiennej do funkcji
    # poprawne użycie funckji sorted
nums = [5, 7, 1, 3]
sorted_courses = sorted(nums)
print(sorted_courses)  # funcka nie zadziała do póki nie nada się zmiennej do funkcji

# wartość maximum z listy
nums = [5, 7, 1, 3]
print(max(nums))

# wartość minimum z listy
nums = [5, 7, 1, 3]
print(min(nums))

# suma elementów listy
nums = [5, 7, 1, 3]
print(sum(nums))

# szukanie indeksu danego elementu w liście
courses = ['History', 'Math', 'Physics', 'CompSci']
element_index = courses.index('Physics')
print(element_index)

# sprawdzanie czy elemnt jest w liscie
courses = ['History', 'Math', 'Physics', 'CompSci']
print('Art' in courses) # wynik:False

# iterowanie listy
courses = ['History', 'Math', 'Physics', 'CompSci']
for course in courses:
    print(course)

# iterowanie listy + dodanie numeru pozycji (enumerate + number) + dodanie od jakiej cyfry numeruje (start=1)
courses = ['History', 'Math', 'Physics', 'CompSci']
for number, course in enumerate(courses, start=1):
    print(number, course)

# utworzenie ciągu znaków z elementów listy
courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ', '.join(courses)
print(course_str)

# utworzenie listy z ciągu znaków
new_list =  course_str.split(', ')
print(new_list)

# Mutable objects - BARDZO WAŻNE!!!!
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)
#wyniki:
# ['History', 'Math', 'Physics', 'CompSci']
# ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'

print(list_1)
print(list_2)
#wyniki: ZMIANA ELEMENTU W LIŚCIE 1 SPOWODOWAŁA ZMIANĘ ELEMNTU W LIŚCIE 2!!!!!
# ['Art', 'Math', 'Physics', 'CompSci']
# ['Art', 'Math', 'Physics', 'CompSci']

# Immutable - Tuple-----------------------------------------------------------------------------------------------------
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # nie można zmieniać danych w tupli

print(tuple_1)
print(tuple_2)

# Sets------------------------------------------------------------------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)   # printowanie słownika zawsze jest w różnej kolejności

# wyszukiwanie wspólnych elementów set-a 1, w set-a 2
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

# wyszukiwanie róznych elementów set-a 1, w set-a 2
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.difference(art_courses))

# łączenie dwóch set-ów w jeden
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
# wynik: []
empty_list = list()
# wynik: []

# Empty Tuples
empty_tuple = ()
# wynik: ()
empty_tuple = tuple()
# wynik: ()

# Empty Sets
empty_set = {} # This isn't right, it isn't a set! It's a dict!
# wynik: {}
empty_set = set()
# wynik: set()