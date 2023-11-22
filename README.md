# SailadvTest

Test project for Sailadv Junior Python Developer position

## Technologies

- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Alembic
- Docker

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LulaKebaber/SailadvTest
   ```
2. Create venv:
   
   ```bash
   python3 -m venv venv
   
   source venv/bin/activate  # MacOS
   venv\Scripts\activate  # Windows
   ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```
4. Migrate DataBase

   ```bash
   alembic upgrade head
   ```

5. Run project:

   ```bash
   docker-compose build
   docker-compose up -d
   docker-compose logs -f
   ```

## Endpoints API

| №  | Endpoint                          | Method | Description                         |
|----|-----------------------------------|--------|-------------------------------------|
| 1  | `/api/system`                     | GET    | List all systems                    |
| 2  | `/api/system`                     | POST   | Create a new system                 |
| 3  | `/api/system/{system_id:str}`     | PUT    | Update an existing system           |
| 4  | `/api/system/{system_id:str}`     | DELETE | Delete an existing system           |
| 5  | `/api/variable`                   | GET    | List all variables                  |
| 6  | `/api/variable`                   | POST   | Create a new variable               |
| 7  | `/api/variable/{variable_id:str}` | PUT    | Update an existing variable         |
| 8  | `/api/variable/{variable_id:str}` | DELETE | Delete an existing variable         |
| 9  | `/api/list`                       | GET    | Systems and variables tables return |
| 10 | `/api/logs`                       | GET    | Retrieve logs of accessed endpoints |


## Testing

1. Run tests:

   ```bash
   pytest
   ```