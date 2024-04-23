import pandas as pd
import numpy as np

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

# Создаем словарь для сопоставления категорий и индексов
categories = list(set(lst))
category_index = {category: i for i, category in enumerate(categories)}

# Преобразуем данные в one-hot представление
one_hot = np.eye(len(categories))[np.array([category_index[category] for category in lst])]

# Создаем DataFrame с one-hot представлением
columns = [f'{category}_one_hot' for category in categories]
data = pd.DataFrame(one_hot, columns=columns)

# Выводим первые несколько строк
data.head()
