#importando um módulo que não é nativo
import math

#ler as linhas com as coordenadas
linha = input()

#separar linha e guardar em duas variáveis 
x1 , y1 = linha.split()

#transformando em inteiro
x1 = int(x1)
y1 = int(y1)

linha = input()

x2, y2 = linha.split()

x2 = int(x2)
y2 = int(y2)

#usando a função para calcular raiz quadrada
distancia = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
print(distancia)