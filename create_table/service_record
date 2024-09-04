CREATE TABLE IF NOT EXISTS service_record (
         record_id INT REFERENCES RECORD(ID),
         service_id INT REFERENCES SERVICE(ID),
         CONSTRAINT service_record_pk PRIMARY KEY (record_id, service_id)
);
