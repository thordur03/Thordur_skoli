import time
import sys

on = True
while on == True:
    print("(1)")
    print("(2)")
    print("(3)")
    print("(4)")
    print("(5)")
    print("(0) Hætta við")
    val=int(input("hvað viltu gera? "))
    if val==1:
        skeidklukka

    elif val==2:
        klukka = True
        timi = time.localtime()
        while klukka:
            timi = time.localtime()
            print(timi[3],":",timi[4],":",timi[5])
            sys.stdout.write("\033[F")
            

    elif val==3:
        a = 1
        b = 2
        c = 3
        a = b = c
        print(a)
    elif val==4:
        pass
    elif val==0:
        lokaval = input("ertu viss um að þú viljir hætta ja eða nei: ")
        lokaval = lokaval.lower()
        if lokaval == "ja":
            on=False
    