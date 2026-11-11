# Calculator API

A FastAPI service that adds, subtracts, divides, and multiplies two numbers, with Docker and Docker Compose support.

## Run with Docker Compose

Install Docker with the Compose plugin and start Docker, then run:

```powershell
docker compose up --build -d
```

This builds the `calculator-addition:local` image and serves the API on port 8000.
Open http://localhost:8000/docs to try the endpoint in the interactive API docs.

Stop the service:

```powershell
docker compose down
```

## Build and run the Docker image directly

```powershell
docker build -t calculator-addition:local .
docker run --rm -p 8000:8000 calculator-addition:local
```

## Run locally without Docker

Use Python 3.10 or newer. In PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

## Add two numbers

Send a `POST` request to `http://localhost:8000/add` with a JSON body:

```json
{"a": 10, "b": 5}
```

Response:

```json
{"result": 15.0}
```

PowerShell example:

```powershell
Invoke-RestMethod -Uri http://localhost:8000/add -Method Post -ContentType 'application/json' -Body '{"a":10,"b":5}'
```

## Subtract two numbers

Send a `POST` request to `http://localhost:8000/subtract` with a JSON body.
The endpoint calculates `a - b`:

```json
{"a": 10, "b": 5}
```

Response:

```json
{"result": 5.0}
```

PowerShell example:

```powershell
Invoke-RestMethod -Uri http://localhost:8000/subtract -Method Post -ContentType 'application/json' -Body '{"a":10,"b":5}'
```

## Divide two numbers

Send a `POST` request to `http://localhost:8000/divide` with a JSON body.
The endpoint calculates `a / b`:

```json
{"a": 10, "b": 5}
```

Response:

```json
{"result": 2.0}
```

PowerShell example:

```powershell
Invoke-RestMethod -Uri http://localhost:8000/divide -Method Post -ContentType 'application/json' -Body '{"a":10,"b":5}'
```

Dividing by zero returns HTTP 422 with `{"detail":"Cannot divide by zero."}`.

## Multiply two numbers

Send a `POST` request to `http://localhost:8000/multiply` with a JSON body.
The endpoint calculates `a * b`:

```json
{"a": 10, "b": 5}
```

Response:

```json
{"result": 50.0}
```

PowerShell example:

```powershell
Invoke-RestMethod -Uri http://localhost:8000/multiply -Method Post -ContentType 'application/json' -Body '{"a":10,"b":5}'
```

All endpoints support negative numbers and decimals. Missing fields, invalid numbers,
non-finite numbers, and results outside the supported range return HTTP 422.
Numbers use floating-point arithmetic, so decimal results may have rounding effects.

`GET /health` returns `{"status":"ok"}`.

## Project files

- `main.py`: FastAPI application and input validation.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Instructions for building the Docker image.
- `compose.yaml`: Docker Compose service and health check.
- `.gitignore`: Excludes local environments, caches, and secrets from Git.
- `.dockerignore`: Limits the Docker build context to application files.

Docker setup follows the [FastAPI container documentation](https://fastapi.tiangolo.com/deployment/docker/).
