valor1 = int(input("Digite a primeiro valor: "))
valor2 = int(input("Digite a segundo valor "))
valor3 = int(input("Digite a terceiro valor "))

if ((valor1 < valor2) and (valor2 < valor3) and (valor3 > valor1)):
    print("Crescente")
else:
    print("Não está em ordem crescente")        
