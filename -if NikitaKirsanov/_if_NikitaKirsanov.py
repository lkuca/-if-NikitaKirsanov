from math import *
from random import * 

print("Tere, palun sisestage oma isikukood")
a=float(input("Kirjutage oma isikukood => "))
a=len("text")
if a==11 and text.isdigit():
     print("Teie isikukoodi kinnitatakse.......")
else:
     print("protsessi.....")
     print("Sinu isikukood õige")
     print()
 

print()





from math import *
from random import *



r=randint(-100,100)
a=randint(-100,100)
print(f"r=(r)\na=(a)")
if r>0 and a<0:
   skv=a**2
   skr=pi*r**2
   if skv>skr:
        print(f"Ruusu pindala (skv) on suurem ringi pindala (skr)")
   elif skr>skv:
        print(f"Ruusu pindala (skv) on suurem ringi pindala (skv)")
   else:
        print("Pindalad on võrdseb. (skr) m^2")
else:
     print(f"(a) ja (r) peavad > kui 0 olla")
print()

from math import *
from random import * 
try:
    päev=int(input("Mis päev ja mitu tundi täna on ?"))
    if   päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisipäev"
        n="8 tundi"
    elif päev==3:
        n="Kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="Neljapäev"
        n="5 tundi"
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==7:
        n="Pühapäev"
        n="0 tundi"
    else:
        n="vale nimber"
        print(n)
except:
    print("!!!!!!!")

print("Sisselogimine tahvel")
try:
    vanus=int(input("Kui vana sa oled? ")
    if vanus>=18:
        print("Kas te annate vanematele loa oma Tahvelit vaadata? ")
        o=(input("Jah või ei"))
        if o.lower()=="jah": #upper() будет делать все буквы большими
        print({o})
        print("See on ligipääs teie vanematele.")
        print("Tahvel on kinni.")
    elif o.upper()=="EI":
        print("Sissepääs puudub")
        print("Tahvel on kinni")
if vanus<18
   print("Juurdepääs vsnematele on automaatselt antud.")
