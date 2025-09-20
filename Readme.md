












<img width="788" height="700" alt="image" src="https://github.com/user-attachments/assets/9467d349-43a5-43e4-96c5-2b8f86f76e7b" />

<img width="721" height="501" alt="image" src="https://github.com/user-attachments/assets/cfaf82da-606b-4405-9589-0489c6db5611" />



<img width="605" height="293" alt="image" src="https://github.com/user-attachments/assets/f03f068f-22b5-4516-a063-9e1b450cbe8d" />


<img width="511" height="182" alt="image" src="https://github.com/user-attachments/assets/b0d8443c-11d1-47fb-86ea-d1aa6e7372fb" />


<img width="882" height="234" alt="image" src="https://github.com/user-attachments/assets/16e451b8-6331-482e-b07c-378a44eea940" />




<img width="911" height="558" alt="image" src="https://github.com/user-attachments/assets/6da65104-ddf6-466f-b3a5-07cc0f889722" />

<img width="1533" height="471" alt="image" src="https://github.com/user-attachments/assets/195cddee-a95c-4306-a007-186b7f7dec8e" />

<img width="1523" height="407" alt="image" src="https://github.com/user-attachments/assets/87330b0d-cab8-4090-8d41-be86ba56e3db" />


<img width="1542" height="406" alt="image" src="https://github.com/user-attachments/assets/89170834-07c1-4698-98fd-890d65429cac" />


<img width="1529" height="444" alt="image" src="https://github.com/user-attachments/assets/b4390103-d22b-4cce-bcd2-8026306e87ac" />


<img width="931" height="590" alt="image" src="https://github.com/user-attachments/assets/8fbebb05-cf1b-49e1-9b76-8690be835b00" />


<img width="1559" height="418" alt="image" src="https://github.com/user-attachments/assets/07e920e1-3e09-4c51-8d95-ffef07c49f7f" />

<img width="1547" height="382" alt="image" src="https://github.com/user-attachments/assets/a82643c9-9c6a-4d76-8b8a-f34d6bd44ba2" />





---














---

# Django User-Client-Project Management System Documentation

## Project Overview
This project is a Django-based REST API system for managing users, clients, and projects. It includes endpoints for client CRUD operations, project creation with user assignment, and listing assigned projects. The system uses MySQL (`nimap_db` with `root:root` credentials), supports IST timezone (+05:30), and is deployed on GitHub.

## File Structure
```python
Django-User-Client-Project-Management-System/
├── api/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/                   # Virtual environment (not in Git)
├── manage.py
├── requirements.txt
├── .gitignore
```

### File Descriptions
- **manage.py**: Django’s command-line utility for administrative tasks.
- **core/settings.py**: Configuration file with hardcoded `SECRET_KEY` and MySQL credentials (`nimap_db`, `root:root`).
- **core/urls.py**: Root URL configuration, including admin, login, and API routes.
- **api/urls.py**: API-specific URL patterns for client and project endpoints.
- **api/models.py**: Defines `Client` and `Project` models with relationships to `User`.
- **api/serializers.py**: Serializers for API data handling, including IST timezone conversion with `pytz`.
- **api/views.py**: API views for client CRUD, project creation, and project listing.
- **api/admin.py**: Registers `Client` and `Project` models in the Django admin.
- **requirements.txt**: Lists dependencies (`Django==5.2.6`, `djangorestframework==3.15.2`, `mysqlclient==2.2.4`, `pytz==2024.2`).
- **.gitignore**: Excludes `venv/`, `__pycache__/`, `*.pyc`, `*.log`, `*.sql`, `.vscode/`.

