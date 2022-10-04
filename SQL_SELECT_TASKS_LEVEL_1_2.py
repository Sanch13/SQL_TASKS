import string

#  TASKS FROM www.sql-ex.ru

"""Схема БД состоит из четырех таблиц:

Product(maker, model, type)

Таблица Product представляет:
производителя (maker)
номер модели (model)
тип type ('PC' - ПК, 
        'Laptop' - ПК-блокнот
        'Printer' - принтер)
Предполагается, что номера моделей в таблице Product уникальны для всех производителей и типов продуктов.


PC(code, model, speed, ram, hd, cd, price)

В таблице PC для каждого ПК, однозначно определяемого уникальным кодом – code,указаны 
модель – model (внешний ключ к таблице Product), 
скорость - speed (процессора в мегагерцах), 
объем памяти - ram (в мегабайтах), 
размер диска - hd (в гигабайтах), 
скорость считывающего устройства - cd (например, '4x')
цена - price (в долларах). 



Таблица Laptop аналогична таблице РС за исключением того, что вместо скорости CD содержит
размер экрана -screen (в дюймах).


Printer(code, model, color, type, price)


В таблице Printer для каждой модели принтера указывается, является ли он 
цветным - color ('y', если цветной), 
тип принтера - type (лазерный – 'Laser', 
                     струйный – 'Jet'
                     матричный – 'Matrix')
цена - price."""

##################################################################################################
"""Задание: 1 Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол.
Вывести: model, speed и hd"""
# SELECT model, speed, hd
# FROM PC
# WHERE price < 500
##################################################################################################
"""Задание: 2 Найдите производителей принтеров. Вывести: maker"""
# SELECT DISTINCT maker
# FROM PRODUCT
# WHERE type='Printer'
##################################################################################################
"""Задание: 3 Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, 
цена которых превышает 1000 дол."""
# SELECT model, ram, screen
# FROM LAPTOP
# WHERE price > 1000
##################################################################################################
"""Задание: 4 Найдите все записи таблицы Printer для цветных принтеров."""
# SELECT code, model, color, type, price
# FROM PRINTER
# WHERE color='y'
##################################################################################################
"""Задание: 5 Найдите номер модели, скорость и размер жесткого диска ПК, 
имеющих 12x или 24x CD и цену менее 600 дол."""
# SELECT model, speed, hd
# FROM PC
# WHERE price < 600 AND (cd = '12x' OR cd = '24x')
##################################################################################################
"""Задание: 6 Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не
менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость."""
# SELECT DISTINCT Product.maker, speed
# FROM Product, Laptop
# WHERE Product.type = 'Laptop' AND Laptop.hd >= 10 AND Product.model = Laptop.model
#       решение через JOIN
# SELECT DISTINCT Product.maker, Laptop.speed
# FROM Product
# JOIN Laptop ON Product.model = Laptop.model
# WHERE Laptop.hd >= 10
#       без использования AS
# SELECT DISTINCT p.maker, l.speed
# FROM Product p
# JOIN Laptop l ON p.model = l.model
# WHERE l.hd >= 10
##################################################################################################
"""Задание: 7 Найдите номера моделей и цены всех продуктов (любого типа), выпущенных 
производителем B (латинская буква)."""
# SELECT DISTINCT Product.model, PC.price
# FROM Product JOIN PC ON Product.model = PC.model
# WHERE Product.maker = 'B'
# UNION
# SELECT DISTINCT Product.model, Laptop.price
# FROM Product JOIN Laptop ON Product.model = Laptop.model
# WHERE Product.maker = 'B'
# UNION
# SELECT DISTINCT Product.model, Printer.price
# FROM Product JOIN Printer ON Product.model = Printer.model
# WHERE Product.maker = 'B'
##################################################################################################











