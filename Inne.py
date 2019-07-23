# funkcja dir() - pokazuje metody i atrybuty jakie można zastosować na tej zmiennej

name = 'Sylwia'
print(name)
print(dir(name))

# funkcja help() - pokazuje opis co metody robią i atrybuty jakie można zastosować na tej zmiennej

name = 'Sylwia'
print(name)
# print(help(name)) # na zmiennej name nie zadziała
print(help(str)) # na str zadziała
# przykład:
# | lower(...)
# | S.lower() -> str

print(help(str.lower())) # na str zadziała