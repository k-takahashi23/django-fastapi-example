# fastapi-example


## Requirements

```
Python 3.9.5+
```

## How to install

```bash
$ pip install -r requirements.txt
```

## How to run

### Use docker

```bash
$ docker-compose up
```

### Use local env

```bash
$ uvicorn main:app --reload
```

### API Documents

`http://localhost:8080/docs`

## Linter

```bash
$ pip install flake8
$ pip install autopep8
```

### Check

```bash
$ flake8 .
```

### Apply

```bash
$ autopep8 --in-place --aggressive --aggressive {file_name}.py  
```