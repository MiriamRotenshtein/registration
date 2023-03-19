# FastAPI

This project is a FastAPI-based web service for managing user information.
## Getting Started

To run the service, you can use Docker to build and run the container:
docker build -t myapp .
docker run -p 8000:8000 -v /path/to/local/directory:/app myapp
You can then access the API at `http://localhost:8000/docs`.

## API Endpoints

The service provides the following API endpoints:

  - `GET /users`: Returns a list of the 10 most recently added users.
  - `POST /users`: Adds a new user to the system.

Both endpoints expect and return JSON data.

## Data Model
The user model consists of the following fields:

  - id (int): Unique identifier for the user.
  - email (str): Email address of the user.
  - name (str): Name of the user.
  - password (str): Password of the user.
  - age (int): Age of the user.

## Dependencies
The service depends on the following Python packages:

    fastapi
    uvicorn
    pydantic

These packages are included in the requirements.txt file.