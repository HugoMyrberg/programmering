svar = int(input("skriv ett tal"))
antal_gissningar = 1

# igen om antal gissningar < 3
# igen om gissat fel o
# sluta om gissar rätt

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
print(antal_gissningar, "är tyvärr det maximala antal gissningar du får på dig. Vill du köra igen så starta om programmet")
