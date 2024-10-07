import random

# Начальное число и список для хранения результата
n = random.randint(3, 20)
result = []

for i in range(1, 21):
    i_pairs = []

    for j in range(1, 21):
        if j != i and n % (i + j) == 0:
            i_pairs.append(j)

    for pair in i_pairs:
        if pair not in result:
            result.append(i)
            result.append(pair)

print( n, ":", * result)
