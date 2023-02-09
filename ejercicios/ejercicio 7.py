lista =[2,45,6,3,6,23,76,98,34,9,32,76,12,34,78,11,22,67,102]
menor = 0
mayor = 0
for numbers in lista:
    if menor==0 and mayor==0:
        menor=numbers
        mayor=numbers
    else:
        if numbers<menor:
            menor=numbers
        if numbers>mayor:
            mayor=numbers
print(f"el numero mayor es {mayor}")
print(f"el numero menor es {menor}")


