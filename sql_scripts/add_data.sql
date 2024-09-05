-- Добавление данных в таблицу barber
INSERT INTO barber (first_name, last_name, experience_years, working_hours_start, working_hours_stop, working_days_start, working_days_stop) 
VALUES ('Bob', 'Smith', 10, '08:00', '16:00', 1, 5);

INSERT INTO barber (first_name, last_name, experience_years, working_hours_start, working_hours_stop, working_days_start, working_days_stop) 
VALUES ('John', 'Doe', 5, '12:00', '20:00', 2, 6);

-- Добавление данных в таблицу client
INSERT INTO client (first_name, last_name, phone) 
VALUES ('Alice', 'Johnson', '123-123-0077');

INSERT INTO client (first_name, last_name, phone) 
VALUES ('Emma', 'Watson', '996-555-8833');

-- Добавление данных в таблицу service
INSERT INTO service (name, price, duration) 
VALUES ('Haircut', 1500, 30);

INSERT INTO service (name, price, duration) 
VALUES ('Shave', 800, 15);

-- Добавление записей в таблицу record
INSERT INTO record (barber_id , datetime, client_id) VALUES ( 1, '2024-09-07', 1);
INSERT INTO record (barber_id, datetime, client_id) VALUES (5, '2024-09-12', 7);

-- Добавление записей в таблицу service_record
INSERT INTO service_record values (6,2), (2,1);
INSERT INTO service_record values (6,7), (3,2);







-- Чтение данных из таблиц
SELECT * FROM record; -- чтение всей таблицы 
SELECT  first_name, experience_years FROM barber; -- чтение выбранных столбцов 

SELECT * FROM barber
WHERE experience_years > 5; -- чтение с условием