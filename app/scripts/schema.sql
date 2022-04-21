DROP TABLE IF EXISTS postal_codes CASCADE;
CREATE TABLE postal_codes (
    id INTEGER  PRIMARY KEY,
    code VARCHAR(5) UNIQUE NOT NULL
);

SELECT AddGeometryColumn ('public', 'postal_codes', 'the_geom', 4326, 'MULTIPOLYGON', 2);

CREATE INDEX postal_codes_gist_idx
  ON postal_codes
  USING GIST (the_geom);

DROP TABLE IF EXISTS paystats CASCADE;
DROP TYPE IF EXISTS age;
DROP TYPE IF EXISTS gender;

CREATE TYPE age AS ENUM (
    '<=24', 
    '25-34',
    '35-44',
    '45-54',
    '55-64',
    '>=65' 
);

CREATE TYPE gender AS ENUM ('M', 'F');

CREATE TABLE paystats (
    id INTEGER PRIMARY KEY,
    postal_code_id INTEGER REFERENCES postal_codes(id),
    pay_date DATE NOT NULL,
    gender gender,
    age age,
    amount NUMERIC(16, 2) NOT NULL
);