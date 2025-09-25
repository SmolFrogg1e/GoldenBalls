# 4. alkalom

def negyszog(a, b):
    ker = 2 * a + 2 * b
    ter = a * b
    alakzat = "téglalap"
    if a == b:
        alakzat = "négyzet"
    return ker, ter, alakzat

def szamolas(*args):
    osszeg = sum(args)
    legnagyobb = max(args)
    return osszeg, legnagyobb

if __name__ =="__main__":

    sorozat = [1,2,"három",4,5]
for elem in sorozat:
    print(elem)

for i in range(1, 11, 3):
    print(i)

for _ in range(10):
    print("nem leszek rossz!")



print("Összeg:", szamolas(1,2,3,4,5)[0])
print("legnagyobb szám", szamolas(1,2,3,4)[1])



eredmeny = negyszog(a=4,b=4)
print("kerület:", eredmeny[0])
print("terület:", eredmeny[1])
print("alakzat:", eredmeny[2])
