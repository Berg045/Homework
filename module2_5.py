def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []

    matrix = []

    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)

        matrix.append(row)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(2, 0, 20)
result5 = get_matrix(0, 2,10)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
