svar = int(input("skriv ett tal"))
antal_gissningar = 1


while svar != 42 and antal_gissningar <3:
    if svar < 42:
        print("för litet")
        svar = int(input("gissa igen:  "))

    if svar > 42:
        print("för stort. ")
        svar = int(input("gissa igen: "))
    antal_gissningar = antal_gissningar + 1
if svar == 42:
    print("du är bäst")
    print(antal_gissningar, "gisningar behövde du")
