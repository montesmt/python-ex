p_nome = input("Digite o primeiro nome: ")
s_nome = input("Digite o segundo nome: ")

p_idade = int(input("Digite a primeira idade: "))
s_idade = int(input("Digite a segunda idade: "))

if p_idade > s_idade:
    print(f"{p_nome} é mais velho que o {s_nome}")

elif s_idade > p_idade:
    print(f"{s_nome} é mais velho que o {p_nome}")

else: 
    print("Eles tem a mesma idade.")

