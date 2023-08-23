num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese otro numero:"))

comun_divisor=1
if num1 > num2:
    num_hasta = num2
else:
    num_hasta = num1
    
i = 1

while i <= num_hasta:
    if (num1 % i == 0) and (num2 % i == 0):
        comun_divisor = i
    
    i+=1

print("El maximo comun divisor es ", comun_divisor) 