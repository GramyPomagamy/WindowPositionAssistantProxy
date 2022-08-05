# Window Position Assistant Proxy (WPAP)

A small caching service designed to be used with [Window Position Assistant](https://github.com/GramyPomagamy/WindowPositionAssistant).
It behaves like a "JSON pastebin" – stores data sent with `POST` and returns it with `GET` for each arbitrary endpoint.

## Basic Usage

The suggested way to run WPAP is to use the provided Dockerfile to create a container.
```
$ docker build -t wpap .
$ docker run -d -p 127.0.0.1:5000:80 wpap
```

The server listens on port 80 in the container. In order to use it from outside use the `--bind` option. Exposing it on
some other custom port bound to localhost makes it easy to use with a reverse proxy, for example to provide a TLS layer.

## Advanced Usage

By default, the server runs 4 threads of [gunicorn](https://gunicorn.org/). It can be overridden with providing extra
arguments to `docker run`, for example: `docker run -d -p 127.0.0.1:5000:80 wpap --threads 42`.

Database is implemented in the filesystem to allow easy scaling of workers and threads of the production server. By
default, it's created in an ephemeral `/app/wpap_cache`. However, it can be configured with a `WPAP_DIR` environment
variable passed to the container. That way data can be persisted on restarts. For example:
```
# usage with a docker volume for storage
$ docker run -d -v wpap_volume:/storage -e WPAP_DIR=/storage -p 127.0.0.1:5000:80 wpap
```
