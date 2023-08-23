num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingreso otro numero: "))

def maximo_comun_div(num1, num2):
    comun_divisor = 1
    if num1 > num2:
        num_hasta = num2
    else:
        num_hasta = num1
    i = 1
    while i <= num_hasta:
        if (num1 % i == 0) and (num2 % i == 0):
            comun_divisor = i
        
        i+=1
    return comun_divisor
    
minimo_comun_multiplo = num1 * num2 / maximo_comun_div(num1, num2)
   
print("Minimo comun multiplo: ", minimo_comun_multiplo)

        
