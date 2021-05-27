#!/usr/bin/env python3
# -*- config: utf-8 -*-

import pandas as pd
import numpy as np

# Использовать объект Series, содержащий следующие индексы: фамилия, имя; знак Зодиака;
# дата рождения (отдельный индекс для каждого из трех чисел). Написать программу,
# выполняющую следующие действия:
# 1.ввод с клавиатуры данных в DataFrame, с заданными колонками;
# 2.вывод на экран информации о человеке, чья фамилия введена с клавиатуры;
# если такого нет, выдать на дисплей соответствующее сообщение.

def add(iter_dat):
    temp_1 = input('Введите Фамилию> ')
    temp_2 = input('Введите Имя> ')
    temp_3 = input('Введите Знак Зодиака> ')
    temp_4 = input('Введите День рождения> ')
    temp_5 = input('Введите Месяц рождения> ')
    temp_6 = input('Введите Год рождения> ')
    dat_frame.loc[iter_dat] = [temp_1, temp_2, temp_3, temp_4, temp_5, temp_6]


def find():
    temp_f = input('Какая фамилия> ')
    print(f'\nТакого человечка мы нашли\n{dat_frame[dat_frame["Фамилия"] == temp_f]}')


if __name__ == '__main__':
    first_ser = pd.Series(['Абдуллаев', 'Джамалудин', 'Водолей', '28', '01', '2001'],
                          ['Фамилия', 'Имя', 'Знак Зодиака', 'День рождения', 'Месяц рождения', 'Год рождения'])
    iter_dat = 1
    dat_frame = pd.DataFrame(
        {
            'Фамилия': {iter_dat: first_ser['Фамилия']},
            'Имя': {iter_dat: first_ser['Имя']},
            'Знак Зодиака': {iter_dat: first_ser['Знак Зодиака']},
            'День рождения': {iter_dat: first_ser['День рождения']},
            'Месяц рождения': {iter_dat: first_ser['Месяц рождения']},
            'Год рождения': {iter_dat: first_ser['Год рождения']},
        }
    )
    while True:
        comm = input('Введите команду> ')
        if comm == 'add':
            iter_dat += 1
            add(iter_dat)
        elif comm == 'find':
            find()
        elif comm == 'help':
            print('ХЕЛП\nДобавить человека - add\n'
                  'Найти человека по фамилии - find\n'
                  'Показать всех - show\nХЕЛП - help'
                  'Выход - exit')
        elif comm == 'show':
            print(dat_frame)
        elif comm == 'exit':
            break
        else:
            print('Ошибка')
