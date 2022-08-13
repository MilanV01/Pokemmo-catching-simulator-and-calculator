import math
import Database


def Input():
    PercentofHP=input("Enter % HP: ")
    Pokemon=input("Pokemon name: ")
    
    CatchRate=input("Enter base Catch Rate: ")
    Pokeball=input("Enter base Pokeball Rate: ")
    Status=input("Enter status: ")
    BaseHP=input("BASEHP: ")
    level=input("NIVO: ")
    Calculate(BaseHP,level,PercentofHP,CatchRate,Pokeball,Status)

def Calculate(BaseHP,level,PercentofHP,CatchRate,Pokeball,Status):
    CatchPercentage=0
    MaxHp=math.floor(0.01*(2*int(BaseHP)+15)*int(level))+int(level)+10 #15 is avg IV on a wild pkmn
    CurrentHp=round(int(MaxHp)/100*int(PercentofHP))
    print(MaxHp)
    X=int((round(int((round(round(((3*float(MaxHp)-2*float(CurrentHp))*float(CatchRate)*float(Pokeball)) * 4096) / 4096 * 4096) / 4096)/(3*int(MaxHp)) * 4096) / 4096 *float(Status) * 4096) / 4096 )* 4096) / 4096
    if(X>=255):CatchPercentage=100
    else:CatchPercentage=round((X/255)**0.75,5)  #maybe add rounding to floor x and add the y formula for uber precision
    print(str(CatchPercentage*100)+"%")

Input()