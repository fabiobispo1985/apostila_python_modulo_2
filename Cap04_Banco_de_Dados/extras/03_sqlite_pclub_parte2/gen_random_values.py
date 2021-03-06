#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""Criando valores randômicos
Antes de mexer no banco de fato vamos criar uns valores
randômicos para popular o banco futuramente.

O arquivo gen_random_values.py gera idade, cpf, telefone, data e
cidade aleatoriamente. Para isso vamos importar algumas bibliotecas."""

import random
#import rstr
import datetime


def gen_age():
    """gera um número inteiro entre 15 e 99"""
    return random.randint(15,99)


def gen_cpf():
    """"gera uma string com 11 caracteres numéricos. No caso, o primeiro parâmetro
    são os caracteres que serão sorteados e o segundo é o tamanho da string"""
    return rstr.rstr('1234567890', 11)


def gen_phone():
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4)
    )


def gen_timestamp():
    year = random.randint(1980, 2015)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date


def gen_city():
    list_city = [
        [u'Sao Paulo', 'SP'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return random.choice(list_city)

