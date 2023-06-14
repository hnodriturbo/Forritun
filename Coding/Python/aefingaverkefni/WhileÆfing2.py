#Hreiðar Pétursson
#25 janúar 2023
#While æfing fatamarkaður

fjherraskyrtur = 0
verdherraskyrta = 1500
fjdomuskyrtur = 0
verddomuskyrtur = 1500
fjherrabuxur = 0
verdherrabuxur = 2000
fjdomubuxur = 0
verddomubuxur = 2000
fjherrasokkar = 0
verdherrasokkar = 500
fjdomusokkar = 0
verddomusokkar = 500
fjherraskor = 0
verdherraskor = 5000
fjdomuskor = 0
verddomuskor = 5000

samtalsherraskyrtur = 0
samtalsdomuskyrtur = 0
samtalsherrabuxur = 0
samtalsdomubuxur = 0
samtalsherrasokkar = 0
samtalsdomusokkar = 0
samtalsherraskor = 0
samtalsdomuskor = 0


reikningur = 0


on = True


while on == True:




      print("Eftir farandi vörur eru til sölu\n"
            "1. Herra skyrtur 1500kr\n"
            "2. Dömuskyrtur 1500kr\n"
            "3. Herrabuxur 2000kr\n"
            "4. Dömubuxur 2000kr\n"
            "5. Herra sokkur 500kr\n"
            "6. Dömu sokkar 500kr\n"
            "7. Herra skór 5000kr\n"
            "8. Dömu skór 5000kr\n"
            "9. hætta og borga")

      val = int(input("Hvað viltu kaupa"))


      if val == 1:
            fjoldi = int(input("hvað viltu margar herra skyrtur"))
            fjherraskyrtur = fjherraskyrtur + fjoldi

      elif val == 2:
            fjoldi = int(input("Hvað viltu margar dömuskyrtur"))
            fjdomuskyrtur = fjdomuskyrtur + fjoldi

      elif val == 3:
            fjoldi = int(input("hvað viltu margar herrabuxur"))
            fjherrabuxur = fjherrabuxur + fjoldi

      elif val == 4:
            fjoldi = int(input("hvað viltu margar dömubuxur"))
            fjdomubuxur = fjdomubuxur + fjoldi
      elif val == 5:
            fjoldi = int(input("hvað viltu margar herrasokkar"))
            fjherrasokkar = fjherrasokkar + fjoldi

      elif val == 6:
            fjoldi = int(input("hvað viltu margar dömusokka"))
            fjdomusokkar = fjdomusokkar + fjoldi

      elif val == 7:
            fjoldi = int(input("hvað viltu margar herraskó"))
            fjherraskor = fjherraskor + fjoldi


      elif val == 8:
            fjoldi = int(input("hvað viltu margar dömuskó"))
            fjdomuskor = fjdomuskor + fjoldi

      elif val == 9:
            print("Þú hefur valið að hætta.")
            nafn = input("Sláðu inn nafnið þitt:")
            kennitala = int(input("Sláðu inn kennitölu"))
            break






print(nafn)
print("kt:",kennitala)

if fjherraskyrtur > 0:
      samtalsherraskyrtur = fjherraskyrtur * verdherraskyrta
      print("Þú keyptir", fjherraskyrtur,"herraskyrtur á kr", verdherraskyrta, "per stk og það er samtals",samtalsherraskyrtur )

if fjdomuskyrtur > 0:
      samtalsdomuskyrtur = fjdomuskyrtur * verddomuskyrtur
      print("þú keyptir", fjdomuskyrtur,"dömuskyrtur á kr", verddomuskyrtur,"per stk og það er samtals",samtalsdomuskyrtur)

if fjherrabuxur > 0:
      samtalsherrabuxur = fjherrabuxur * verdherrabuxur
      print("Þú keyptir",fjherrabuxur,"herrabuxur á kr",verdherrabuxur,"per stk og það er samtals",samtalsherrabuxur)

if fjdomubuxur > 0:
      samtalsdomubuxur = fjdomubuxur * verddomubuxur
      print("þú keyptir",fjdomubuxur,"dömubuxur á kr",verddomubuxur,"per stk og það er samtals",samtalsdomubuxur)

if fjherrasokkar > 0:
      samtalsherrasokkar = fjherrasokkar * verdherrasokkar
      print("Þú keyptir",fjherrasokkar,"herrasokka á kr",verdherrasokkar,"per stk og það er samtals",samtalsherrasokkar)
if fjdomusokkar > 0:
      samtalsdomusokkar = fjdomusokkar * verddomusokkar
      print("Þú keyptir",fjdomusokkar,"dömusokka á kr",verddomusokkar,"per stk og það er samtals",samtalsdomusokkar)
if fjherraskor > 0:
      samtalsherraskor = fjherraskor * verdherraskor
      print("þú keyptir",fjherraskor,"herraskó á kr",verdherraskor,"per stk og það er samtals",samtalsherraskor)
if fjdomuskor > 0:
      samtalsdomuskor = fjdomuskor * verddomuskor
      print("Þú keyptir",fjdomuskor,"dömuskó á kr",verddomuskor,"per stk og það er samtals",samtalsdomuskor)

heildarverd = samtalsherrabuxur + samtalsdomubuxur + samtalsherrasokkar + samtalsdomusokkar + samtalsherraskor + samtalsdomuskor + samtalsdomuskyrtur + samtalsherraskyrtur

print("Samtals er þetta",samtalsdomuskor)