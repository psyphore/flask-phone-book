# flask-phone-book

My 1st take at Python, Flask, GraphQL, Neo4J

## Resources

1. [based on](https://github.com/elementsinteractive/flask-graphql-neo4j/tree/master/app)
1. [flask](http://flask.pocoo.org/)
1. [py2neo](https://py2neo.org/v4/index.html)
1. [py2neo 4](https://medium.com/neo4j/py2neo-v4-2bedc8afef2)
1. [graph dbs + python - medium](https://medium.com/labcodes/graph-databases-talking-about-your-data-relationships-with-python-b438c689dc89)
1. [graphQL + Neo4J + python - medium](https://medium.com/elements/diving-into-graphql-and-neo4j-with-python-244ec39ddd94)
1. [pypi](https://pypi.org/project/py2neo/)
1. [flask + graphql](https://bcb.github.io/python/graphql-flask)
1. [graphene-python - django](https://docs.graphene-python.org/projects/django/en/latest/)
1. [flask + graphql - medium](https://medium.com/@marvinkome/creating-a-graphql-server-with-flask-ae767c7e2525)
1. [Google Calendar API sample](https://bitbucket.org/kingmray/django-google-calendar/src/3856538e28822c5ffaba39a3258a9e833ffe413a/calendar_api/calendar_api.py?at=master&fileviewer=file-view-default)
1. [Flask + JWT](https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb)
1. [How to GraphQL](https://www.howtographql.com/graphql-python)
1. [Flask + GraphQL + JWT](https://media.readthedocs.org/pdf/flask-graphql-auth/latest/flask-graphql-auth.pdf)

## Commands

1. from clean install without pipenv

```shell
 > python install pipenv
```

1. with pipenv installed already

```shell
 > pipenv shell
 > pipenv install
 > flask run
 or
 > FLASK_APP=run.py flask run
 or
 > python run.py
```

1. running tests

```shell
running a specific test file
> python -m unittest tests/test_custom_utilities.py -v
> python -m unittest tests/test_people_service.py -v
or
running tests in discovery mode
> python -m unittest discover -v
```

## Environment Settings

```env
DEBUG=true
BIND_HOST=127.0.0.1
BIND_PORT=5000

NEO4J_HOST=localhost
NEO4J_HTTP_PORT=7474
NEO4J_BOLT_PORT=7687
NEO4J_USER=username
NEO4J_PASSWORD=password

JWT_SECRET_KEY=supersecretkey
JWT_REFRESH_EXP_LENGTH=30
JWT_ACCESS_EXP_LENGTH=10
JWT_TOKEN_ARGUMENT_NAME=Authorization
```
