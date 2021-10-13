lorem_ipsum = """"
Czym jest Lorem Ipsum?
Lorem Ipsum jest tekstem stosowanym jako przykładowy 
wypełniacz w przemyśle poligraficznym. Został po raz pierwszy 
użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem 
próbnej książki. Pięć wieków później zaczął być używany przemyśle 
elektronicznym, pozostając praktycznie niezmienionym. 
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy 
Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z 
zawierającym różne wersje Lorem Ipsum oprogramowaniem 
przeznaczonym do realizacji druków na komputerach osobistych, 
jak Aldus PageMaker
"""

print(lorem_ipsum)

imie = "Michał"
nazwisko = "Ruść"

litera1 = nazwisko[2]
liczba_liter1 = lorem_ipsum.count(litera1)

litera2 = imie[1]
liczba_liter2 = lorem_ipsum.count(litera2)

print("W tekście jest {} liter {} oraz {} liter {}"
      .format(liczba_liter1,litera1,liczba_liter2,litera2)
      )

print(dir(lorem_ipsum))
help(lorem_ipsum.format_map)

print("{} {}".format(imie[::-1].lower().capitalize()
                     ,nazwisko[::-1].lower().capitalize()))
lista = [i for i in range(1,11)]
print(lista)
lista2 = lista[5:10]
lista = lista[0:5]
print(lista)
print(lista2)

lista.extend(lista2)
lista.insert(0,0)
print(lista)
lista2 = lista.copy()
lista2.sort(reverse=True)
print(lista2)

studenci = [("Michał Ruść",151160) , ("Adfas Fsafas",1324141)]
print(studenci)
slownik = dict(studenci)
print(slownik)
slownik["24.06.1999"] = 151160
slownik["michal.rusc1234@gmail.com"] = 151160
slownik["22"] = 151160
slownik["Olsztyn"] = 151160
print(slownik)

telefony = ["514 412 412","514 412 412","514 412 412","514 412 413",
            "514 412 414"]
telefony_set = set(telefony)
print(telefony_set)
for i in range(1,11):
      print(i)
for i in range(100, 19, -5):
      print(i)

