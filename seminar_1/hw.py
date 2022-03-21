from multiprocessing import Process, Pool
import os
import pandas as pd
from razdel import tokenize
from pymorphy2 import MorphAnalyzer

# В данном задании необходимо будет реализовать параллельную обработку и сохранение текстов в вашу файловую систему.

# Подготовка:
# Загрузите корпус ria.csv с помощью команды: wget https://github.com/ods-ai-ml4sg/proj_news_viz/releases/download/data/ria.csv.gz
# Разахривируйте корпус (или считывайте сразу с декомпрессором в pandas)
# Установите библиотеки pandas, pymorphy2 и razdel

# Логика программы: функция main() -- точка входа данного скрипта.
# В ней вы считываете корпус в виде csv таблицы,выделяете темы и стартуете процессы.
# Нас интересуют только новости из следующих категорий:'В мире', 'Происшествия', 'Общество', 'Экономика', 'РИА Наука', 'Политика', 'Россия', 'Безопасность'
# После выделения тем необходимо заранее создать 8 директорий (по одной на тему), в которые вы будете складывать соответствующие новости. За это будет отвечать функция make_dirs,которая с помощью библиотеки os проверяет наличие переданных в нее директорий, и, если их нет, создаёт их.
#Затем создаётся pool процессов, который применяет функцию process к каждой строчке датасета (в map() можно передать, например, df.iterrows() для этого).
# Функция process(row) вызывает функцию preprocess(text), а затем сохраняет полученный результат с помощью функции save().
# Конечный вид output должен выглядеть как-то так:
# |- Безопасность
#   |- 1543457829.txt
#   |- 1547480072.txt
#   |- .
#   |- .
# |- В мире
#   |- 1543....txt
#   |- 1543....txt
#   |- .
#   |- .
# Имя файлов берём из url

m = MorphAnalyzer()


def make_dirs(names):
    pass


def preprocess(text):
    pass


def save(text, topic, url):
    pass


def process(row):
    # Это функция, которая параллельно будет выполняться в pool.map().
    # Она вызывает все остальные функции (preprocess и save)
    pass


def main():
    # df = ...
    with Pool(4) as pool:
        pass


if __name__ == '__main__':
    main()
