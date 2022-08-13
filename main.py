import random
import CatchRate

#17.359 %
#male - female
#convert to tkinter
#put avg time per encounter
#price per pokeball
#catch rate calculator (myb test it)
#prices for 1 31iv and myb 2 31v average
#after 4hrs per day for a week for encounters to figure out % for common rare etc


Encounters=input('Please enter your expected encounter amount: ')
while (Encounters.isdigit()==False):
    Encounters=input("Error, enter the number of encounters again (intiger): ")

CatchingEncounters=input('Please enter your expected cathing pokemon encounter amount: ')
while (CatchingEncounters.isdigit()==False or Encounters<=CatchingEncounters):
    CatchingEncounters=input("Error, must be smaller or equal to the total encounters number: ")

DonatorStatus=input('Donator status (Y, N): ')

NumberofSimulations=1
for x in range(NumberofSimulations):
    IVcount=0
    ZeroIV=0
    OneIV=0
    TwoIV=0
    ThreeIV=0
    FourIV=0
    FiveIV=0
    SixIV=0
    HpIvCount=0
    AtkIvCount=0
    DefIvCount=0
    SpAtkIvCount=0
    SpDefIvCount=0
    SpeIvCount=0
    ShinyCount=0
    for x in range(int(CatchingEncounters)):
        Iv31=False
        NumberOf31=0
        IVs=[random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31)]
        for id,iv in enumerate(IVs):
            if iv == (31):
                if(id==0):HpIvCount+=1
                elif(id==1):AtkIvCount+=1
                elif(id==2):DefIvCount+=1
                elif(id==3):SpAtkIvCount+=1
                elif(id==4):SpDefIvCount+=1
                elif(id==5):SpeIvCount+=1
                NumberOf31+=1
                Iv31=True
        if Iv31==True:
            IVcount+=1

        if(NumberOf31==0):ZeroIV+=1
        elif(NumberOf31==1):OneIV+=1
        elif(NumberOf31==2):TwoIV+=1
        elif(NumberOf31==3):ThreeIV+=1
        elif(NumberOf31==4):FourIV+=1
        elif(NumberOf31==5):FiveIV+=1
        elif(NumberOf31==6):SixIV+=1

for x in range(NumberofSimulations):
    for x in range(int(Encounters)):
        if(DonatorStatus=="Y" or DonatorStatus=="y"):
            Shiny=random.randint(1,27000)
            if(Shiny==27000):ShinyCount+=1
        elif(DonatorStatus=="N" or DonatorStatus=="n"):
            Shiny=random.randint(1,30000)
            if(Shiny==30000):ShinyCount+=1

    print("\n"+str(round(IVcount/int(CatchingEncounters)*100,2))+" % of 31-Ived mons."+"\n")
    if(IVcount>0):
        print("Hp IVS: "+str(HpIvCount)+" ("+str(round(HpIvCount/int(IVcount)*100,2))+")"+"%"+" | Atk IVS: "+str(AtkIvCount)+" ("+str(round(AtkIvCount/int(IVcount)*100,2))+"%"+")"
        +" | Def IVS: "+str(DefIvCount)+" ("+str(round(DefIvCount/int(IVcount)*100,2))+"%"+")"
        +" | SpAtk IVS: "+str(SpAtkIvCount)+" ("+str(round(SpAtkIvCount/int(IVcount)*100,2))+"%"+")"+" | SpDef IVS: "+str(SpDefIvCount)+" ("+str(round(SpDefIvCount/int(IVcount)*100,2))+"%"+")"
        +" | Speed IVS: "+str(SpeIvCount)+" ("+str(round(SpeIvCount/int(IVcount)*100,2))+"%"+")"+"\n")

        print("Zero 31: "+str(ZeroIV)+" ("+str(round(ZeroIV/int(CatchingEncounters)*100,3))+"%"+")"+" | One 31: "+str(OneIV)+
          " ("+str(round(OneIV/int(CatchingEncounters)*100,3))+"%"+")"+" | Two 31: "+str(TwoIV)+" ("+str(round(TwoIV/int(CatchingEncounters)*100,3))+"%"+")"+
          " | Three 31: "+str(ThreeIV)+" ("+str(round(ThreeIV/int(CatchingEncounters)*100,3))+"%"+")"+" | Four 31: "+str(FourIV)+" ("+str(round(FourIV/int(CatchingEncounters)*100,3))+"%"+")"+
          " | Five 31: "+str(FiveIV)+" ("+str(round(FiveIV/int(CatchingEncounters)*100,3))+"%"+")"+" | Six 31: "+str(SixIV)+" ("+str(round(SixIV/int(CatchingEncounters)*100,3))+"%"+")"+"\n")

    print("Shinies: " +str(ShinyCount)+"\n")
