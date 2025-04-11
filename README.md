## Overview

A simple CRUD API template using Flask. Designed for students to learn by building on top of prewritten tests.

The application is a simple car inventory system.
Each `Car` object will have the following fields:

you can use in memory list to store the values.

- `id`: Integer
- `make`: String
- `model`: String
- `year`: Integer

## 🚗 CRUD Operations

Create endpoints for:

- POST `/cars` - Add a car
- GET `/cars` - List all cars
- GET `/cars/<id>` - List car with matching id
- PUT `/cars/<id>` - Update a car
- DELETE `/cars/<id>` - Remove a car

## 🧪 Tests

Run locally:

```bash
pip install -r requirements.txt
pytest
```

## Note:

**make sure to pass tests before pass test before uploading to main branch**

**Do Not** remove or modify `.github` and `tests` folder they contain important code for evaluation.
