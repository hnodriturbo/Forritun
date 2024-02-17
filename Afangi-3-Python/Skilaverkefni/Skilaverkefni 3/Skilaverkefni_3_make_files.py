########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########

from Skilaverkefni_3_klasar import *
import csv
# Sample data for hermannanemi instances
hermannanemi_instances = [
    hermannanemi("1404872529", "Hreiðar Pétursson", "kk", "7617603", "Pétur Már Jónsson", "Bekkur 1", "Önn 1"),
    hermannanemi("1206806059", "Anton Gunnarsson", "kk", "8947869", "Stína Gunnarsdóttir", "Bekkur 2", "Önn 2"),
    hermannanemi("1507891269", "Guðný Ósk Hreiðarsdóttir", "kvk", "5897465", "Fríða Jónsdóttir", "Bekkur 1", "Önn 1"),
    hermannanemi("0506844589", "Sunna Jónsdóttir", "kvk", "8963256", "Jónína Friðjónsdóttir", "Bekkur 3", "Önn 3"),
    hermannanemi("0909817899", "Svanhvít Jónsdóttir", "kvk", "4689654", "Anna Gunnarsdóttir", "Bekkur 3", "Önn 3"),
    hermannanemi("0112897419", "Alexander Bjarnason", "kk", "7684598", "Arna Fríðudóttir", "Bekkur 2", "Önn 2")
]

# Sample data for flokkstjoranemi instances
flokkstjoranemi_instances = [
    flokkstjoranemi("1504887529", "Jón Ólafsson", "kk", "8976541", "Landher", "Herdeild 1"),
    flokkstjoranemi("1206806059", "Sara Jónsdóttir", "kvk", "5648965", "Landher", "Herdeild 1"),
    flokkstjoranemi("1407813269", "Björn Björnsson", "kk", "5632456", "Sjóher", "Herdeild 2"),
    flokkstjoranemi("0506844589", "Dís Jónsdóttir", "kvk", "7894561", "Sjóher", "Herdeild 2"),
    flokkstjoranemi("0909817899", "Sigurður Sigurðsson", "kk", "7985645", "Flugher", "Herdeild 3"),
    flokkstjoranemi("0112897419", "Ásta Ástardóttir", "kvk", "8956565", "Flugher", "Herdeild 3")
]

# Sample data for foringjanemi instances
foringjanemi_instances = [
    foringjanemi("1504872529", "Hafdís Ólafsdóttir", "kvk", "8991111", "Stig 1", "89000", "1120000"),
    foringjanemi("1206806059", "Þórður Jónsson", "kk", "8977899", "Stig 3", "0", "0"),
    foringjanemi("1407813269", "Guðmundur Guðmundsson", "kk", "8778888", "Stig 2", "301000", "4568000"),
    foringjanemi("0506844589", "Berglind Ólafsdóttir", "kvk", "7776666", "Stig 1", "99000", "1256000"),
    foringjanemi("0909817899", "Einar Einarsson", "kk", "8693565", "Stig 2", "0", "0"),
    foringjanemi("0112897419", "Sólveig Jónsdóttir", "kvk", "7617676", "Stig 3", "212000", "2890000")
]



def buaTilSkrarnar(hermannanemi_instances, flokkstjoranemi_instances, foringjanemi_instances):
    with open("hermannanemi.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Kennitala', 'Nafn', 'Kyn', 'Símanúmer', 'Aðstandandi', 'Bekkur', 'Önn'])
        for hermannanemi in hermannanemi_instances:
            writer.writerow([hermannanemi.kennitala, hermannanemi.nafn, hermannanemi.kyn, hermannanemi.simanumer, 
                             hermannanemi.adstandandi, hermannanemi.bekkur, hermannanemi.onn])
    
        # Create CSV files for flokkstjoranemi instances
    with open('flokkstjoranemi.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Kennitala', 'Nafn', 'Kyn', 'Símanúmer', 'Herdeild', 'Her'])
        for instance in flokkstjoranemi_instances:
            writer.writerow([instance.kennitala, instance.nafn, instance.kyn, instance.simanumer,
                             instance.herdeild, instance.her])
    
    # Create CSV files for foringjanemi instances
    with open('foringjanemi.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Kennitala', 'Nafn', 'Kyn', 'Símanúmer', 'Stig Náms', 'Námslaun', 'Herlán'])
        for instance in foringjanemi_instances:
            writer.writerow([instance.kennitala, instance.nafn, instance.kyn, instance.simanumer,
                             instance.stigNams, instance.namslaun, instance.herlan])
    return True
