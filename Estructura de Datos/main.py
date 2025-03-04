import numpy as np

n_candidatos = 30
n_votos = 5000

#Randomizer con sumatoria de 5000
pvals = [1/30] * 30
votos = np.random.multinomial(n_votos, pvals, size=1)

votos = votos[0]
#print(votos)

votosMatriz = []
for i in range(n_candidatos - 1):
    votosMatriz.append([f"Candidato {i + 1}: ", int(votos[i])])

#Ordena los votos de mayor a menor
votosMatriz.sort(key=lambda x: x[1], reverse=True)

#Imprime resultados
print("----- RESULTADOS -----\n")

for j in range(n_candidatos - 1):
    print(votosMatriz[j][0] + str(votosMatriz[j][1]))

#print(votosMatriz)