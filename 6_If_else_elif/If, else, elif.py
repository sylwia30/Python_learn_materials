# Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements
# https://www.youtube.com/watch?v=DZwmZ8Usvnk

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# Operations:
# and
# or
# not

# warunek if
if True:
    print('Conditional is True')

#-----------------------------------
language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Languane is Java')
elif language == 'JavaScript':
    print('Languane is JavaScript')
else:
    print('No match')

#-----------------------------------
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#-----------------------------------
user = 'Admin'
logged_in = False
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

#-----------------------------------
a = [1,2,3]
b = [1,2,3]

print(a == b)   # wynik: True
print(a is b)   # wynik: False

# wynika to z tego, że obiekt a i b mają różne numery ID

print(id(a)) # wynik: 7190856
print(id(b)) # wynik: 7190920

# ale jeśli zapiszemy:
a = [1,2,3]
b = a
# to zmienna a i b mają już taki sam numer ID

print(id(a)) # wynik: 36813320
print(id(b)) # wynik: 36813320

print(a is b)   # wynik: True
print(a == b)   # wynik: True

print(id(a) == id(b))   # wynik: True

#-----------------------------------
# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False     # wynik: False
# condition = None      # wynik: False
# condition = 0         # wynik: False
# condition = 5         # wynik: True !!!!
# condition = ''        # wynik: False
# condition = 'Sylwia'  # wynik: True !!!!
# condition = ()        # wynik: False
# condition = []        # wynik: False
# condition = {}        # wynik: False


if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')















# Wrócić do tego:
# https://www.youtube.com/watch?v=ajrtAuDg3yw

