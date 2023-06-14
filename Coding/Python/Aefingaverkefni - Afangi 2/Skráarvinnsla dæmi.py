"""
Skoðum dæmi þar sem við lesum skrá sem nefnist lykilord.txt og lítur svona út:\



"""
notendur=[]# skilgreini listann
with open("lykilord.txt","w",encoding="utf-8") as f:
    f.write("Jonas;Jarðaber\n")
    f.write("Haraldur;Hvannarotarsafi\n")
    f.write("Kamila;KokKonni\n")

with open("lykilord.txt", "r", encoding="utf-8") as file:
    skra = file.read()#les innihald textaskráinnar    #
    print(skra)#gott að skoða þetta
    notendur = skra.split("\n")# býr til lista. Hér nafn og lykilorð
    print(notendur)# gott að skoða þetta
    listi=[]#listi af listum
    for lina in notendur:
        listi.append(lina.split(";"))#splitum listann notndur á ";" og búum til lista af listum
print(listi)#gott að skoða þetta

#Setja í texta skrá:
for lina in notendur:
    lina.strip()
    listi.append(lina.split(";"))#splitum listann notndur á ";" og búum til lista af listum
listi.pop()
print(listi)#gott að skoða þetta#

#setja í skránna
a = ["Sponni","bestur"]
listi.append(a)
print(listi)

with open("lykilord.txt","w",encoding="utf-8")as f:
    for x in listi:
        f.write(x[0]+";"+x[1]+"\n")

#Bæta við skrá:
with open("lykilord.txt","a",encoding="utf-8")as f:
    f.write(x[0]+";"+x[1]+"\n")

"""
CSV skrár
CSV(comma-separated values) skrár eru texta skrár sem hafa það fram yfir venjulegar textaskrár
að hægt er að geyma upplýsingar frá þeim á töfluformi(“rows”). Þessar skrá eru alltaf með  svo
kallaðan “delimeter” sem er tákn sem afmarkar upplýsingar í skránni. Þessar skrá hafa endinguna csv.
Skoðum dæmi
Þetta er skráin
skra.csv:
Jonas Jonasson;23
borkur barkarson;19
andres arason;24
Skráin innheldur nafn og aldur
Svona lesum við út úr CSV skrám
import csv
listiA=[]# opnum csv skrá og notum with open og setjum "r" til að lesa skrá
with open("skra.csv","r",encoding="utf-8",newline="") as file:
    reader = csv.reader(file, delimiter=";") # breyta sem inniheldur csv.reader sem les skrá
    print(reader)
    for row in reader: # for lykkja sem keyrir fyrir hverja röð/row í listaA
        listiA.append(row) #listiA er listi af listum
    print(listiA)
"""
"""
    
Json skrár
https://www.geeksforgeeks.org/read-json-file-using-python/
Json skrá getur litið svona út(data1.json):
{
    "skra":[
        {
        "fornafn": "Konrad",
        "eftirnafn": "Gudmundsson",
    "kyn": "kk",
    "aldur": 63,
    "heimili": {
        "heimilisfang": "Hraunbraut 27",
        "bær": "Kópavogur",
        "póstfang": "200",
        "símanúmer": "8990567"
    }
    }
    ]
}

"""

"""
#Það sést að þetta er einhvers konar dictionary. Til að lesa jason
#skrá er notað fallið load(). Fallið  breytir json objecti í python
#dictionary. Skoðum eftirfarandi kóða:
import json
#opnar json skránna
f=open("data1.json")
#breytir json hlut(object) í python dictionary
data = json.load(f)
for i in data["skra"]:
    print(i)
for k,v in data.items():
    print(k)
    print(v)
    for d in v:
        for k,v in d.items():
            print(k,v)
"""
