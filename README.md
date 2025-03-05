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

## Constraints  

- JWT (JSON Web Token) is used for authentication and protecting API endpoints.  
- You can use any programming language, framework, or database of your choice.  
- Any ORM or database library can be used for database interactions.  

## Getting Started  

### Prerequisites  

Ensure you have the following installed:  

- [Programming language of choice]  
- [Framework of choice]  
- [Database of choice]  

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

    

