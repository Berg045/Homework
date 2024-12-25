# 1. requests
import requests

# Запрос данных с сайта
url = 'https://api.github.com'
response = requests.get(url)

# Вывод статуса запроса
print(f"Status Code: {response.status_code}")

# Вывод данных в формате JSON
data = response.json()
print(data)



# 2. Pandas

import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')

print(df.head())

# Простой анализ данных: вычисление среднего значения каждого столбца
mean_values = df.mean()
print(mean_values)

# Простой анализ данных: подсчет количества пропущенных значений
missing_values = df.isnull().sum()
print(missing_values)


# 3. NumPy

import numpy as np

# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций с массивом
squared_array = np.square(array)
print(squared_array)

# Вычисление среднего значения массива
mean_value = np.mean(array)
print(mean_value)

# Вычисление суммы элементов массива
sum_value = np.sum(array)
print(sum_value)



