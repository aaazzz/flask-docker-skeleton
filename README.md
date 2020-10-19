# Flask Docker Skelton

## Run production server

localhost:5000 -> ((nginx:80 -> uwsgi:3031) + supervisord)

```shell
$ docker-compose up
```

http://localhost:5000


## Run development server

Development server supports auto reload after every code change.
a flask app derectly runs on localhost:5000.

```shell
$ python app/server.py
```
