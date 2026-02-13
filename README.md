# Flask Cafe API

A RESTful API built using Flask and SQLAlchemy that allows users to view, add, update, and delete cafe data.

---

## Project Overview

- Cafe API is a RESTful web project built using Flask and a SQLite database.
- This application allows users to perform CRUD operations.
- Users can create new cafe entries in the database.
- Users can delete existing cafe data from the database.
- Users can update existing cafe prices in the database.
- Users can search cafes by location.

---

## Features

- Get a random cafe
- Get all cafes
- Search cafe by location
- Add a new cafe
- Update cafe price
- Delete cafe (API key protected)

---

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Database

The project includes a `cafes.db` file with dummy sample data for testing purposes.

Make sure to keep the folder structure unchanged, otherwise the database connection or template rendering may not work properly.

---

## API Routes

GET /random  
GET /all  
GET /search?loc=location_name  
POST /add  
GET or PATCH /update_price/<id>?new_price=price  
GET or DELETE /report_closed/<id>?api_key=topsecretkey  

---

## Quickstart

Hit the below URLs in your browser after starting the server.

### Get All Cafes (GET)

```bash
http://127.0.0.1:5000/all
```

### Get Random Cafe (GET)

```bash
http://127.0.0.1:5000/random
```

### Search Cafe by Location (GET)

```bash
http://127.0.0.1:5000/search?loc=London
```

### Update Cafe Price (GET)

```bash
http://127.0.0.1:5000/update_price/1?new_price=£4.00
```

### Delete Cafe (GET)

```bash
http://127.0.0.1:5000/report_closed/1?api_key=topsecretkey
```

---

### Note

The `/add` route must be tested using Postman or another API testing tool using the POST method with form data.
