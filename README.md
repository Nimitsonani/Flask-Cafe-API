# Flask Cafe API

This is a RESTful API built with Flask and SQLAlchemy.

It exposes endpoints to perform CRUD operations on a café database.  
The project focuses on building structured API routes, handling HTTP methods properly, and interacting with a relational database using an ORM.

---

## What This Project Does

The API allows clients to:

- Retrieve café data
- Search cafés by location
- Add new cafés
- Update café pricing
- Delete cafés (API key protected)

All data is stored in a SQLite database using SQLAlchemy models.

The goal of this project was to build a clean REST-style backend with proper route design and database interaction.

---

## How It Works

- Each café is stored as a row in the `cafes.db` SQLite database.
- SQLAlchemy handles database operations through ORM models.
- Different HTTP methods are used for different operations:
  - `GET` → Retrieve data
  - `POST` → Create new data
  - `PATCH` → Update existing data
  - `DELETE` → Remove data

The delete endpoint requires an API key as a simple protection mechanism.

---

## Available Routes

### Retrieve Data

- `GET /random` → Returns a random café  
- `GET /all` → Returns all cafés  
- `GET /search?loc=location_name` → Search cafés by location  

### Modify Data

- `POST /add` → Add a new café  
- `PATCH /update_price/<id>?new_price=price` → Update café price  
- `DELETE /report_closed/<id>?api_key=topsecretkey` → Delete café  

---

## Example Requests

Get all cafés:

```
http://127.0.0.1:5000/all
```

Get a random café:

```
http://127.0.0.1:5000/random
```

Search by location:

```
http://127.0.0.1:5000/search?loc=London
```

Update price:

```
http://127.0.0.1:5000/update_price/1?new_price=£4.00
```

Delete café:

```
http://127.0.0.1:5000/report_closed/1?api_key=topsecretkey
```

The `/add` route should be tested using Postman or another API client with the `POST` method and form data.

---

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite

---

## Database

The repository includes a `cafes.db` file with sample data for testing.

The database is connected through SQLAlchemy ORM.  
Folder structure should remain unchanged so the database path resolves correctly.

---

## Running Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
python main.py
```

The server will start on:

```
http://127.0.0.1:5000
```
