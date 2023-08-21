#Hreiðar Pétursson
#Skilaverkefni 1
#11janúar
import math
#liður 1 - skilaverkefni

#Hérna bið ég notanda um nafn
nafnnotanda = input("Vinsamlegast sláðu inn nafn:")

#Hérna bið ég notanda um uppáhaldsfagið sitt
uppahalds = input("Vinsamlegast sláðu inn þitt uppáhaldsfag:")

#Hérna prenta ég í setningu það sem notandinn skrifaði inn
print("Velkominn í",uppahalds,"Þetta verður skemmtileg önn hjá okkur",nafnnotanda)


#Liður 2 - skilaverkefni

#Forrit biður um tvær heilt0lur
tala1 = int(input("Sláðu inn tölu 1"))
tala2 = int(input("Sláðu inn tölu 2"))

#Hérna set ég margfeldi talnanna inn í breytu
margfeldi = tala1 * tala2
#prenta út margfeldi talnanna
print("Margfeldi talnanna er:",margfeldi)

#Hérna set ég frádrátt talnanna inn í breytu
fradrattur = tala1 - tala2

#Prenta úr frádrátt talnanna
print("frádráttur talnanna er:",fradrattur)

#hér legg ég tölurnar saman í breytu
lidurc = tala1 + tala2
#Hér deili ég svo summu talnanna með 1.45
deilinglidurc = lidurc / 1.45
print("summa talnanna deild með 1,45 er:",deilinglidurc)

#Liður 3 - skilaverkefni

#Hérna bið ég notanda um radíus hrings
radiushrings = int(input("Sláðu inn radíus hrings:"))

#hérna reiknga ég ummál hringsins
ummalhrings = 2 * radiushrings * math.pi
#Hérna bið ég forritið að hafa bara einn aukastaf eftir kommuna
ummalhrings2 = round(ummalhrings, 1)
#Hérna prenta ég út ummálið af hringnum
print("ummál hringsins er:",ummalhrings2)

#hérna reikna ég út flatarmál hringsins:
flatarmal = radiushrings * radiushrings * math.pi
#Hérna bið ég forritið að hafa bara einn aukastaf eftir kommuna
flatarmal2 = round(flatarmal, 1)
#Hérna prenta ég flatarmál hringsins
print("flatarmál hringsins er:",flatarmal2)

#liður 4 - skilaverkefni
#Ég bið notanda um aldur
aldurnotanda = int(input("Sláðu inn þinn aldur:"))
#Hérna bið ég notanda um aldur föður síns
aldurfodur = int(input("Sláðu inn aldur pabba þíns"))

#Reikna út hvað pabbinn var gamall þegar hann eignaðist barnið sitt
aldurfodur2 = aldurfodur - aldurnotanda
#Prenta út niðurstöðuna
print("Pabbi þinn var",aldurfodur2,"ára þegar hann eignaðist þig :D")

#liður 5 - skilaverkefni
#Hérna við ég um aldur þriggja einstaklinga
print("Til að fá meðalaldur vinsamlegast sláðu inn aldur ykkar þriggja:")
      
#Hér bið ég um aldur Hreiðars
aldurhreidar = int(input("Hreiðar, sláðu inn aldur þinn:"))
#Hér bið ég um aldur Gunnars
aldurgunnar = int(input("Gunnar, sláðu inn aldur þinn"))
#Hér bið ég um aldur Jónatans
aldurjonatan = int(input("Jónatan, sláðu inn aldur þinn"))

#Hér reikna ég út meðalaldur
#Byrja á að plúsa saman aldur þeirra þriggja
reikningur = aldurhreidar + aldurgunnar + aldurjonatan
#Deili svo útkomunni með 3
medaltal = reikningur / 3
#Hérna bið ég um að fá útkomuna með tveimur kommutölum
medaltal = round(medaltal, 2)
#Hérna prenta ég útkomuna
print("meðalaldur ykkar er:",medaltal)

