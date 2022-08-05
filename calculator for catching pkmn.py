import random

#add shiny odds

#17.359 %

#put avg time per encounter
#price per pokeball
#catch rate calculator(myb test it)
#prices for 131iv and myb 231v average
#after 4hrs per day for a week for encounters to figure out % for common rare etc

Encounters=input('Please enter your expected encounter amount: ')
while(Encounters.isdigit()==False):
    Encounters=input("Error, enter the number of encounters again (intiger): ")

NumberofSimulations=10

for x in range(NumberofSimulations):
    IVcount=0
    ZeroIV=0
    OneIV=0
    TwoIV=0
    ThreeIV=0
    FourIV=0
    FiveIV=0
    SixIV=0
    NumberOf31=0
    for x in range(int(Encounters)):
        Iv31=False
        NumberOf31=0
        IVs=[random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31)]
        for iv in IVs:
            if iv == (31):
                NumberOf31+=1
                Iv31=True
        if Iv31==True:
            IVcount+=1

        if(NumberOf31==0):ZeroIV+=1
        if(NumberOf31==1):OneIV+=1
        if(NumberOf31==2):TwoIV+=1
        if(NumberOf31==3):ThreeIV+=1
        if(NumberOf31==4):FourIV+=1
        if(NumberOf31==5):FiveIV+=1
        if(NumberOf31==6):SixIV+=1

    print(str(round(IVcount/int(Encounters)*100,2))+" % of 31-Ived mons")
    print("")
    print("Zero 31: "+str(ZeroIV), str(round(ZeroIV/int(Encounters)*100,3))+"%"+" | One 31: "+str(OneIV)+" | Two 31: "+str(TwoIV)+" | Three 31: "+str(ThreeIV)+" | Four 31: "+str(FourIV)+" | Five 31: "+str(FiveIV)+" | Six 31: "+str(SixIV))

