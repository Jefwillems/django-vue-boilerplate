# django-vue-base

## Prerequisites

* [Node](https://nodejs.org/en/)
* [yarn](https://yarnpkg.com/en/)
* python v3.x (preferably a new virtualenv)

## Installation
```
$ yarn
$ pip install -r requirements.txt
```

### Compiles and hot-reloads for development
* frontend
```
yarn run serve
```
* backend

It's only possible to test the api while running this command, for see frontend updates, you have to build the frontend
```
python management.py runserver
```

### Compiles and minifies frontend for production
```
yarn run build
```

### Run your tests
```
yarn run test:unit
python manage.py test
```

### Lints and fixes frontend files
```
yarn run lint
```
