#Hreiðar Pétursson
#1.2.2023
#Lista dæmi

import random


#Listar geta teki inn mismunandi gögn
change = [1,"pennies",2,"dimes",3,"quarters"]
for i in change:
    print("i got",i)
print(change)

listi2 = ['gulur',"rauður","grænn","blár","svartur"]
print(listi2)
print(listi2[:2])
print(listi2[-1])

#listi með 5 random tölum á bilinu 20-29
listi = []

#listi.append() bætir við listann
for i in range(5):
    listi.append(random.randint(20, 30))
print(listi)


#Raða listanum (eftir töluröð og/eða stafrófsröð
listi.sort()
print(listi)
#fá lista afturábak
listi.reverse()
print(listi)
#að telja hversu oft kom fyrir í listanum
listi.count(25)
print(listi)

#bæta við lista á ákveðinn stað
listi2.insert(2,"pappír")
print(listi2)

#eyða úr lista
listi2.remove("pappír")
print(listi2)
#Líka eyða úr lista
del(listi2[1])


"""
#Að setja inn í lista með inputi frá notanda
nafnalisti = []
for i in range(1):
    nafn = input("Sláðu inn nafn")
    nafnalisti.append(nafn)
print(nafnalisti)

"""
#Önnur gagnleg föll með list
#Velur random úr listanum
print(random.choice(listi2))
#Stokka listann upp og breyta röðun hans
random.shuffle(listi2)
print(listi2)
#Fara handahófskennt í gegnum listann (byrjun, endir, hækkun)
print(random.randrange(0,5,1))

#Lengd lista
print(len(listi2))

#hæðsta gildi og minnsta
print(max(listi))
print(min(listi))


#Sigríður Sturlaugsdóttir

import random
#~~~~~~~ að finna stök eftir indexi/staðsetningu ~~~~~~~~~~~~~~~~~~~~~
listi = ["gulur", "rauður", "grænn", "blár", "svartur"]

#prentar upp að staki nr 2
print(listi[2])
#prentar frá staki 2 og út að enda listans
print(listi[2:])
#prentar frá upphafi listans upp að staki 4
print(listi[:4])
#prentar stak 2 og 3
print(listi[2:4])

# ~~~~~~~~~~ Að setja randomtölur í lista ~~~~~~~~~~~~~~~~~~~~~
#muna að importa random efst í skjalinu
talnalisti =[]
#listi með 10 random tölum á bilinu 20-40
for x in range(10):
    tala = random.randint(2,41)
    talnalisti.append(tala)
print(listi)

# ~~~~~~~~~~ Að setja input frá notanda í lista ~~~~~~~~~~~~~~~~~~~~~
nafnalisti =[]
#listi með 5 nöfnum frá notanda
for x in range(5):
    nafn = input("Sláðu inn nafn")
    nafnalisti.append(nafn)
#prenta listann út óbreyttan
print(nafnalisti)

# ~~~~~~~~~~ Að raða lista ~~~~~~~~~~~~~~~~~~~~~
#notum sort() til að raða listanum og prentum svo út
nafnalisti.sort()
print(nafnalisti)
#S Snúum listanum við og prentum hann út öfugan
nafnalisti.reverse()
print(nafnalisti)

# ~~~~~~~~ Að finna stak í lista ~~~~~~~~~~~~~~~~~~~~~
vinalisti = ["Karl","Ingimar", "Eva", "Már", "Dís", "Karl", "Anna"]
nafn = "Karl"
#Hér finnum við hvort nafnið er í listanum, en vitum ekki hvar né hvort það séu fleiri en einn
if nafn in vinalisti:
    print("Vinalistinn inniheldur nafnið:", nafn)
else:
    print("Vinalistinn inniheldur ekki nafnið:", nafn)

#Hér finnum við staðsetningu nafnsins
for x in range(len(vinalisti)):
    if vinalisti[x]== nafn:
        print("Nafnið", nafn, "er í staki nr",x)
#Önnur leið til að finna staðsetningu staks í listalista - gefur bara fyrsta index af þessu gildi
stadur = vinalisti.index(nafn)
print("Nafnið", nafn, "er í staki nr",stadur)

#Til að finna hve oft eitthvað nafn kemur fyrir notum við count()
fjNafn= nafnalisti.count(nafn)
print("Nafnið",nafn,"kom fyrir ",fjNafn, "sinnum")

# ~~~~~~~~~~~~~~ Gagnleg föll ~~~~~~~~~~~~~~~~~~~~~
listinn = []
for x in range(200):
    listinn.append(random.randint(70,131))
#Að finna lengd listans - fjölda staka
lengd = len(listinn)
print("Lengd listans er;",lengd)
#Að finna hæsta gildi listans
haesta = max(listinn)
print("Hæsta gildið er:", haesta)
#Að finna lægsta gildið
laegsta = min(listinn)
print("Lægsta gildið er:", laegsta)
#að eyða staki
#pop() tekur eina færibreytu - staðsetningu/index staksins sem á að eyða
#sjálfgefið gildi er -1 - þannig eyðist aftasta stakið ef ekki er sett inn færibreyta
#pop() skilar gildi þess staks sem eytt er
listinn.pop()  # eyðir aftasta stakinu
listinn.pop(7) #Eyðir staki nr. 7

#að finna staðsetningu staks eftir gildi-
# ef stökin eru fleiri en eitt, skilar það lægsta indexnum
nrStak = listi.index(70)
print("Talan 70 er í staki nr:",nrStak)

#að eyða öllum stökum úr lista
listinn.clear()

#að summa upp listann
summa = sum(listi)

#