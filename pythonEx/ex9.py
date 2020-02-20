salario = float(input("Digite o seu salário: "))
porcentagem = float(input("Porcentagem de aumento: "))

porcentagem = porcentagem/100
aumento = salario * porcentagem
salario = salario + aumento

print(f"O reajuste salarial é de {aumento} reais e o novo salário é: {salario} reais")

