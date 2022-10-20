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
"""Задание: 8 Найдите производителя, выпускающего ПК, но не ПК-блокноты."""
# SELECT DISTINCT maker
# FROM Product
# WHERE type = 'PC'
# EXCEPT
# SELECT DISTINCT maker
# FROM Product
# WHERE type = 'Laptop'
##################################################################################################
"""Задание: 9 Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker"""
# SELECT DISTINCT maker
# FROM Product JOIN PC ON Product.model = PC.model
# WHERE PC.speed >= 450
##################################################################################################
"""Задание: 10 Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price"""
# SELECT model, price
# FROM Printer
# WHERE price = (SELECT MAX(price) FROM Printer)
##################################################################################################
"""Задание: 11 Найдите среднюю скорость ПК."""
# SELECT AVG(speed)
# FROM PC
##################################################################################################
"""Задание: 12 Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол."""
# SELECT AVG(speed)
# FROM Laptop
# WHERE Laptop.price > 1000
##################################################################################################
"""Задание: 13 Найдите среднюю скорость ПК, выпущенных производителем A."""
# SELECT AVG(speed)
# FROM PC JOIN Product ON Product.model = PC.model
# WHERE Product.maker = 'A'
##################################################################################################
"""Задание: 14 Найдите класс, имя и страну для кораблей из таблицы Ships, 
имеющих не менее 10 орудий."""
# SELECT Classes.class, name, country
# FROM Classes JOIN Ships ON Classes.class = Ships.class
# WHERE Classes.numGuns >= 10
##################################################################################################
"""Задание: 15 Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD"""
# SELECT hd
# FROM PC
# GROUP BY hd
# HAVING COUNT(hd) >= 2
##################################################################################################
"""Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается
только один раз, т.е. (i,j), но не (j,i), Порядок вывода: модель с большим номером, модель с 
меньшим номером, скорость и RAM."""
# SELECT DISTINCT i.model, j.model, i.speed, i.ram
# FROM PC i, PC j
# WHERE i.speed = j.speed AND i.ram = j.ram AND i.model > j.model
##################################################################################################
"""Задание: 17 Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК.
Вывести: type, model, speed"""
# SELECT DISTINCT type, Laptop.model, Laptop.speed
# FROM Product JOIN Laptop ON  Product.model = Laptop.model
# WHERE Laptop.speed < ALL (SELECT PC.speed FROM PC)
##################################################################################################
"""Задание: 18 Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price"""
# SELECT DISTINCT Product.maker, Printer.price
# FROM Product JOIN Printer ON Product.model = Printer.model
# WHERE Printer.color= 'y' AND Printer.price =
# (SELECT MIN(price) FROM Printer WHERE  Printer.color= 'y')
##################################################################################################
"""Задание: 19 Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер 
экрана выпускаемых им ПК-блокнотов. Вывести: maker, средний размер экрана (avg_screen)."""
# SELECT maker, AVG(screen)
# FROM Product JOIN Laptop ON Product.model = Laptop.model
# GROUP BY maker
##################################################################################################
"""Задание: 20 Найдите производителей, выпускающих по меньшей мере три различных модели ПК. 
Вывести: Maker, число моделей ПК."""
# SELECT maker, COUNT(model) as count_model
# FROM Product
# WHERE type = 'PC'
# GROUP BY maker
# HAVING  COUNT(DISTINCT model) >= 3
##################################################################################################
"""Задание: 21 Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть
модели в таблице PC. Вывести: maker, максимальная цена."""
# SELECT maker, MAX(price) AS max_price
# FROM Product JOIN PC ON Product.model = PC.model
# GROUP BY maker
##################################################################################################
"""Задание: 22 Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену
 ПК с такой же скоростью. Вывести: speed, средняя цена."""
