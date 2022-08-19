import math
import Database


def Input():
    PercentofHP=input("Enter % HP: ")
    Pokemon=input("Pokemon name: ")
    for ix, item in enumerate(Database.search(Pokemon)):CatchRate=item[3]
    for ix, item in enumerate(Database.search(Pokemon)):BaseHP=item[4]
    print(Database.search(Pokemon))
    SelectedLocation=input("Enter selected location: ")
    # for ix, item in enumerate(Database.search(Pokemon)):Location=item[7]
    # odvojeno=Location.splitlines()
    # list=odvojeno for tkinter combobox
    #selected value = string selectedlocation
    start = SelectedLocation.find('Lvl.') + len('Lvl.')
    LevelRange=SelectedLocation[start:]
    print(LevelRange)
    if len(LevelRange)>2:
        levels=LevelRange.split("-")
        level=(int(levels[1])+int(levels[0]))/2
    else:level=LevelRange
    Rarity=(SelectedLocation.split(" | ")[-2])
    Pokeball=input("Enter base Pokeball Rate: ")
    Status=input("Enter status: ")
    one=SelectedLocation.find("|")+1
    two=SelectedLocation.find("|",one)+1
    end=SelectedLocation.find("|",two)-1
    EditedStr=SelectedLocation[:end]

    if EditedStr[-1]==")":
        end=EditedStr.find(" (")
        EditedStr=EditedStr[:end]

    print(EditedStr)
    AllLocations=[]
    for ix, item in enumerate(Database.searchAll(EditedStr,Pokemon)):AllLocations.append(item[7])
    print(AllLocations)
    Uncommon=VCommon=Common=Rare=Vrare=0
    for n in AllLocations:
        if(EditedStr+" | Uncommon" in n):Uncommon+=1
        elif(EditedStr+" | Very Common" in n):VCommon+=1
        elif(EditedStr+" | Common" in n):Common+-1
        elif(EditedStr+" | Very Rare" in n):Vrare+=1
        elif(EditedStr+" | Rare" in n):Rare+=1


    print("Uncommon: "+str(Uncommon)+" Very common: "+str(VCommon)+" Common: "+str(Common)+" Very Rare: "+str(Vrare)+" Rare: "+str(Rare))

    Calculate(BaseHP,level,PercentofHP,CatchRate,Pokeball,Status)


def Calculate(BaseHP,level,PercentofHP,CatchRate,Pokeball,Status):
    CatchPercentage=0
    MaxHp=math.floor(0.01*(2*int(BaseHP)+15)*int(level))+int(level)+10 #15 is avg IV on a wild pkmn
    CurrentHp=round(int(MaxHp)/100*int(PercentofHP))
    print(MaxHp)
    X=int((round(int((round(round(((3*float(MaxHp)-2*float(CurrentHp))*float(CatchRate)*float(Pokeball)) * 4096) / 4096 * 4096) / 4096)/(3*int(MaxHp)) * 4096) / 4096 *float(Status) * 4096) / 4096 )* 4096) / 4096
    if(X>=255):CatchPercentage=100
    else:CatchPercentage=(X/255)**0.75  #maybe add rounding to floor x and add the y formula for extra extra precision
    if(CatchPercentage*100>=100):print("100%")
    else:print(str(round(CatchPercentage*100,3))+"%")

Input()
