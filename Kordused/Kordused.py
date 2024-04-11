#1


while True:
    try:
        mitu=int(input("Siseta arv 1-9"))
        if 1<=mitu<=9:
            break
    except ValueError:    
        print("Vale tüüp")
        
for i in range(mitu):
    print("(\_/)".center(10," "),end="")
print()
for i in range(mitu):
    print("(o o)".center(10," "),end="")
for i in range(mitu):
    print("/ | \*".center(10," "),end="")


#2
i in range(0,14,1)
a=0
while i<15:
 a=a+i
else:
    print("Nende arvede summa on: ", a)

    
   

#3

import random 
x=random.randint(1,100)
katse=int(0)
print("Proovi ära arvata, sa saad proovida 10 korda!")
while katse<=10:
    katse+=1
    i=int(input("Mis numbri ma välja mõtlesin?"))
    if i==x:
        print("Sina arvasid ära!")
        break
    elif i!=x:
        int(katse+1)
        if i<x:
            print("Liiga väike arv, proovi uuesti.")
        else:
            print("Liiga suur arv, proovi uuesti.")
else:
    print("Sinu katsed on läbi.")



    #4

try:
    arv=int(input("Sisseta täisarv: "))
    ümberpööratud= 0
 
    while arv > 0:
        n=arv%10
        arv=arv//10
 
        ümberpööratud=ümberpööratud*10
        ümberpööratud =ümberpööratud+n
 
 
    print("See sama arv ümberpööratud:", ümberpööratud)
except:
    print("valed andmed")

    

#5
try:
    arv=int(input("sisseta täisarv"))
    summa=0
    korrutis=1
    while arv/10>=1:
        n=arv%10
        summa=summa + n
        korrutis=korrutis * n
        arv=arv//10
    print("Numbrite summa selles arvus on",summa)
    print("Numbrite korrutis selles arvus on",korrutis)
except:
    print("valed andmed")





#4(varian 5)

from random  import *


sum_num=0
sum_km=0
for i in range(12):
    num=randint(1000,10000)
    km=randint(1,1000)
    sum_num+=num
    sum_num+=km
    print(f"{i+1}. maakond. \nElanikud: {num}. Pindala: {km}\n Kokku: /{sum_num},{sum_km}")
vastus=sum_num/sum_km
print(f"Keskmine: {vastus:.3f}")





#5(4v)


from random import *
while True:
    try:
        K=int(input("Mitu kotlet sul on?  "))
        if K>0:
            break
    except ValueError:
        print("Vale tüüp")
while True:
    try:
        P=int(input("Mitu kotleti ühel panil?  "))
        if P>0:
            break
    except ValueError:
        print("Vale tüüp")
while K>P:
    k-=P
    pann+=1
    print
   
print(f"Täispannid: {pann} ja veel on vaja {lisapann}")
print()