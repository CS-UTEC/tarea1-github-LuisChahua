n=int(input())
i=int(n**0.5)
x=0
for j in range (2,i+1):
    if(n%i==0):
        print("No es primo")
        x=1
        break
if(x==0):
    print("Es primo")
