DROP TABLE postal_codes CASCADE;
CREATE TABLE postal_codes (
    id INTEGER CONSTRAINT zipcodes_pk PRIMARY KEY,
    code VARCHAR(5) UNIQUE NOT NULL
);

SELECT AddGeometryColumn ('public', 'postal_codes', 'the_geom', 4326, 'POLYGON', 2);

DROP TABLE pay_stats CASCADE;
DROP TYPE age;
DROP TYPE gender;

CREATE TYPE age AS ENUM (
    '<=24', 
    '25-34',
    '35-44',
    '45-54',
    '55-64',
    '>=64' 
);

CREATE TYPE gender AS ENUM ('M', 'F');

CREATE TABLE pay_stats (
    id INTEGER PRIMARY KEY,
    postal_code_id INTEGER REFERENCES postal_codes(id),
    pay_date DATE NOT NULL,
    gender gender,
    age age,
    amount NUMERIC(16, 2) NOT NULL
);