## Prerequisites
- **Operating System**: Windows
- **Python**: 3.12.4
- **MySQL**: Running (e.g., via XAMPP or MySQL Server 8.0) with `root:root` credentials
- **Git**: Installed (verify with `git --version`; download from https://git-scm.com/download/win if needed)
- **GitHub Account**: Username `Shivam1456`
- **VSCode**: Recommended for editing files
- **PowerShell**: For running commands and API tests

## Setup Instructions
Follow these steps to clone the project, set it up, and test all APIs.

### Step 1: Clone the Repository
1. **Navigate to a Directory:**
   ```python
   cd "C:\Users\Dell 5400\Desktop\Prac-Test"
   ```

2. **Clone the Repository:**
   ```python
   git clone https://github.com/Shivam1456/Django-User-Client-Project-Management-System.git
   cd Django-User-Client-Project-Management-System
   ```

### Step 2: Set Up Virtual Environment
1. **Create Virtual Environment:**
   ```python
   python -m venv venv
   ```

2. **Activate Virtual Environment:**
   ```python
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies:**
   ```python
   pip install -r requirements.txt
   ```
   Verify `requirements.txt`:
   ```python
   Django==5.2.6
   djangorestframework==3.15.2
   mysqlclient==2.2.4
   pytz==2024.2
   ```
   If installation fails, manually install:
   ```python
   pip install Django==5.2.6 djangorestframework==3.15.2 mysqlclient==2.2.4 pytz==2024.2
   ```

### Step 3: Configure MySQL Database
1. **Create Database:**
   ```python
   mysql -u root -proot
   ```
   ```python
   DROP DATABASE IF EXISTS nimap_db;
   CREATE DATABASE nimap_db;
   EXIT;
   ```

2. **Apply Migrations:**
   ```python
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Verify Tables:**
   ```python
   mysql -u root -proot
   ```
   ```python
   USE nimap_db;
   SHOW TABLES;
   ```
   Expected: `api_client`, `api_project`, `api_project_users`, `auth_user`, `authtoken_token`, etc.

### Step 4: Create Users
Create users for API testing and admin access:
```python
python manage.py shell
```
```python
from django.contrib.auth.models import User
User.objects.filter(username__in=['root', 'Rohit', 'Ganesh']).delete()
User.objects.create_superuser(username='root', password='root', email='')  # ID: 1
User.objects.create_user(username='Rohit', password='test1234')  # ID: 2
User.objects.create_user(username='Ganesh', password='test1234') # ID: 3
exit()
```

**Verify:**
```python
USE nimap_db;
SELECT id, username, is_staff, is_superuser FROM auth_user;
```
Expected:
```python
+----+----------+----------+--------------+
| id | username | is_staff | is_superuser |
+----+----------+----------+--------------+
| 1  | root     | 1        | 1            |
| 2  | Rohit    | 0        | 0            |
| 3  | Ganesh   | 0        | 0            |
+----+----------+----------+--------------+
```

### Step 5: Log In to Django Admin
1. **Run Server:**
   ```python
   python manage.py runserver
   ```

2. **Access Admin Panel:**
   - Open `http://127.0.0.1:8000/admin/` in a browser.
   - Username: `root`
   - Password: `root`
   - Should log in successfully.

### Step 6: Test APIs with PowerShell
Run these in PowerShell (in `venv`). Tests are sequential, using `Rohit` for client creation (`created_by: Rohit`) and `Ganesh` for project creation (`created_by: Ganesh`). The database is fresh, so IDs start at 1.

1. **Obtain Tokens:**
   **For `root`:**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "root", "password": "root"}'
   ```
   **Response (200 OK):**
   ```python
   {"token": "<root-token>"}
   ```
   **Extract:**
   ```python
   $response = Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "root", "password": "root"}'
   $root_token = ($response.Content | ConvertFrom-Json).token
   Write-Output $root_token
   ```
<img width="1533" height="471" alt="image" src="https://github.com/user-attachments/assets/195cddee-a95c-4306-a007-186b7f7dec8e" />

   **For `Rohit`:**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "Rohit", "password": "test1234"}'
   ```
   **Response (200 OK):**
   ```python
   {"token": "4f5d7e584ced327d41f41ecd6c0d07391f144619"}
   ```
   **Extract:**
   ```python
   $rohit_token = "4f5d7e584ced327d41f41ecd6c0d07391f144619"
   ```
<img width="1523" height="407" alt="image" src="https://github.com/user-attachments/assets/87330b0d-cab8-4090-8d41-be86ba56e3db" />

   **For `Ganesh`:**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "Ganesh", "password": "test1234"}'
   ```
   **Response (200 OK):**
   ```python
   {"token": "dda28b5053414d40ec6216c4d8480733c698a685"}
   ```
   **Extract:**
   ```python
   $ganesh_token = "dda28b5053414d40ec6216c4d8480733c698a685"
   ```
<img width="1542" height="406" alt="image" src="https://github.com/user-attachments/assets/89170834-07c1-4698-98fd-890d65429cac" />
2. **List All Clients (GET /clients/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}
   ```
   **Response (200 OK, empty):**
   ```python
   []
   ```
   **After creating clients:**
   ```python
   [
       {
           "id": 1,
           "client_name": "Nimap",
           "created_at": "2025-09-20T15:42:00.931739+05:30",
           "created_by": "Rohit"
       },
       {
           "id": 2,
           "client_name": "Infotech",
           "created_at": "2025-09-20T15:43:00.931739+05:30",
           "created_by": "Rohit"
       }
   ]
   ```
   <img width="1559" height="418" alt="image" src="https://github.com/user-attachments/assets/07e920e1-3e09-4c51-8d95-ffef07c49f7f" />
   **Error Test (no auth, 401):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method GET
   ```
   Response: `{"detail": "Authentication credentials were not provided."}`

3. **Create a New Client (POST /clients/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method POST -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": "Nimap"}'
   ```
   **Response (201 Created):**
   ```python
   {
       "id": 1,
       "client_name": "Nimap",
       "created_at": "2025-09-20T15:42:00.931739+05:30",
       "created_by": "Rohit"
   }
   ```
   **Second Client (Infotech):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method POST -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": "Infotech"}'
   ```
   **Response (201 Created):**
   ```python
   {
       "id": 2,
       "client_name": "Infotech",
       "created_at": "2025-09-20T15:43:00.931739+05:30",
       "created_by": "Rohit"
   }
   ```
   **Error Test (missing client_name, 400):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method POST -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{}'
   ```
   Response: `{"client_name": ["This field is required."]}`

