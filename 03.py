#3.alkalom
#if 50>20 or 20<10:
    #print("igaz")
#else
   # print("nem igaz")
   # print("Ez is hamis ág")

#print("Vége")
#uzenet = "Hello!" if 10>1 else "bye"
#print(uzenet)

def szam_bekerese():
    egyik_szam = input("kérek egy számot:")
    if egyik_szam.isdigit():
        egyik_szam = int(egyik_szam)

        if egyik_szam == 0:
            print("nem ismerem a 0 számot")
        elif egyik_szam < 0:
            print("Nem ismerem a negatív számokat")
        else:
            print("Most már tudok a számmal dolgozni")
    else:
        print("nem számot adtál meg")
    return szam

szam_bekerese = szam_bekerese()
print(egyik_szam)
szam_bekerese()
#masik_szam = input("Kérek még egy számot:")

