# practicum_diplom - это 2-я часть дипломного проекта на курсе Инженер по тестированию +
# Яндекс Практикум
Описание:
# 1. Работа с базой данных
Запросы расположены в файле Base.sql 
Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
запрос:
          SELECT c."login" AS login, COUNT(o."id")
          FROM "Orders" o
          INNER JOIN "Couriers" c on o."courierId" = c.id
          WHERE "inDelivery" = true
          GROUP BY login;
Скриншот результата запроса 1_sql.png (директория \practicum_diplom)

Задание 2
При тестировании заказов нужно убедиться, что в базе данных они записываются корректно.

Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.
запрос:
           SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
    FROM
    "Orders";
Скриншот результата запроса 2_sql.png 

# 2. Автоматизация теста.
Для запуска теста необходимо в файл configuration скопировить URLстенда вида 
https:"https://d02797bd-9c4e-44aa-9bc5-863399ebb0d0.serverhub.praktikum-services.ru"
В файле sendor_stand_request нажать кнопку Run 
Скриншот автоматизации  Autotest.png (директория \practicum_diplom)
