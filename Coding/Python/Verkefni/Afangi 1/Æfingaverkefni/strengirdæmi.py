nafn = "Sigga Sturlaugsdóttir"
ordid = "Framhaldsskoli"
kennitala = "2711882929"
leyniord = "K45st5"

# str.count("stafur") - skilar fjölda þess char sem leitað er að
print("Fjöldi g í nafni:",nafn.count("g"))

# hægt að nota margföldunarmerki til að endurtaka streng aftur og aftur
print("~"*7)

#að skipta út staf fyrir annan str.replace(gamli,nýi)
print(nafn.replace("g", "@"))

#str.upper() -> Breyta í hástafi tímabundið
print("Nafn í hástöfum",nafn.upper())

#str.lower() -> breyta í lágstafi tímabundið
print("Nafn í lágstöfum", nafn.lower())

#breytum öllum stöfum í lágstafi
nafn= nafn.lower()
#str.title() -> Breyta fyrsta staf allra orða í streng í hástafi og hinum í lágstafi
print("Nafn í lágstöfum", nafn)
print("Nafn með stóra stafi í upphafi allra orða", nafn.title())


# + tengir saman strengi og setur saman í einn str+str
print("tengja saman tvo strengi",nafn+kennitala)

#str.isalnum() -> athugar hvort allt í strengnum sé stafir/tolur - ekki merki/ tákn  eða annað slíkt og skilar True eða False
if leyniord.isalnum():
    print("Bara stafir og tölustafir í orðinu", leyniord)
else:
    print("Það eru eh tákn í strengnum", leyniord)

#Líka hægt að nota með einum staf í einu
stafur =0
tala=0
temp = "ðjkk77æ654"
for x in temp:
    if x.isalpha():
        print("bókstafur", x)
        stafur= stafur+1
    if x.isdigit():
        tala = tala+1
print("Fjöldi bókstafa í strengnum er:", stafur)
print("Fjöldi tölustafa í strengnum er:", tala)

#str.isalpa() -> athugar hvort það séu bara bókstafir í strengnum (má ekki vera bil) og skilar True/False
if ordid.isalpha():
    print("Bara stafir í ordinu", ordid)
else:
    print("Það eru eh tákn/tölustafir/bil í strengnum", ordid)

#str.isdigit() -> athugar hvort það séu bara tölustafir í strengnum(má ekki vera bil) og skilar True/False
if kennitala.isdigit():
    print("Bara tölustafir í kennitölunni", kennitala)
else:
    print("Það eru eh tákn eða bókstafir í strengnum", kennitala)

#str.isupper() -> athugar hvort allur strengurinn er í hástöfum - skilar True/False
if nafn.isupper():
    print("Bara hástafir")
else:
    print("þetta er ekki allt hástafir")

#str.islower() -> athugar hvort allur strengurinn er í lagstöfum - skilar True/False
if nafn.isupper():
    print("Bara lágstafir")
else:
    print("þetta er ekki allt lágstafir")

#str.isspace() -> athugar hvort það sé bil í strengnum - skilar True/False
if nafn.isspace():
    print("það eru bil í strengnum")
else:
    print("Engin bil í þessum streng")


