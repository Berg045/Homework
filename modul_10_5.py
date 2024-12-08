from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

# Список названий файлов
filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов
if __name__ == '__main__':
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    print(f"Линейный вызов: {end_time - start_time}")

# Многопроцессорный вызов
if __name__ == '__main__':
    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(f"Многопроцессный вызов: {end_time - start_time}")