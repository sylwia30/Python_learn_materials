# Python Tutorial: File Objects - Reading and Writing to Files
# https://www.youtube.com/watch?v=Uh2ebFW8OYM

# f = open('tekst.txt', 'r')
# print(f.name)   # pokaż nazwę pliku
# print(f.mode)   # pokaż jaki sposób otwierania jest pliku read/write/edit...
# f.close()   # zawsze zamykamy plik kóry otwieramy

#-----------------------------------------------------------------------------------------------------------------------
# Moduł 'r' - tylko odczytywanie plików (bez edycji)
#-----------------------------------------------------------------------------------------------------------------------
# read()  - odczytywanie danych z pliku

# with open('tekst.txt', 'r') as f:
    # file_content = f.readline()     # wyświetl pierwszą linię z pliku
    # print(file_content, end='')     # end='' usuń puste linie pomiędzy wierszami
    #
    # file_content = f.readline()     # wyświetl drugą linię z pliku
    # print(file_content, end='')     # end='' usuń puste linie pomiędzy wierszami
    #
    # file_content = f.read()         # wyświetl wszystkie linie z pliku
    # print(file_content, end='')

    # file_content = f.read(10)         # wyświetl 10 pierwszych znaków z pliku (spacje tez liczy)
    # print(file_content, end='*')
    #
    # file_content = f.read(10)         # wyświetl 10 pierwszych znaków z pliku + 10 znaków z poprzedniego kodu (spacje tez liczy)
    # print(file_content, end='*')

    # chyba, że... chcemy aby program zaczął czytać treść plik od początku, to...
    # f.seek(0)
    # file_content = f.read(5)
    # print(file_content, end='')

    # for line in f:                    # wyświetl wszystkie linie z pliku poprzez iterację
    #     print(line, end='')

    # sign_to_read = 10
    # file_content = f.read(sign_to_read)
    # print(f.tell())                     # mówi o ilości znaków w tekście ale tylko wtedy gdy ograniczamy ilość znaków
    #
    # while len(file_content) > 0:        # pokarz pierwsze 10 znaków, potem pokarz kolejne 10 aż będzie koniec tekstu
    #     print(file_content, end='*')    # co 10 znaków pokazuje *
    #     file_content = f.read(sign_to_read)

#-----------------------------------------------------------------------------------------------------------------------
# Moduł 'r','r+','w','w+', 'a', 'a+' - odczytywanie plików oraz edycja (wprowadzanie nowych danych) + tworzenie nowego pliku
#-----------------------------------------------------------------------------------------------------------------------
# write()  - wprowadzanie danych do pliku

# nie ma możliwości wprowadzania danych
# with open('tekstt.txt', 'r') as f:
#     f.write('ggg')

# nadpisuje treść w pliku, zaczynając od początku treści pliku
# with open('tekstt.txt', 'r+') as f:
#     f.write('gggttt')

# kasuje wszystko co jest w pliku i wprowadza nową daną 'ppppp'
# with open('tekstt.txt',  'w') as f:
#     f.write('ppppp')

# kasuje wszystko co jest w pliku i wprowadza nową daną 'dddd'
# with open('tekstt.txt', 'w+') as f:
#     f.write('dddd')

# dopisuje na końcu pliku nową danę 'yyy' nie kasująć reszty treści
# with open('tekstt.txt', 'a') as f:
#     f.write('yyy')

# dopisuje na końcu pliku nową danę 'kkk' nie kasująć reszty treści
# with open('tekstt.txt', 'a+') as f:
#     f.write('kkk')

#-----------------------------------------------------------------------------------------------------------------------
# Moduł 'r' i 'w'- kopiowanie jednego pliku do drugiego
#-----------------------------------------------------------------------------------------------------------------------

# kopiowanie  pliku txt r do pliku w
# with open('tekst.txt', 'r') as r:
#     with open('copy_tekst.txt', 'w') as w:
#         for line in r:
#             w.write(line)

# kopiowanie  pliku jpg r do pliku w - za pomocą iterowania linia po linji
# with open('frogg.jpg', 'rb') as rb:
#     with open('copy_frogg.jpg', 'wb') as wb:
#         for photo in rb:
#             wb.write(photo)

# kopiowanie  pliku jpg r do pliku w - za pomocą iterowania linia po linji
# with open('frogg.jpg', 'rb') as rb:
#     with open('copy_frogg.jpg', 'wb') as wb:
#         size_photo = 4096
#         photo = rb.read(size_photo)
#         while len(photo) > 0:
#             wb.write(photo)
#             photo = rb.read(size_photo)