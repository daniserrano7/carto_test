# CARTO Backend test - Daniel Serrano

This is a test for creating a REST API serving some spatial and non-spatial data related to card payments. Its a basic CRUD backend written in Python and Flask which serves data from a PostgreSQL/PostGIS database.

## Requirements
I was not able to setup a docker container fully functional, so, in order to run the application, there must be a PostgreSQL database already existing and Python 3 must be installed. Being in the root directory, execute
```bash
pip install -r requirements.txt
```
This will installl all the necessary packages. The, execute the following command:
```bash
start.bat
```
This

## Architecture
The main parts of the application are de database connection and the endpoints routing. Everything related to the database is under the directory "db", including parameters configuration, drivers connection and SQL schema. The endpoints are grouped ander the directory "routes". Every file represents a blueprint, which holds several endpoints related. The flask server is in the file named "server.py". 

## Endpoints
- [GET] /accumulated
- [GET] /accumulated/by_age_gender?start_date&end_date 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)