#liður 6 - skilaverkefni
#Spyr notanda um þrjár heiltölur
print("Vinsamlegast sláðu inn þrjár heiltölur")
#Bið um tölu númer 1
tala1 = int(input("Sláðu inn tölu númer 1"))
#Bið um töllu númer 2
tala2 = int(input("Sláðu inn tölu númer 2"))
#bið um tölu númer 3
tala3 = int(input("Sláðu inn tölu númer 3"))

#Hérna athuga ég hvort einhver af tölunum séu eins
if tala1==tala2 or tala1==tala3 or tala3==tala2:
    print("Ekki má slá inn sömu tölu tvisvar")

#hérna byrja ég að athuga hvaða tala er í miðjunni
else:
    #hérna athuga ég hvort tala 1 er í miðjunni
    if tala1 > tala2 and tala1 < tala3 or tala1 < tala2 and tala1 > tala3:
        print("tala", tala1,"er í miðjunni")
    #hérna athuga ég hvort tala 2 er í miðjunni
    elif tala2 > tala1 and tala2 < tala3 or tala2 < tala1 and tala2 > tala3:
        print("tala",tala2,"er í miðjunni")
    #ef hvorugt tala 1 eða 2 er í miðjunni þá hlýtur tala 3 að vera í miðjunni
    else:
        print("tala", tala3,"er í miðjunni")


#liður 7 - skilaverkefni
#spyr hvort notandinn vilji breyta tommu í sentimetra eða öfugt
spurning = input("hvort viltu breyta tommum í sentimetra eða öfugt? Svar: tommur í cm eða cm í tommur")

#hérna skrifar notandinn svarið tommur í cm
if      spurning == "tommur í cm":
#hérna spyr ég notandann hvað margar tommur
        tommur = int(input("sláðu inn hvað margar tommur"))
#hérna reikna ég tommurnar yfir í centimetra
        sentimetrar = tommur * 2.54
#hérna passa ég uppá að svarið hafi bara 2 stafi eftir kommu
        sentimetrar2 = round(sentimetrar, 2)
#hérna prenta ég svarið
        print("Það eru",sentimetrar2,"cm")

elif    spurning == "cm í tommur":
#Hérna spyr ég notandann hvað marga cm
        sentimetrar = int(input("Sláðu inn hvað margir cm"))
#reikna sentrimetra yfir í tommur með því að deila með 2.54
        tommur = sentimetrar / 2.54
#passa uppá að svarið hafi bara 2 aukastafi eftir kommu
        tommur2 = round(tommur, 2)
#hérna prenta ég svarið
        print("Það eru",tommur2,"tommur")

#Ef notandinn slær inn eitthvað annað en cm í tommur eða tommur í cm kemur rangt svar
else:
        print("rangt svar")





#liður 8 - skilaverkefni

#hérna bið ég notandann um númer mánaðar
numermanadar = int(input("Sláðu inn númer mánaðar"))

#athuga hvort númer mánaðar er á bilinu 1-3
if numermanadar > 0 and numermanadar < 4:
    print("Nú er daginn tekið að lengja")

#athuga hvort númer mánaðar er á bilinu 4-5
elif numermanadar > 3 and numermanadar < 6:
    print("vorið er komið og grundirnar gróa")
    
#Athuga hvort númer mánaðar er á bilinu 6-8
elif numermanadar > 5 and numermanadar < 9:
    print("núna er sumarið komið með blóm í haga")

#Athuga hvort númer mánaðar er á bilinu 9-10
elif numermanadar > 8 and numermanadar < 11:
    print("núna er haustið gengið í garð")

#athuga hvort númer mánaðar er á bilinu 11-12
elif numermanadar > 10 and numermanadar < 13:
    print("Núna styttist í jólin")

#allt annað sem slegir er inn er rangt
else:
    print("Rangur innsláttur")


#liður 9 - skilaverkefni

#bið notanda um tölu sem er lægri en 0 eða hærri en 10

tala = int(input("Sláðu inn tölu sem er lægri en 0 eða hærri en 10"))

if tala >= 0 and tala <= 10:
    print("Þessi tala er ekki lægri en 0 eða hærri en 10")
else:
    print("vel gert")