# SELECT speed, AVG(price)
# FROM PC
# WHERE speed > 600
# GROUP BY speed
##################################################################################################
"""Задание: 23 Найдите производителей, которые производили бы как ПК со скоростью не менее 
750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц. Вывести: Maker"""
# SELECT maker
# FROM Product JOIN PC ON Product.model = PC.model
# WHERE PC.speed >= 750
# INTERSECT     # пересечение производителей (maker) из 1 и 2 таблицы
# SELECT maker
# FROM Product JOIN Laptop ON Product.model = Laptop.model
# WHERE Laptop.speed >= 750
##################################################################################################
"""Задание: 24 Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся
в базе данных продукции."""
# WITH model_price_union AS                     # создаем модель представления model_price_union
#      (SELECT model, price FROM pc             # Объеденяем данные столбцов model, price из pc
#      UNION                                    # Laptop, Printer
#      SELECT model, price  FROM Laptop
#      UNION
#      SELECT model, price  FROM Printer)
#
# SELECT model                                  # Выводим самую дорогую model из model_price_union
# FROM model_price_union
# WHERE price = (SELECT MAX(price) FROM model_price_union)  # вытягивем самую дорогую стоимость
                                                            # MAX(price) из model_price_union
##################################################################################################
"""Задание: 25 Найдите производителей принтеров, которые производят ПК с самым быстрым 
процессором среди всех ПК, имеющих наименьший объем RAM. Вывести: Maker"""
# SELECT DISTINCT maker                             # Выводим уникальных производителей
# FROM Product p JOIN PC pc ON p.model = pc.model   # Объед. две таблицы (Product, PC) по ключу
""" производитель входит в перечень производителей принтера ?"""
# WHERE maker IN (SELECT maker FROM Product WHERE type = 'Printer')
""" И максимальная скорость у ram с минимальным объемом памяти"""
# AND speed = (SELECT MAX(speed) FROM PC WHERE ram = (SELECT MIN(ram) FROM PC))
""" И с минимальным объемом памяти"""
# AND ram = (SELECT MIN(ram) FROM PC)
##################################################################################################
"""Задание: 26 Найдите среднюю цену ПК и ПК-блокнотов, выпущенных производителем 
A (латинская буква). Вывести: одна общая средняя цена."""

"""                     The first way                               """
# SELECT SUM(price)/count(quantity) AS avg_price
# FROM (SELECT price, Product.model as quantity
#       FROM PC JOIN Product ON PC.model = Product.model
#       WHERE Product.maker = 'A'
#       UNION ALL
#       SELECT price, Product.model as quantity
#       FROM Laptop JOIN Product ON Laptop.model = Product.model
#       WHERE Product.maker = 'A') as table_price_quantity
"""Выводим среднюю цену (суммируем все цены и делим на количество вещей)
Из as table_price_quantity выбираем колонки  price, Product.model as quantity от производителя А 
компьютеров и объеденяем с колонками price, Product.model as quantity от производителя А ноутбуков
Далее суммируем все цены и делим на количество вещей. Результат выводим"""

"""                     The second way                               """
# WITH price_model AS
#      (SELECT price, Product.model as model
#       FROM PC JOIN Product ON PC.model = Product.model
#       WHERE Product.maker = 'A'
#       UNION ALL
#       SELECT price, Product.model as model
#       FROM Laptop JOIN Product ON Laptop.model = Product.model
#       WHERE Product.maker = 'A')
#
# SELECT SUM(price)/count(model) AS avg_price
# FROM price_model
"""Сначала создаем модель представления model_prices. Это таблица с колонками 
price, model. price - это цены, model - это модели вещей. Далее обращаемся к нашему представлению 
(таблица). Суммируем наши цены и делим на количество моделей."""
##################################################################################################
"""Задание: 27 Найдите средний размер диска ПК каждого из тех производителей, которые выпускают и 
принтеры. Вывести: maker, средний размер HD."""
# SELECT p.maker, AVG(pc.hd)            # вывод производителя и средний размем винта
# FROM Product p JOIN PC pc ON p.model = pc.model   # объеденяем таблицы
# WHERE p.maker IN (SELECT maker FROM Product       # произв. ПК которые выпускают принтера
#                   WHERE type = 'Printer')
# GROUP BY maker                                    # группируем по производителям
##################################################################################################
"""Задание: 28 Используя таблицу Product, определить количество производителей, выпускающих 
по одной модели."""

"""                     The first way                               """
# WITH maker_count_model as                         # создаем модель (таблицу)
#       (SELECT maker, COUNT(model) as qty          # производитель | кол-во моделей
#       FROM Product                                # групируем по производителям
#       GROUP BY maker                              # сортируем производителей по кол-ву
#       HAVING COUNT(model) = 1                     # выпускаемых моделей (кол-во 1)
#       )
                                # В итоге таблица из производитлей который выпускают по 1 модели
