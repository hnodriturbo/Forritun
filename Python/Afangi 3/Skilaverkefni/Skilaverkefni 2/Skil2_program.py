########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
############## Ágúst 2023 ##############
import Skil2_class
import Skil2_functions
import Skil2_minnFlottiKlasi
# Sumum liðum er skipt í þrenna parta.
# 1. Prógram sem keyrir
# 2. Fall sem er keyrt af prógrami (byrjar á byrjun og keyrir ýmsa parta sem eru þættir þess að forritið gangi)
# 3. Fall sem er inn í klasanum mínum og er í raun kjarni liðarins


try:
    while True:
        print("\n0. BÚA TIL SKRÁNNA")
        print("1. Prenta út félagaskrá")
        print("2. Bæta við félaga")
        print("3. Eyða félaga")
        print("4. Breyta félaga")
        print("5. Nafn og laun allra félagsmanna prentuð")
        print("6. Laun allra félagsmanna prentað")
        print("7. Heildarskattar upphæð")
        print("8. Flotta leitarvélin mín")
        print("9. Hætta\n")
        val = input("Veldu hvað þú vilt keyra : ")
        while val not in ["0","1","2","3","4","5","6","7","8","9"]:
            val = input("Verður að velja -- :D -- :S -- :D --")
        
        # 0 - Keyra fallið sem býr til skránna
        if val == "0":
            try:
                # Keyri fallið til að búa til skránna, það skilar true eða false
                success = Skil2_functions.buaTilSkra()
                if success:
                    print(f"Til hamingju !!! Það tókst að búa til skránna og 10 aðilar voru færðir til bókar")
            # Ef buaTilSkra skilar villu þá gríp ég hana hérna        
            except Exception as error:
                print(f"Það kom upp villa við að skrifa skránna. Gripin vill var : \n{error}")

        # 1 - Prenta út félagaskrá
        elif val == "1":
            try:
                success = Skil2_functions.prentaVerkalydsfelag()
                if not success:
                    print("\nPrenta út félagaskrá fallið skilaði sér False. Eitthvað hefur komið uppá")
                else:
                    print("\nTil hamingju! Allt gekk upp við prentun á skránni")
                    
            except Exception as error:
                print(f'\nUpp hefur komið vandamál við keyrslu "Prenta út félagaskrá" :\n{error}')

        # 2 - Bæta við félaga
        elif val == "2":
            try:
                success = Skil2_functions.nyr_medlimur()
                if not success:
                    print(f"Eitthvað kom uppá við keyrslu fallsin því það skilaði sér neikvætt tilbaka.")
                else:
                    print(f"\nTil hamingju! Þú hefur bætt við nýjum félagsmanni.")
            except Exception as error:
                print(f"Villa við keyrslu nyr_medlimur fallsins. Gripin villa:\n{error}")
        
        # 3 - Eyða félaga
        elif val == "3":
            try:
                success = Skil2_functions.eydaMedlim()
                if not success:
                    print(f"\nEkki tókst að eyða viðkomandi úr skránni. Fallið skilaði sér neikvætt tilbaka.")
                else:
                    print(f"\nTil hamingju! Þú hefur eytt viðkomandi úr skránni.")
            except Exception as error:
                print(f"\nVilla við keyrslu eydaMedlim fallsins. Gripin villa:\n{error}")        
                
        # 4 - Breyta félaga
        elif val == "4":
            try:
                for message, success in Skil2_functions.breyta_medlim():
                    print(message)
                    if not success:
                        break
                    else:
                        print(f"\nTil hamingju! Að breyta meðlim gekk allt upp.")
            except Exception as error:
                print(f"\nVilla við keyrslu breyta_medlim fallsins. Gripin villa:\n{error}")
                
        # 5 - Prenta út nafn og laun allra félagsmanna 
        elif val == "5":
            try:
                success = Skil2_functions.nafnLaun()
                if not success:
                    print("\nEinhver villa kom upp við keyrslu fallsins")
                else:
                    print("\nAllt gekk upp. Nú verður þú send/ur aftur í aðalvalmyndina")
            except Exception as error:
                print(f"\nVilla við keyrslu nafnLaun fallsins. Gripin villa :\n{error}")
                
        # 6 - Sýna útborguð laun allra félagsmanna
        elif val == "6":
            try:
                success = Skil2_functions.utborgudLaun()
                if not success:
                    print("\nEinhver villa kom upp við keyrslu fallsins")
                else:
                    print("\nAllt gekk upp. Nú verður þú send/ur aftur í aðalvalmyndina")
            except Exception as error:
                print(f"\nVilla við keyrslu utborgudLaun fallsins. Gripin villa :\n{error}")

        # 7 - Sýna heildartölu skatts og hvað hver og einn borgar í skatt
        elif val == "7":
            try:
                success = Skil2_functions.heildarskattar()
                if not success:
                    print("\nEinhver villa kom upp við keyrslu fallsins")
                else:
                    print("\nAllt gekk upp. Nú verður þú send/ur aftur í aðalvalmyndina")
            except Exception as error:
                print(f"\nVilla við keyrslu heildarskattar fallsins. Gripin villa:\n{error}")
        
        # 8 - Leitarvélin mín
        elif val == "8":
            try:
                Skil2_minnFlottiKlasi.minnKlasi.flotta_leitarvelin_min_program()
            except Exception as error:
                print(f"Það kom upp vill við keyrslu leitarvéla fallsins. Gripin villa :\n{error}")
        
        # 9 - Hætta valmöguleikinn
        elif val == "9":
            break
        
        # Til vara:
        else:
            print("þú hefur ekki valið rétt")
    
    print("Takk fyrir að nota forritið mitt")

# Gríp villu hérna ef hún nær hingað í ysta lag kóðans
except Exception as error:
    print(f"Það hefur komið upp einhver villa. Villan sem var gripin er :\n{error}")
