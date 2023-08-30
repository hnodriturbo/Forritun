############### Hreiðar Pétursson ################
  ### Æfingaverkefni Try / Except / Finally ####
################### Ágúst 2023 ###################



try:
    while True:
        print("Velkominn í æfingaverkefni Try - Except - Finally !")
        print("1. 10 heiltölur frá lyklaborði")
        print("2. Sex mismunandi villuboð")
        print("3. Forrit sem biður um heiltölu")
        print("4. Forrit saem vinnur með skrá")
        
        val = input("Veldu nú - veldu 0 til að hætta")
        while val not in ["1","2","3","4","0"]:
            val = input("Verður að velja 1,2,3 eða 4 og getur valið 0 til að hætta")
        if val == "1":
            
            listiheiltolur = []
            while True:
                try:
                    heiltala = int(input("Sláðu inn 10 heiltölur"))
                    listiheiltolur.append(heiltala)
                    if len(listiheiltolur) == 10:
                        print(f"\nÞað eru komnar 10 tölur í listann! Hér er listinn :\n{listiheiltolur}\n")
                        break
                except ValueError:
                    print("Verður að stimpla inn tölu frá lyklaborði")
                    if ValueError:
                        continue
                
        elif val == "2":
            try:
                while True:
                    print("1. Fá villu eitt - ValueError")
                    print("2. Fá villu tvö - ZeroDivisionError")
                    print("3. Fá villu þrjú - TypeError")
                    print("4. Fá villu fjögur - NameError")
                    print("5. Fá villu fimm - SyntaxError")
                    print("6. Fá villu sex - IndexError")
                    valVilla = input("Veldu nú - Veldu 0 til að hætta")
                    if valVilla == "1":
                        try:
                            strengur = "\nÞetta er strengur sem ég ætla reyna breyta í int"
                            print(strengur)
                            strengur = int(strengur)
                        except ValueError as valueError:
                            print(f"Það hefur komið upp ValueError :\nGripin villa : {valueError}\n")
                    elif valVilla == "2":
                        def deilaTolum(a, b):
                            return a / b
                        try:
                            
                            print("\nHérna ætla ég prenta út niðurstöðu 5 deilt með tölunni 0")
                            nidurstada = deilaTolum(5, 0)
                            print(nidurstada)
                            print("Þessi texti keyrist aldrei !")
                        except ZeroDivisionError as zero:
                            print(f"Það hefur komið upp ZeroDivisionError : \nGripin villa : {zero}\n")
                
                    elif valVilla == "3":
                        def plusaSaman(a, b):
                            return a + b
                        try:
                            print("\nHérna ætla ég plúsa saman tölu og streng")
                            nidurstada = plusaSaman(5, "10")
                            print(f"Þessi texti birtist ekki!  {nidurstada}")
                        except TypeError as error:
                            print(f"Það kom upp TypeError :\nGripin villa : {error}\n")
                    elif valVilla == "4":
                        pass
                    elif valVilla == "5":
                        pass
                    elif valVilla == "6":
                        try:
                            listiFyrirIndexError = ["Eitthvað gildi", 12345, "Þetta er index nr 2"]
                            print(f"\nHérna er ég að reyna prenta út stak frá indexi sem er ekki til :")
                            print(f"{listiFyrirIndexError[3]}")
                        except IndexError as indexError:
                            print(f"\nVilla !! Þú reyndir að fletta upp indexi sem var ekki til :\nGripin villa: {indexError}\n")
                    elif valVilla == "0":
                        break
                    else:
                        print("Einhver furðulegur innsláttur á lyklaborðið kannski ?")
                    
            except:
                pass
        
        
        
        
        
        
        
        
        
        elif val == "3":
            try:
                
                heiltala = int(input("\nSláðu inn heiltölu : "))
                if heiltala < -10:
                    raise ValueError("Talan er minni en -10")
                elif heiltala > 200:
                    raise ValueError("Talan er hærri en 200")
                elif heiltala == 12:
                    raise ValueError("Talan má ekki vera af tölunni 12")
                else:
                    print(f"Talan : {heiltala} er gild tala. Til hamingju ! \n")
            except ValueError as error:
                print(f"Upp hefur komið ValueError : \nGripinn villuboð : {error}\n")
        
        
        
        
        
        
        
        
        elif val == "4":
            
            listiMedTolur = [tala**2 for tala in range(40) if tala % 2 == 0]
            
            def buaTilSkraUtfraTolumILista(listiMedTolur):
                with open("tryExceptVilluVerkefni.txt", "w") as file:
                    file.write(" ".join(map(str, listiMedTolur)))
            def lesaTolurUrSkranniOgFinnaSummuÞeirra():
                with open("tryExceptVilluVerkefni.txt", "r") as file:
                    tolurUrSkra = file.read().split(" ")
                    summa = 0
                    for tala in tolurUrSkra:
                        summa += int(tala)
                    return tolurUrSkra, summa
            try:
                
                while True:
                    print("1. Búa til skrá með tölum")
                    print("2. Lesa tölur úr skránni og finna summu talnanna")
                    valFyrirSkra = input("Veldu 9 til að hætta")
                    
                    while valFyrirSkra not in ["1","2","9"]:
                        valFyrirSkra = input("Verður að velja 1 eða 2 eða 9")
                    
                    if valFyrirSkra == "1":
                        try:
                            buaTilSkraUtfraTolumILista(listiMedTolur)
                        except Exception as error:
                            print(f"\nÞað kom upp villa við að búa til skránna með innihaldi listans :\nGripin villa: {error}")

                        
                    elif valFyrirSkra == "2":
                        try:
                            tolurUrSkraListi, summa = lesaTolurUrSkranniOgFinnaSummuÞeirra()
                        except Exception as error:
                            print(f"Villa : {error}")
                        finally:
                            print(f"Listinn með tölurnar : {tolurUrSkraListi}")
                            print(f"Summa talnanna er : {summa}")
                    elif valFyrirSkra == "9":
                        break
                    
            except Exception as error:
                print(f"\nÞað hefur komið upp einhver villa : \nGripin villa : {error}\n")
        elif val == "0":
            break
        else:
            print("Einhver fór úrskeiðis")
            
    print("Takk fyrir að nota forritið mitt!")
    
except Exception as error:
    print(f"Villa kom upp í valmyndar parti kóðans: {error}")