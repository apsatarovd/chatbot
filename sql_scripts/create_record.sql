CREATE TABLE record (
         id SERIAL PRIMARY KEY,
         barber_id INT, 
         client_id INT,
         datetime TIMESTAMP,
         FOREIGN KEY (barber_id) REFERENCES barber (id),
         FOREIGN KEY (client_id) REFERENCES client (id)
);