# FastAPI starter kit

[FastAPI](https://fastapi.tiangolo.com/) simple starter kit

## Rewuirement

Python 3.9

## Installation of dependencies

```
conda install poetry
poetry install
```

## Usage

### Running

```bash
(venv) $ python app.py
```

### Testing

```bash
(venv) $ pytest .
```

### Docker

```
docker build -t fastapi_sample .
```

```
docker run -it --name fastapi_dev -p 8080:8080 fastapi_sample:latest
```

## Application url

```
http://0.0.0.0:8080/
```

## Swagger url

```
http://0.0.0.0:8080/docs
```

## Additional helpful Docker command

```
docker rmi fastapi_sample:latest
docker image prune -f
```
