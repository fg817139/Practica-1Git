print("ingrese un numero")
numero= int(input())
factorial=1
for i in range(1,numero+1):
    factorial*=i
print(f"el factorial del {numero} es:{factorial}")
