# CARTO Backend test - Daniel Serrano

This is a test for creating a REST API serving some spatial and non-spatial data related to card payments. Its a basic CRUD backend written in Python and Flask which serves data from a PostgreSQL/PostGIS database.

## Requirements
I was not able to setup a docker container fully functional, so, in order to run the application, there must be a PostgreSQL database already existing and Python 3 must be installed. Being in the root directory, use the package manager pip to install the necessary dependencies
```bash
pip install -r requirements.txt
```

## Usage
Execute the following command to build the project:
```bash
build.bat
```
This will create the database schema, populate it with data and run the server. Alternatively, if the project is already build and you only want to run the server, use the following command:
```bash
run.bat
```
The database credentials can be set via environment variables or modifying the default values, which are stored in the /src/db/config.py file. The necessary environment variables are the following:

Env variable  | Default value
------------- | -------------
DB_HOST       | localhost
DB_NAME       | carto_test
DB_PORT       | 5432
DB_USER       | postgres
DB_PASSWORD   | password

## Architecture
The main parts of the application are de database connection and the endpoints routing. Everything related to the database is under the directory "db", including parameters configuration, drivers connection and SQL schema. The endpoints are grouped ander the directory "routes". Every file represents a blueprint, which holds several endpoints related. The flask server is in the file named "server.py". 


## Cache
Cache is implemented using flask-caching. It is only used on the developed endpoints: 
- /accumulated/by_age_gender
- /postal_codes
- /madrid_community

Caching takes into account query params. This means that using different query params like start_date and end_date in the /accumulated/by_age_gender endpoint will result in different outputs and different caches.

## Endpoints
#### - [GET] /accumulated
Returns total payment amount 

#### - [GET] /accumulated/by_age_gender?start_date&end_date
Returns accumulated payment amount segregated by age and gender

#### - [GET] /time_series
Returns turnover by age and gender

#### - [GET] /postal_codes
Returns postal codes entities including geometry

#### - [GET] /postal_codes/<postal_code_id>
Returns specified postal code data

#### - [GET] /madrid_community
Returns Madrid Community's unified geometry and aggregated turnover

## Git
The project is developed using Git Flow methodology, and the commits have the following naming convention:

- [ADD] to add a new feature or piece of code
- [UPD] to update any feature or piece of code
- [FIX] to fix an issue
- [REF] to refactor some code


## License
[MIT](https://choosealicense.com/licenses/mit/)
