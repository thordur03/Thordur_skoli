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
        listi = []
        while len(listi) != 10:
            try:
                listi.append(int(input("sláðu inn heiltölu")))
            except:
                print("þetta er ekki heiltala")
    elif val==2:
        try:
            #x = 0
            #x = "Q"
            #x = float("konni")
            print(10/x)
        except ZeroDivisionError as e:
            print("Ekki hægt að deila með 0",e)
        except ValueError as e:
            print("ops vitlaust gagnatak",e)
        except NameError as e:
            print("óskilgreind breyta")
        except TypeError as e:
            print("Get ekki lagt saman streng og heiltölu",e)

    elif val==3:
        try:
            tala = int(input("sláðu inn tölu: "))
            if tala < -10:
                raise ValueError("Talan má ekki vera minni en -10")   
            elif tala > 200:
                raise ValueError("Talan má ekki vera stærri en 200")
            elif tala == 27:
                raise ValueError("Talan má ekki vera 27") 
        except ValueError as x:
            print(x)
    elif val==4:
        try:
            f = open("test.txt","r")
            summa = 0
            for x in f.readlines():
                summa = summa + int(x)
            print(summa)
        except:
            print("einhvað fór úrskeyðis",sys.exc_info())
        finally:
            f.close()

    elif val==0:
        on=False