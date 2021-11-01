def Tafel():
    getal = input('Van welk getal wilt u de tafel zien? ')
    
    getal = int(getal)
    for teller in range(1,11):
        print(teller * getal)
    print()
Tafel()