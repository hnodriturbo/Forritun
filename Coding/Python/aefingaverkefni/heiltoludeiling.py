#HreiðarPétursson
#Heiltöludeiling
#16janúar2023

#Fáum upphæð frá notanda
peningur = int(input("Sláðu inn upphæð"))

#Notum // til að fá fjölda 5000 kr seðla
fimmthusund = peningur // 5000

#Notum modulus % til að fá hve mikið er eftir
#Þegar búið er að taka 5000 kr seðlana af
afgfimmthusund = peningur % 5000

#Notum // til að fá fjölda þúsund kr seðla
eittthusund = afgfimmthusund // 1000
afgeittthusund = afgfimmthusund % 1000

#Prentum út hver útkoman okkar er
print("Þetta er þá", fimmthusund, "fimm þúsund kr seðlar og", eittthusund, "þúsund króna seðlar")


#liður 1 æfingaverkefni
gradur = int(input("Sláðu inn hvað margar gráður"))

heillhringur = gradur // 360

afgheillhringur = gradur % 360

print("Þetta er",heillhringur,"hringir og",afgheillhringur,"gráður")


#liður 2 - æfingaverkefni heiltöludeiling

hvadmargir = int(input("Hvað eru margir mættir á fótboltaæfinguna?"))
hvamorglid = int(input("hvað eiga að vera mörg lið?"))

lid = hvadmargir // hvamorglid
afglid = hvadmargir % hvamorglid

print("það verða",lid,"lið og það verða",afglid,"margir varamenn")


#Liður 4 - heiltöludeiling
millimetrar = int(input("Sláðu inn fjölda millimetra"))

metrar = millimetrar // 1000
afgmetrar = millimetrar % 1000

sentimetrar = afgmetrar // 10
afgmillimetrar = afgmetrar % 10

print("Þetta gerir",metrar,"metra og",sentimetrar,"sentimetra og",afgmillimetrar,"millimetra")


#liður 5 - heiltöludeiling
kronur = int(input("Sláðu inn hvað margar krónur"))

thusund = kronur // 1000
afgthusund = kronur % 1000

fimmhundrud = afgthusund // 500
afgfimmhundrud = afgthusund % 500

hundrad = afgfimmhundrud // 100
afghundrad = afgfimmhundrud % 100

print("Þetta gerir",thusund,"stk 1000 kr seðla,",fimmhundrud,"500kr seðla,",hundrad,"100kr peninga og",afghundrad,"krónur")


#liður 6 - heiltöludeiling

tala = int(input("Sláðu inn tölu"))
if tala % 2 == 1:
    print("Þetta er oddatala")
else:
    print("Þetta er slétt tala")
