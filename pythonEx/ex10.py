a = int(input("Digite a quantidade de dias: "))
b = int(input("Digite a quantidade de horas: "))
c = int(input("Digite a quantidade de minutos: "))
d = int(input("Digite a quantidade de segundos: "))


segundos = (a*86400)
horas = (b*3600)
minutos = (c*60)

soma = (segundos+horas+minutos)

print (f"O total de tudo isso é: {soma}")
