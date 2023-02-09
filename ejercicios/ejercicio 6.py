amount_of_numbers =int(input("ingrese el numero de veces que quiere que se repita la litas"))
numbers = 0
for i in range(0, amount_of_numbers):
    entered_number = float(input("ingrese el numero deseado"))
    numbers += entered_number
print(f"la suma de los numeros de la lista es {numbers}")
