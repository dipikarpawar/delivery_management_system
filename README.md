Delivery Management System (Backend)
-------------------------------------
This is a backend system for managing food delivery orders, built with Python and Flask.
It handles restaurants, orders, delivery boys, and customers, with real-time order assignment and caching for faster operations.

Tech Stack
-------------------------------------
```Language: Python
Framework: Flask
Auth: JWT
Database: PostgreSQL
Cache: Redis (for caching and locks)
CI/CD: Git + Jenkins

Features
-------------------------------------
1. Manage orders from restaurants
2. Assign orders to delivery boys (First-Come, First-Serve)
3. Track order lifecycle:
4. Ready for pickup → Assigned → Picked up → On the way → Delivered → Cancelled/Failed
5. Delivery boy status: Available, Busy, Offline, Suspended
6. Live GPS tracking (via Redis cache)
7. Secure JWT-based authentication
8. Clean separation of models, services, repositories, and routes

Setup
-------------------------------------
1. Clone the repo

git clone <your-repo-url>
cd delivery-management-system

2. Create virtual environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

4. Setup PostgreSQL database

Create database delivery_db
Update .env with database, JWT, and Redis settings
Run migrations

5. flask db upgrade
Start the server

flask run
Server should now be running at: http://127.0.0.1:5000

Environment Variables (.env)
-------------------------------------
FLASK_ENV=development
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/delivery_db
JWT_SECRET_KEY=<your-secret-key>
REDIS_HOST=localhost
REDIS_PORT=6379

Project Structure
-------------------------------------
app/models → Database tables
app/repositories → DB access layer
app/services → Business logic (order assignment, caching, etc.)
app/routes → API endpoints
app/extensions → DB, Redis, JWT setup