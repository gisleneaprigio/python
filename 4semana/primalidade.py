n = int(input("Digite um número inteiro:  "))


if n == 2 or (n != 1 and n % 2 == 1): 
    é_primo = True
else:
    é_primo = False 

divisor = 3
while divisor < n and é_primo: 
    if n % divisor == 0:
        é_primo = False
    divisor += 2 
   
if é_primo: 
    print("primo")
else:
    print("não primo")