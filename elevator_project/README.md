# Elevator Prediction Data App

## Purpose

- Generate synthetic elevator data suitable for ML model training.
- Provide basic CRUD endpoints using FastAPI.

## Schema

- **Elevator Events** table:
  - `timestamp`: Date and time of the event.
  - `elevator_id`: Elevator identifier.
  - `transition`: Elevator state transition (`resting`, `on_demand`, `vacant`).
  - `floor`: Current floor of the elevator.

## Business Rules

- Elevator automatically repositions to the reset floor (`0`) if idle for more than 30 minutes on a non-reset floor.

## How to Run the Application (Docker)

Navigate to the root folder of the project and build/run the Docker containers:

```bash
sudo docker-compose up --build
```

## Populate Database with Synthetic Data

After the Docker container is running, open another terminal and execute:

```bash
sudo docker-compose exec api python -m app.populate_db
```

This script populates the database with synthetic elevator data.

## Available API Endpoints

The FastAPI application provides the following endpoints:

### Create Event

- **POST** `/events/`

Creates a new elevator event.

Example payload:
```json
{
  "timestamp": "2025-03-20T15:53:17.817Z",
  "elevator_id": 1,
  "transition": "resting",
  "floor": 0
}
```

### Read Events

- **GET** `/events/`

Returns a list of recent elevator events.

### Query Events

- **POST** `/events/query/`

Query elevator events based on a specific date/time interval and elevator ID.

Example payload:
```json
{
  "start_datetime": "2025-03-20T15:00:00.000Z",
  "end_datetime": "2025-03-20T16:00:00.000Z",
  "elevator_id": 1
}
```

Returns events within the specified interval.

## Swagger UI

You can explore and test the endpoints by visiting:
```
http://localhost:8000/docs

