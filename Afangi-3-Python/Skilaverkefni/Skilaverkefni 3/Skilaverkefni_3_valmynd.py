########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########
 

from Skilaverkefni_3_make_files import *
from Skilaverkefni_3_foll import *



try:
    
    while True:
        print("\nVelkominn í Erfða Skilaverkefni 3")
        print("0. Búa til skrárnar")
        print("1. Hermannanema Valmynd")
        print("2. Flokkstjóranema Valmynd")
        print("3. Foringjanema Valmynd")
        print("9. Hætta")
        
        val = input("\nVeldu hvað þú vilt gera : ")
        while val not in ["0","1","2","3","9"]:
            val = input("\nVerður að velja eitthvað")
        
        
        if val == "0":
            try:
                success = buaTilSkrarnar(hermannanemi_instances, flokkstjoranemi_instances, foringjanemi_instances)
                if not success:
                    print("Eitthvað kom uppá við að búa til skrárnar")
                else:
                    print("Það tókst að búa til skrárnar")
            except Exception as error:
                print(f"\nÞað kom upp villa við að búa til skrárnar. Gripin villa : \n{error}")


        elif val == "1":
            # Byrja valmyndina
            while True:
                print("\nVelkominn í Hermannanema Valmyndina")
                print("1. Prenta út alla nemendur")
                print("2. KK, KVK, Hvorugt")
                print("3. Finna nemendur sem byrja á ákveðnum staf")
                print("9. Hætta")
                val = input("\nVeldu hvað þú vilt gera : ")
                while val not in ["1","2","3","9"]:
                    val = input("\nVerður að velja eitthvað af þessu")
                if val == "1":
                    try:
                        success = prenta("hermannanemi.csv", "hermannanemi")
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við að prenta út nemendur. Gripin villa : \n{error}")
                elif val == "2":
                    try:
                        success = eftirKynjum()
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við keyrslu eftirKynjum fallsins. Gripin villa : \n{error}")
                elif val == "3":
                    try:
                        success = eftirStafProgram()
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við keyrslu eftirStafProgram fallsins. Gripin villa : \n{error}")
                elif val == "9":
                    break
        elif val == "2":
            # Byrja valmyndina
            while True:
                print("\nVelkominn í Flokkstjóranema Valmyndina")
                print("1. Prenta út alla nemendur")
                print("2. Finna þá nemendur sem eru í landhernum")
                print("3. Finna alla sem eru eldri en 20 ára")
                print("9. Hætta")
                val = input("\nVeldu hvað þú vilt gera : ")
                while val not in ["1","2","3","9"]:
                    val = input("\nVerður að velja eitthvað af þessu")
                if val == "1":
                    try:
                        success = prenta("flokkstjoranemi.csv", "flokkstjoranemi")
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við að prenta út nemendur. Gripin villa : \n{error}")
                elif val == "2":
                    try:
                        success = finnaLandher()
                        if not success:
                            print("\nÞað fundust engar niðurstöður")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við keyrslu finnaLandher fallsins. Gripin villa : \n{error}")
                elif val == "3":
                    try:
                        success = eldri_20_program()
                        if not success:
                            print("\nÞað kom eitthvað uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við keyrslu finnaLandher fallsins. Gripin villa : \n{error}")
                elif val == "9":
                    break
        elif val == "3":
            # Byrja valmyndina
            while True:
                print("\nVelkominn í Foringjanema Valmyndina")
                print("1. Prenta út alla nemendur")
                print("2. Nafn og upphæð hjá þeim sem skulda herlán")
                print("3. Heildarupphæð herlánsskulda allra nemanda")
                print("9. Hætta")
                val = input("\nVeldu hvað þú vilt gera : ")
                while val not in ["1","2","3","9"]:
                    val = input("\nVerður að velja eitthvað af þessu")
                if val == "1":
                    try:
                        success = prenta("foringjanemi.csv", "foringjanemi")
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við að prenta út nemendur. Gripin villa : \n{error}")
                        
                elif val == "2":
                    try:
                        success = skuldaHerlanProgram()
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við keyrslu skuldaHerlanProgram fallsins Gripin villa : \n{error}")
                elif val == "3":
                    try:
                        success = heildarupphaedHerlansskuldaProgram()
                        if not success:
                            print("\nEitthvað kom uppá við keyrslu fallsins")
                        else:
                            print("\nAllt gekk upp. Nú verðuru sendur aftur í aðalvalmyndina")
                    except Exception as error:
                        print(f"\nÞað kom upp einhver villa við keyrslu heildarupphaedHerlansskuldaProgram fallsins Gripin villa : \n{error}")
                elif val == "9":
                    break
        
        elif val == "9":
            break
        
    print("Takk fyrir að nota forritið mitt")

except Exception as error:
    print(f"Það hefur komið upp einhver villa. Gripin villa: \n{error}")