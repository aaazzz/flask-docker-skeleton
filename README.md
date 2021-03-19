# Flask Docker Skeleton

## Run production server

localhost:5000 -> ((nginx:80 -> socket -> uwsgi) + supervisord)

```shell
$ docker-compose up
```

## Run development server

Development server supports auto reload after every code change.
a flask app derectly runs on localhost:5000.

```shell
$ python app/server.py
```

When you change the `ini` files under `etc` directory, copy it directly to the docker container so that you can save your build time.

```shell
$ docker cp app/etc/nginx.conf app:/etc/nginx/nginx.conf
```
