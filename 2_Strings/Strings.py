# Python Tutorial for Beginners 2: Strings - Working with Textual Data
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2


# sposoby wyświetlania print():
greeting = 'Hello'
name = 'Lukas'

print(greeting + ', ' + name)

    # format

greeting = 'Hello'
name = 'Sylwia'

message = '{}, {}, Welcome!'.format(greeting, name)

print(message)

    # f-string

greeting = 'Hello'
name = 'Marta'

message = f'{greeting}, {name.upper()}, Welcome!'

print(message)


# wyświetlanie stringa z apostrofem

    # 1 sposób
message = 'Boby\'s World'
print(message)

    # 2 sposób
message = "Boby's World"
print(message)

    # 3 sposób
message = """Boby's World"""
print(message)

# długość stringa
message = "Boby's World"
print(len(message))

# pierwszy znak stringa
message = "Boby's World"
print(message[0])

# ostatni znak stringa
message = "Boby's World"
print(message[-1])

print('kkkk')
# ostatni znak stringa - alternatywa (-1 bo liczymy od zera)
message = "Boby's World"
print(message[len(message)-1])

# od 2 do 3 znaku stringa
message = "Boby's World"
print(message[1:3])

# od 4 do końca stringa
message = "Boby's World"
print(message[3:])


# od początku do 6 znaku stringa, wyświetl co drugi znak
message = "Boby's World"
print(message[:6:2])

# zmień string na małe litery
message = "Boby's World"
print(message.lower())

# zmień string na duże litery
message = "Boby's World"
print(message.upper())

# ile razy występuje w stringu litera 'o'
message = "Boby's World"
print(message.count('o'))

# pod jakim indeksem jest litera 'y'
message = "Boby's World"
print(message.find('y'))

# pod jakim indeksem jest słowo 'World'
message = "Boby's World"
print(message.find('World'))    # Wynikiem jest 7 ponieważ słowo zaczyna się na 7 indeksie

# pod jakim indeksem jest nieistniejące słowo 'Sylwia'
message = "Boby's World"
print(message.find('Sylwia'))   # Wynikiem jest -1

# zamiana części stringa na inną treść
message = "Boby's World"
print(message.replace('Boby\'s', 'Sylwia\'s'))
print(message)  #Uwaga!!! replace nie zmienia trwale stringa, trzeba nadać nową zmienną
# Wyniki:
# Sylwia's World
# Boby's World