4. **Retrieve Client Info (GET /clients/<id>/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}
   ```
   **Response (200 OK, initially):**
   ```python
   {
       "id": 2,
       "client_name": "Infotech",
       "projects": [],
       "created_at": "2025-09-20T15:43:00.931739+05:30",
       "created_by": "Rohit",
       "updated_at": "2025-09-20T15:43:00.931739+05:30"
   }
   ```
   **After project creation:**
   ```python
   {
       "id": 2,
       "client_name": "Infotech",
       "projects": [
           {
               "id": 1,
               "name": "Project A"
           }
       ],
       "created_at": "2025-09-20T15:43:00.931739+05:30",
       "created_by": "Rohit",
       "updated_at": "2025-09-20T15:43:00.931739+05:30"
   }
   ```
   **Error Test (invalid ID, 404):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/999/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}
   ```
   Response: `{"detail": "Not found."}`

5. **Update Client (PATCH /clients/<id>/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method PATCH -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": "company A"}'
   ```
   **Response (200 OK):**
   ```python
   {
       "id": 2,
       "client_name": "company A",
       "projects": [],
       "created_at": "2025-09-20T15:43:00.931739+05:30",
       "created_by": "Rohit",
       "updated_at": "2025-09-20T15:44:00.000000+05:30"
   }
   ```
   **Error Test (empty client_name, 400):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method PATCH -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": ""}'
   ```
   Response: `{"client_name": ["This field may not be blank."]}`

6. **Delete Client (DELETE /clients/<id>/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method DELETE -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}
   ```
   **Response (204 No Content):** (No body)
   **Error Test (invalid ID, 404):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/999/ -Method DELETE -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}
   ```
   Response: `{"detail": "Not found."}`

7. **Create Project for Client (POST /clients/<client_id>/projects/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/1/projects/ -Method POST -Headers @{"Authorization"="Token $ganesh_token"; "Content-Type"="application/json"} -Body '{"project_name": "Project A", "users": [{"id": 2, "name": "Rohit"}]}'
   ```
   **Response (201 Created):**
   ```python
   {
       "id": 1,
       "project_name": "Project A",
       "client": "Nimap",
       "users": [
           {
               "id": 2,
               "name": "Rohit"
           }
       ],
       "created_at": "2025-09-20T15:45:00.931739+05:30",
       "created_by": "Ganesh"
   }
   ```
   **Error Test (wrong name, 400):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/1/projects/ -Method POST -Headers @{"Authorization"="Token $ganesh_token"; "Content-Type"="application/json"} -Body '{"project_name": "Project A", "users": [{"id": 2, "name": "WrongName"}]}'
   ```
   Response: `{"users": ["Name does not match for user id 2"]}`

   **Error Test (non-existent user, 400):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/1/projects/ -Method POST -Headers @{"Authorization"="Token $ganesh_token"; "Content-Type"="application/json"} -Body '{"project_name": "Project A", "users": [{"id": 999, "name": "Rohit"}]}'
   ```
   Response: `{"users": ["User with id 999 does not exist"]}`

8. **List Assigned Projects (GET /projects/):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/projects/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}
   ```
   **Response (200 OK):**
   ```python
   [
       {
           "id": 1,
           "project_name": "Project A",
           "created_at": "2025-09-20T15:45:00.931739+05:30",
           "created_by": "Ganesh"
       }
   ]
   ```
   **Error Test (no auth, 401):**
   ```python
   Invoke-WebRequest -Uri http://127.0.0.1:8000/projects/ -Method GET
   ```
   Response: `{"detail": "Authentication credentials were not provided."}`

### Step 7: Update GitHub Repository
Push updates to the repository:
1. **Add and Commit:**
   ```python
   git add .
   git commit -m "Completed project setup and tested all APIs"
   ```

2. **Push to GitHub:**
   ```python
   git push origin main
   ```

3. **Verify on GitHub:** Visit https://github.com/Shivam1456/Django-User-Client-Project-Management-System.

### Troubleshooting
- **Login Issues:** If user login fails, recreate users:
  ```python
  python manage.py shell
  ```
  ```python
  from django.contrib.auth.models import User
  User.objects.filter(username__in=['root', 'Rohit', 'Ganesh']).delete()
  User.objects.create_superuser(username='root', password='root', email='')
  User.objects.create_user(username='Rohit', password='test1234')
  User.objects.create_user(username='Ganesh', password='test1234')
  exit()
  ```
- **MySQL Issues:** Ensure `mysql -u root -proot` works and `nimap_db` exists (`SHOW DATABASES;`).
- **User IDs:** Verify with:
  ```python
  USE nimap_db;
  SELECT id, username FROM auth_user;
  ```
- **Git Issues:** If `git push` fails, verify URL (`git remote -v`) and token.
- **Response Parsing:** Pipe to `| ConvertFrom-Json | Format-Table`.










---




