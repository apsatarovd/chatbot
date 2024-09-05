CREATE TABLE IF NOT EXISTS service (
         id SERIAL PRIMARY KEY,
         name TEXT NOT NULL,
         price INT,
         duration INT
);