# SELECT COUNT(maker) as qty    # Выводим кол-во производителей которые выпускают ровно 1 модель
# FROM maker_count_model        # из модели представления (таблица) maker_count_model

"""                     The second way                               """
# SELECT COUNT(maker) as qty
# FROM (SELECT maker, COUNT(model) as count_model
#       FROM Product
#       GROUP BY maker) as maker_count_model
# WHERE count_model = 1
##################################################################################################
"""Задание: 29 В предположении, что приход и расход денег на каждом пункте приема фиксируется 
не чаще одного раза в день [т.е. первичный ключ (пункт, дата)], написать запрос с выходными данными
 (пункт, дата, приход, расход). Использовать таблицы Income_o и Outcome_o."""
# SELECT o.point, o.date, inc, out       # выводим таблицу o.point, o.date, inc, out
# FROM outcome_o o LEFT JOIN             # соединяем таблицы. С права таблица будет с NULL-ами
#      income_o  i ON (o.point = i.point AND o.date = i.date)
# UNION                                  # объединяем (уникальные строки) с следующей таблицей
# SELECT i.point, i.date, inc, out       # выводим таблицу i.point, i.date, inc, out
# FROM outcome_o o RIGHT JOIN            # соединяем таблицы. С лево таблица будет с NULL-ами
#      income_o  i ON (o.point = i.point AND o.date = i.date)
##################################################################################################
"""Задание: 30 В предположении, что приход и расход денег на каждом пункте приема фиксируется 
произвольное число раз (первичным ключом в таблицах является столбец code), требуется получить 
таблицу, в которой каждому пункту за каждую дату выполнения операций будет соответствовать 
одна строка. Вывод: point, date, суммарный расход пункта за день (out), суммарный приход пункта 
за день (inc). Отсутствующие значения считать неопределенными (NULL)."""
# WITH point_date_out_inc as
#         (SELECT point, date, SUM(inc) as sum_inc, null as sum_out
#          FROM income
#          GROUP BY point, date
#          UNION
#          SELECT point, date, null as sum_inc, SUM(out) as sum_out
#          FROM outcome
#          GROUP BY point, date
#          )
#
# SELECT point, date, SUM(sum_out) outcome, SUM(sum_inc) income
# FROM point_date_out_inc
# GROUP BY point, date
##################################################################################################
"""Задание: 31 Для классов кораблей, калибр орудий которых не менее 16 дюймов, укажите класс 
и страну."""
# SELECT class, country
# FROM Classes
# WHERE bore >= 16
##################################################################################################
""""""

##################################################################################################
"""Задание: 33 Укажите корабли, потопленные в сражениях в Северной Атлантике (North Atlantic). 
Вывод: ship."""
# SELECT ship
# FROM Outcomes
# WHERE result = 'sunk' AND battle ='North Atlantic'
##################################################################################################
"""Задание: 34 По Вашингтонскому международному договору от начала 1922 г. запрещалось строить 
линейные корабли водоизмещением более 35 тыс.тонн. Укажите корабли, нарушившие этот договор 
(учитывать только корабли c известным годом спуска на воду). Вывести названия кораблей."""
# SELECT name                       # Вывод кораблей
# FROM ships                        # из таблицы ships
# WHERE launched >= 1922  AND       # которые производились с 1922 года
#       class IN (SELECT class      # подзапрос возвращ. Классы кораблей bb - линейный
#                 FROM classes      # displacement - водоизмещение свыше 35 тон
#                 WHERE type = 'bb' AND displacement > 35000)
##################################################################################################
"""Задание: 35 В таблице Product найти модели, которые состоят только из цифр или только из 
латинских букв (A-Z, без учета регистра). Вывод: номер модели, тип модели."""
# SELECT model, type
# FROM product
# WHERE model not LIKE '%[^0-9]%' or upper(model) LIKE '%[A-Z]%'
##################################################################################################
"""Задание: 36 Перечислите названия головных кораблей, имеющихся в базе данных 
(учесть корабли в Outcomes)."""




