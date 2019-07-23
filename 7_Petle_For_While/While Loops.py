# Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ

print('------------------------------------')
# break w pętli for
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# wynik:
# 1
# 2
# Found!

print('------------------------------------')
# continue w pętli for
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# wynik:
# 1
# 2
# Found!
# 4
# 5

print('------------------------------------')
# bez break i bez continue w pętli for
for num in nums:
    if num == 3:
        print('Found!')
    print(num)

# wynik:
# 1
# 2
# Found!
# 3
# 4
# 5

print('------------------------------------')
# Pętla w pętli

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('------------------------------------')
# Pętla z range()
for i in range(10):
    print(i)

# wynik:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print('------------------------------------')
for i in range(1, 11):
    print(i)
# wynik:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print(' while ------------------------------------')
# Pętla While

x = 0
while x < 10:
    print(x)
    x += 1

# wynik:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print(' while ------------------------------------')
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# wynik:
# 0
# 1
# 2
# 3
# 4