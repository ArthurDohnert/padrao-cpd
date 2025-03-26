import random
import time

potencias_de_dois = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
tres_n_mais_um = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]

tempo = [0,0,0,0,0,0]
movimentacoes = [0,0,0,0,0,0]

def generate_random_array(n, seed):
  random_array = [random.randint(0, 10000) for _ in range(n)]  # Generates numbers between 0 and 10000
  return random_array

# passe os parâmetros para gerar o vetor aleatório
seed = 587540 # id do portal do aluno
array100 = generate_random_array(100, seed)
array1000000 = generate_random_array(100000, seed)

# salve no formato CSV
import csv
with open('random_array.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(array100)
    writer.writerow(array1000000)


# Implementação da função de ordenação

def shell_sort(arr, intervalo, sequencia_para_array):
    start_time = time.time()
    tamanho_array = len(arr)
    intervalo.reverse()
    valor_no_intervalo = 0
    mov = 0

    while (valor_no_intervalo < len(intervalo)):
        h = intervalo[valor_no_intervalo]
        for i in range(h, tamanho_array):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
                mov += 1
            arr[j] = temp
            mov += 1
        
        valor_no_intervalo += 1

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 # multiplicar por 1000 gera o tempo em ms

    movimentacoes[sequencia_para_array] = mov
    tempo[sequencia_para_array] = execution_time

    return arr



array100000_1 = array1000000
array100000_2 = array1000000
array100000_3 = array1000000

array100_1 = array100
array100_2 = array100
array100_3 = array100

## Aqui ordenamos, com os três diferentes métodos, os arrays de 100000 e 100 elementos

sorted100000_1 = shell_sort(array100000_1, potencias_de_dois, 0)
sorted100000_2 = shell_sort(array100000_2, tres_n_mais_um, 1)
sorted100000_3 = shell_sort(array100000_3, ciura, 2)

sorted100_1 = shell_sort(array100_1, potencias_de_dois, 3)
sorted100_2 = shell_sort(array100_2, tres_n_mais_um, 4)
sorted100_3 = shell_sort(array100_3, ciura, 5)

## Saída

output = []
output.append(f"100000 sorted com shellsort. movimentacoes: {movimentacoes[0]}, tempo: {tempo[0]} ms")
output.append(f"100000 sorted com 3n+1. movimentacoes: {movimentacoes[1]}, tempo: {tempo[1]} ms")
output.append(f"100000 sorted com ciura. movimentacoes: {movimentacoes[2]}, tempo: {tempo[2]} ms")
output.append(f"100 sorted com shellsort. movimentacoes: {movimentacoes[3]}, tempo: {tempo[3]} ms")
output.append(f"100 sorted com 3n+1. movimentacoes: {movimentacoes[4]}, tempo: {tempo[4]} ms")
output.append(f"100 sorted com ciura. movimentacoes: {movimentacoes[5]}, tempo: {tempo[5]} ms")

with open('resultados.txt', 'w') as file:
    for line in output:
        print(line)
        file.write(line + '\n')