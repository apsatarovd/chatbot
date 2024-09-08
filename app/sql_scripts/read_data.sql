-- Чтение данных из таблиц
SELECT * FROM record; -- чтение всей таблицы 
SELECT  first_name, experience_years FROM barber; -- чтение выбранных столбцов 

SELECT * FROM barber
WHERE experience_years > 5; -- чтение с условием

-- чтение данных из таблицы client
SELECT * FROM client;

-- чтение данных из таблицы record
SELECT * FROM record;


-- чтение всех связанных таблиц 
SELECT 
    r.id AS record_id,
    c.first_name AS client_name,
    b.first_name AS barber_name,
    s.name AS service_name
FROM 
    record r
JOIN 
    client c ON r.client_id = c.id
JOIN 
    barber b ON r.barber_id = b.id
JOIN 
    service_record sr ON r.id = sr.record_id
JOIN 
    service s ON sr.service_id = s.id;