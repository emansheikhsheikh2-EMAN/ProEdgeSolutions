# Day 38 - Multi-Service Deployment with Docker Compose

## Objective

Learn how to manage multiple containers using Docker Compose and understand how services communicate within a containerized environment.

## Task

Extend the Dockerized ML Prediction API from Day 37 into a multi-service application by connecting it with Redis using Docker Compose.

## Services

This project contains two services:

### 1. ML Prediction API

* Built with FastAPI
* Runs on port `8000`
* Provides health and prediction endpoints
* Uses the trained ML model for customer churn prediction

### 2. Redis

* Redis version `7-alpine`
* Runs on port `6379`
* Used as the secondary service
* Stores the prediction counter

## Project Structure

```text
Day-38-Docker-Compose/
│
├── models/
│   └── churn_model_v1.joblib
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── logging_config.py
│   ├── main.py
│   └── models.py
│
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Docker Compose Configuration

The `docker-compose.yml` file defines both services:

```yaml
services:
  api:
    build: .
    container_name: ml_prediction_api
    ports:
      - "8000:8000"
    environment:
      REDIS_HOST: redis
      REDIS_PORT: 6379
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    container_name: ml_prediction_redis
    ports:
      - "6379:6379"
```

## Environment Variables

The Redis configuration is passed to the API through Docker Compose:

```text
REDIS_HOST=redis
REDIS_PORT=6379
```

The API uses `redis` as the Redis host because `redis` is the service name in Docker Compose.

## Running the Application

Build and start both services with:

```powershell
docker compose up --build
```

To run the services in detached mode:

```powershell
docker compose up --build -d
```

## Check Running Containers

```powershell
docker ps
```

The following containers should be running:

```text
ml_prediction_api
ml_prediction_redis
```

## API Endpoints

### Health Check

```text
GET /health
```

Expected response:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Redis Health Check

```text
GET /redis-health
```

Expected response:

```json
{
  "status": "connected",
  "redis_host": "redis",
  "redis_port": 6379
}
```

This confirms that the API successfully communicates with Redis.

### Prediction

```text
POST /predict
```

Example response:

```json
{
  "prediction": 0,
  "churn": "No",
  "message": "Prediction generated successfully"
}
```

Each successful prediction increments the Redis `prediction_count`.

## Redis Verification

The Redis counter can be checked using:

```powershell
docker exec ml_prediction_redis redis-cli GET prediction_count
```

Example output:

```text
1
```

This confirms that the API successfully communicated with Redis and updated the counter.

## Docker Networking

Docker Compose automatically creates a network for the services.

The API connects to Redis using the service name:

```text
REDIS_HOST=redis
```

The communication works as follows:

```text
ML Prediction API
        |
        | Docker Compose Network
        |
        v
      Redis
```

## Verification

The following tests were successfully performed:

* API container started successfully.
* Redis container started successfully.
* API health check returned `healthy`.
* Redis health check returned `connected`.
* ML prediction was generated successfully.
* Redis prediction counter was updated successfully.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Docker
* Docker Compose
* Redis
* Pydantic
* Scikit-learn
* Joblib
* Pandas
* NumPy

## Screenshots

### Docker Compose Services

Add screenshot here:

```text
screenshots/Day-38-Docker-Compose-Services.png
```

### Redis Health Check

Add screenshot here:

```text
screenshots/Day-38-Redis-Health.png
```

### API Health Check

Add screenshot here:

```text
screenshots/Day-38-API-Health.png
```

### Prediction Response

Add screenshot here:

```text
screenshots/Day-38-Prediction.png
```

### Redis Counter

Add screenshot here:

```text
screenshots/Day-38-Redis-Counter.png
```

## Conclusion

Day 38 successfully extends the Dockerized ML Prediction API into a multi-service application using Docker Compose.

The ML Prediction API and Redis run as separate containers and communicate successfully through the Docker Compose network. Environment variables are used to configure the Redis connection.
