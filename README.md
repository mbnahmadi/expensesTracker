# Expense Tracker API  

A simple Expense Tracker API that allows users to manage their expenses efficiently. The API supports authentication using JWT and provides endpoints to create, list, filter, update, and delete expenses.

## Features  

- **User Authentication**  
  - Sign up as a new user  
  - Generate and validate JWTs for authentication  

- **Expense Management**  
  - Add new expenses  
  - List and filter past expenses:  
    - Past week  
    - Past month  
    - Last 3 months  
    - Custom date range (start and end date)  
  - Update existing expenses  
  - Remove expenses  

## Categories  

The following categories are available for expenses:  

- Groceries  
- Leisure  
- Electronics  
- Utilities  
- Clothing  
- Health  
- Others  


## Getting Started  

### Prerequisites  

Ensure you have the following installed:  

- python 3.10 r later 
- django 5.1 or later 
- postgresql 

### Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/mbnahmadi/expensesTracker.git
   cd expensesTracker


2. Install dependencies:
    ```sh
    pip install -r requirements.txt 

3. Set up the database and apply migrations:
    ```sh
    python manage.py migrate

4. Start the API server:
    ```sh
    python manage.py runserver



### API Endpoints  

| Method  | Endpoint                  | Description                | Authentication |
|---------|---------------------------|----------------------------|---------------|
| POST    | /auth/signup              | Register a new user        | ❌            |
| POST    | /auth/login               | Generate JWT token         | ❌            |
| POST    | /auth/login/refresh/      | Generate refresh JWT token | ❌            |
| GET     | /expense/list/            | List & filter expenses     | ✅            |
| GET     | /expense/filter/          | Filter expenses            | ✅            |
| POST    | /expense/create/          | Add a new expense          | ✅            |
| PUT     | /expense/update/{id}      | Update an expense          | ✅            |
| DELETE  | /expense/delete/{id}      | Remove an expense          | ✅            |

    

## API Documentation  

This project uses **Swagger UI** for API documentation.  

You can access the interactive API documentation at:  

- **Swagger UI**: [`http://localhost:8000/swagger/`](http://localhost:8000/swagger/)  
- **Redoc UI**: [`http://localhost:8000/redoc/`](http://localhost:8000/redoc/)  

https://roadmap.sh/projects/expense-tracker-api
