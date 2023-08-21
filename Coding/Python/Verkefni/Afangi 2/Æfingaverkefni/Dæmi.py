tala1 = 10
tala2 = 20

def reikna(tala1,tala2):
    utkoma = tala2 + tala1
    return utkoma

print(reikna)

def leggja_sama_2tolur(tala1,tala2):
    summa = 0
    summa = tala1+tala2
    return summa

print(leggja_sama_2tolur(12,23))

def listi(tolur):
    summa = 0
    for tala in tolur:
        summa+=tala
    return summa

talnalisti = [1,2,3,4,5]
print(listi(talnalisti))

def setning(nafn='konni',action='sefur',hlutur='rólega'):
    print(nafn,action,hlutur)
    print(setning())
    print(setning(action="hleypur"))

def leggja_saman_tolur(*tolur):
    summa = 0
    for tala in tolur:
        summa += tala
    return summa
print(leggja_saman_tolur(12,2,3,45))

listi = [1,2,3,4,5]
print(leggja_saman_tolur(*listi))

def heilsu_reiknir(aldur,epli,sigarettur):
    svar = (100-aldur)+(epli*3.5)-(sigarettur*2)
    print(svar)
print(heilsu_reiknir(12,40,5))

listi = [12,34,5]
print(heilsu_reiknir(*listi))
print()
print()
#Dictionary æfingar
my_dict = {} #Tómt dictionary
my_dict = {1:"apple",2:"ball",3:"Hafabolti"} #Með integer lykli
my_dict = {"Nafn":"John",1:[2,4,3]} #mismunandi gagnlykill

#Nálgast gildi(value) í dictionary
print(my_dict["Nafn"])
print(my_dict.get(1)) #Skilar none ef ekkert finnst

#útskrift
my_dict = {1:"Apple",2:"Ball",3:"Epli",4:"Banani"}
for x in my_dict:
    print("númer",x,"er",my_dict[x])

for key, value in my_dict.items():
    print("%s er %s" % (key,value))

for key, value in my_dict.items():
    print("{0} er {1}" .format(key,value))

#Breyta value
my_dict[2] = "Bolti"
print(my_dict)
my_dict[5] = "Grænmeti"
print(my_dict)
#Bæta við key = value
my_dict[6] = "Halló"
print(my_dict)
#Eyða value
print(my_dict.pop(3))
print(my_dict)
del my_dict[5]
print(my_dict)
my_dict.clear()
print(my_dict)
del my_dict
#ýmsar aðferðir tengt dictionary
marks = {}.fromkeys(["math","English","Science"], 0)
print(marks)
for item in marks.items():
    print(item)
print(sorted(marks.keys()))
marks["math"] = 10
print(marks)

squares = {x:x*x for x in range(6)}
print(squares)
squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)

odd_squares = {x:x*x for x in range(11) if x%2 == 1}
print(odd_squares)

print(1 in odd_squares)
print(2 not in odd_squares)
print(49 in odd_squares)
"""
#fleiri innbyggð föll
all() # Return True if all keys of the dictionary are true or dict empty
any() # Return True if any key of the dictionary is true. If dict empty then False
len() # Returns the length
cmp() # Compare two items
sorted() #Returns a sorted list of keys in the dictionary
"""

print(len(squares))
print(sorted(squares))

squares.clear() # Remove all items
squares.copy() # Return a shallow copy
marks = {}.fromkeys(["Math","Copy","Paste"])
print(marks)
print(marks.get("Math"))
print(marks.items())
marks.pop("Math")
marks.popitem()
marks.setdefault("Math")
print(marks)
marks.update(["Math"])
print(marks.values())



