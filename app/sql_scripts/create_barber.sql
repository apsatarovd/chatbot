CREATE TABLE IF NOT EXISTS barber(
         id SERIAL PRIMARY KEY,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         experience_years INT,
         working_hours_start TEXT NOT NULL,
         working_hours_stop  TEXT NOT NULL,
         working_days_start INT,
         working_days_stop INT
         
      );
