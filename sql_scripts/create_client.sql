CREATE TABLE IF NOT EXISTS client(
         id SERIAL PRIMARY KEY,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         phone VARCHAR
      );
