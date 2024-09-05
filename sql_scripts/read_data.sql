-- Чтение данных из таблиц
SELECT * FROM record; -- чтение всей таблицы 
SELECT  first_name, experience_years FROM barber; -- чтение выбранных столбцов 

SELECT * FROM barber
WHERE experience_years > 5; -- чтение с условием