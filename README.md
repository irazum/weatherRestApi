# Weather REST API

### Description
It is a REST API service for getting a weather forecast by the Latin name of a city. The app uses weather data from OpenWeatherMap API.

This app is the test task from EPAM.

Requirements:
* choice of units, Celsius or Fahrenheit
* weather forecast should to be able only for authorized users
* caching requests to API for 1 min
* the app should to work in a Docker container
* code coverage
* clear API documentation

### Documentation
Please, see the [API documentation](https://github.com/irazum/weatherRestApi/wiki) in the wiki tab.


### Usage
```
python manage.py runserver
```