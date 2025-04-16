import random
import time
import csv

tempo = 0
movimentacoes = 0

def generate_random_array(n, seed):
    random.seed(seed)
    random_array = [random.randint(0, 10000) for _ in range(n)]  # Gera números entre 0 e 10000
    return random_array

# Parâmetros para gerar os vetores aleatórios
seed = 587540
array100 = generate_random_array(100, seed)
array100000 = generate_random_array(100000, seed)

# Salva no formato CSV
with open('random_array.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(array100)
    writer.writerow(array100000)

# Implementação do Radix Sort LSD
def radix_sort_lsd(arr):
    global movimentacoes, tempo
    movimentacoes = 0  # Zera contador antes de cada execução
    start_time = time.time()

    # Cria uma cópia para não modificar o array original
    arr = arr[:]
    
    if len(arr) == 0:
        tempo = time.time() - start_time
        return arr

    max_num = max(arr)
    exp = 1  # Começa pelas unidades

    while max_num // exp > 0:
        # 10 buckets para base decimal (0 a 9)
        buckets = [[] for _ in range(10)]

        for number in arr:
            index = (number // exp) % 10
            buckets[index].append(number)
            movimentacoes += 1

        # Junta os buckets em um único array
        arr = [num for bucket in buckets for num in bucket]
        movimentacoes += len(arr)

        exp *= 10

    tempo = (time.time() - start_time) * 1000  # Tempo em milissegundos
    return arr

# Radix Sort MSD (chamada principal)
def radix_sort_msd(arr):
    global tempo, movimentacoes
    movimentacoes = 0
    start_time = time.time()

    arr_copy = arr[:]
    max_num = max(arr_copy) if arr_copy else 0
    max_digits = len(str(max_num))

    arr_sorted = _radix_sort_msd_recursive(arr_copy, max_digits - 1)

    tempo = (time.time() - start_time) * 1000  # Tempo em milissegundos
    return arr_sorted

# Função recursiva do MSD
def _radix_sort_msd_recursive(arr, digit):
    global movimentacoes
    if digit < 0 or len(arr) <= 1:
        return arr

    buckets = [[] for _ in range(10)]

    for number in arr:
        num_str = str(number).zfill(digit + 1)
        index = int(num_str[-(digit + 1)])
        buckets[index].append(number)
        movimentacoes += 1

    result = []
    for bucket in buckets:
        result.extend(_radix_sort_msd_recursive(bucket, digit - 1))
        movimentacoes += len(bucket)

    return result

# Saída dos resultados
output = []
output.append("algoritmo,tamanho,movimentacoes,tempo")

# LSD com 100
sorted_100_lsd = radix_sort_lsd(array100)
output.append(f"Radix LSD,100,{movimentacoes},{tempo:.6f}")

# LSD com 100000
sorted_100000_lsd = radix_sort_lsd(array100000)
output.append(f"Radix LSD,100000,{movimentacoes},{tempo:.6f}")

# MSD com 100
sorted_100_msd = radix_sort_msd(array100)
output.append(f"Radix MSD,100,{movimentacoes},{tempo:.6f}")

# MSD com 100000
sorted_100000_msd = radix_sort_msd(array100000)
output.append(f"Radix MSD,100000,{movimentacoes},{tempo:.6f}")

# Salva no arquivo
with open('resultados.txt', 'w') as file:
    for line in output:
        print(line)
        file.write(line + '\n')