"""
for i in range (10):
    if i == 4:
        continue
    print(i)    


"""
n = int(input("ingrese un número entero: "))

for numero in range(2,n+1):    
    primo = True
    for i in range (2, numero):
        if numero % i == 0:
             primo = False
             break
             
    if primo:
         print("El número ", numero, " es primo")
    else:
         print("El número ", numero, " NO es primo")

