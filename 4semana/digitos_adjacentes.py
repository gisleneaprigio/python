nDigitado = int(input("Digite um número inteiro:"))

anterior = nDigitado % 10
nDigitado = nDigitado // 10;
adj_iguais = False;
pos = 0

while nDigitado > 0 and not adj_iguais:
    atual = nDigitado % 10
    if atual == anterior:
        adj_iguais = True
    else:
        pos += 1
    anterior = atual
    nDigitado = nDigitado // 10

if adj_iguais:
    print("Sim")
else:
    print("Não")    