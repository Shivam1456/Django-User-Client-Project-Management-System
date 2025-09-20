












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





















Django User-Client-Project Management System Setup Guide
File Structure
Django-User-Client-Project-Management-System/
├── api/
│   ├── migrations/
│   │   ├── 0001_initial.py  # Database migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Client and Project models
│   ├── serializers.py      # API serializers with IST timezone handling
│   ├── tests.py            # Test cases (empty)
│   ├── urls.py             # API URL routes
│   └── views.py            # API views
├── core/
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Project settings with hardcoded credentials
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI configuration
├── venv/                   # Virtual environment (not in Git)
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
├── .gitignore             # Git ignore file

Prerequisites

OS: Windows
Python: 3.12.4
MySQL: Running with root:root credentials (e.g., via XAMPP or MySQL Server 8.0)
Git: Installed (git --version to verify)
GitHub Account: Username Shivam1456
VSCode: Recommended for editing
Current Time: 03:17 PM IST, September 20, 2025 (for timestamp context)

Setup Instructions

Clone the Repository
cd "C:\Users\Dell 5400\Desktop\Prac-Test"
git clone https://github.com/Shivam1456/Django-User-Client-Project-Management-System.git
cd Django-User-Client-Project-Management-System


Set Up Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1


Install DependenciesVerify requirements.txt:
Django==5.2.6
djangorestframework==3.15.2
mysqlclient==2.2.4
pytz==2024.2

Install:
pip install -r requirements.txt

If errors, reinstall:
pip install Django==5.2.6 djangorestframework==3.15.2 mysqlclient==2.2.4 pytz==2024.2
pip freeze > requirements.txt


Verify .gitignoreOpen .gitignore in VSCode. It should contain:
# Virtual environment
venv/
__pycache__/
*.pyc
*.pyo
*.pyd

# Django
*.log
*.pot
*.sqlite3
local_settings.py

# VSCode
.vscode/

# MySQL database
*.sql


Configure MySQL Database
mysql -u root -proot

DROP DATABASE IF EXISTS nimap_db;
CREATE DATABASE nimap_db;
EXIT;

Verify:
SHOW DATABASES;


Apply Migrations
python manage.py makemigrations
python manage.py migrate

Verify tables:
mysql -u root -proot

USE nimap_db;
SHOW TABLES;

Expected: api_client, api_project, api_project_users, auth_user, authtoken_token, etc.

Create Users
python manage.py shell

from django.contrib.auth.models import User
User.objects.filter(username__in=['root', 'Rohit', 'Ganesh']).delete()
User.objects.create_superuser(username='root', password='root', email='')  # ID: 1
User.objects.create_user(username='Rohit', password='test1234')  # ID: 2
User.objects.create_user(username='Ganesh', password='test1234') # ID: 3
exit()

Verify:
USE nimap_db;
SELECT id, username, is_staff, is_superuser FROM auth_user;

Expected:
+----+----------+----------+--------------+
| id | username | is_staff | is_superuser |
+----+----------+----------+--------------+
| 1  | root     | 1        | 1            |
| 2  | Rohit    | 0        | 0            |
| 3  | Ganesh   | 0        | 0            |
+----+----------+----------+--------------+


Run Server
python manage.py runserver



API Testing
Test APIs using PowerShell’s Invoke-WebRequest. Tests are sequential, using Rohit for client creation (created_by: Rohit) and Ganesh for project creation (created_by: Ganesh).

Obtain TokensFor root:
Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "root", "password": "root"}'

Response (200 OK):
{"token": "b97f0aee91bf358d83941a285a47ce486f32f6a0"}

Extract:
$response = Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "root", "password": "root"}'
$root_token = ($response.Content | ConvertFrom-Json).token
Write-Output $root_token

For Rohit:
Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "Rohit", "password": "test1234"}'

Response (200 OK):
{"token": "4f5d7e584ced327d41f41ecd6c0d07391f144619"}

Extract:
$response = Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "Rohit", "password": "test1234"}'
$rohit_token = ($response.Content | ConvertFrom-Json).token
Write-Output $rohit_token

For `Ganesh:**
Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "Ganesh", "password": "test1234"}'

Response (200 OK):
{"token": "dda28b5053414d40ec6216c4d8480733c698a685"}

Extract:
$response = Invoke-WebRequest -Uri http://127.0.0.1:8000/login/ -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"username": "Ganesh", "password": "test1234"}'
$ganesh_token = ($response.Content | ConvertFrom-Json).token
Write-Output $ganesh_token

Set tokens:
$root_token = "b97f0aee91bf358d83941a285a47ce486f32f6a0"
$rohit_token = "4f5d7e584ced327d41f41ecd6c0d07391f144619"
$ganesh_token = "dda28b5053414d40ec6216c4d8480733c698a685"


List All Clients (GET /clients/)
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}

Response (200 OK, empty):
[]

After creating clients:
[
    {
        "id": 1,
        "client_name": "Nimap",
        "created_at": "2025-09-20T15:20:00.931739+05:30",
        "created_by": "Rohit"
    },
    {
        "id": 2,
        "client_name": "Infotech",
        "created_at": "2025-09-20T15:21:00.931739+05:30",
        "created_by": "Rohit"
    }
]

Error Test (no auth, 401):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method GET

Response: {"detail": "Authentication credentials were not provided."}

Create a New Client (POST /clients/)
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method POST -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": "Nimap"}'

Response (201 Created):
{
    "id": 1,
    "client_name": "Nimap",
    "created_at": "2025-09-20T15:20:00.931739+05:30",
    "created_by": "Rohit"
}

Second Client (Infotech):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method POST -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": "Infotech"}'

Response (201 Created):
{
    "id": 2,
    "client_name": "Infotech",
    "created_at": "2025-09-20T15:21:00.931739+05:30",
    "created_by": "Rohit"
}

Error Test (missing client_name, 400):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/ -Method POST -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{}'

Response: {"client_name": ["This field is required."]}

Retrieve Client Info (GET /clients//)
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}

Response (200 OK, initially):
{
    "id": 2,
    "client_name": "Infotech",
    "projects": [],
    "created_at": "2025-09-20T15:21:00.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2025-09-20T15:21:00.931739+05:30"
}

After project creation:
{
    "id": 2,
    "client_name": "Infotech",
    "projects": [
        {
            "id": 1,
            "name": "Project A"
        }
    ],
    "created_at": "2025-09-20T15:21:00.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2025-09-20T15:21:00.931739+05:30"
}

Error Test (invalid ID, 404):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/999/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}

Response: {"detail": "Not found."}

Update Client (PATCH /clients//)
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method PATCH -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": "company A"}'

Response (200 OK):
{
    "id": 2,
    "client_name": "company A",
    "projects": [],
    "created_at": "2025-09-20T15:21:00.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2025-09-20T15:22:00.000000+05:30"
}

Error Test (empty client_name, 400):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method PATCH -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"} -Body '{"client_name": ""}'

Response: {"client_name": ["This field may not be blank."]}

Delete Client (DELETE /clients//)
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/2/ -Method DELETE -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}

Response (204 No Content): (No body)Error Test (invalid ID, 404):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/999/ -Method DELETE -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}

Response: {"detail": "Not found."}

Create Project for Client (POST /clients//projects/)
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/1/projects/ -Method POST -Headers @{"Authorization"="Token $ganesh_token"; "Content-Type"="application/json"} -Body '{"project_name": "Project A", "users": [{"id": 2, "name": "Rohit"}]}'

Response (201 Created):
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
    "created_at": "2025-09-20T15:23:00.931739+05:30",
    "created_by": "Ganesh"
}

Error Test (wrong name, 400):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/1/projects/ -Method POST -Headers @{"Authorization"="Token $ganesh_token"; "Content-Type"="application/json"} -Body '{"project_name": "Project A", "users": [{"id": 2, "name": "WrongName"}]}'

Response: {"users": ["Name does not match for user id 2"]}
Error Test (non-existent user, 400):
Invoke-WebRequest -Uri http://127.0.0.1:8000/clients/1/projects/ -Method POST -Headers @{"Authorization"="Token $ganesh_token"; "Content-Type"="application/json"} -Body '{"project_name": "Project A", "users": [{"id": 999, "name": "Rohit"}]}'

Response: {"users": ["User with id 999 does not exist"]}

List Assigned Projects (GET /projects/)
Invoke-WebRequest -Uri http://127.0.0.1:8000/projects/ -Method GET -Headers @{"Authorization"="Token $rohit_token"; "Content-Type"="application/json"}

Response (200 OK):
[
    {
        "id": 1,
        "project_name": "Project A",
        "created_at": "2025-09-20T15:23:00.931739+05:30",
        "created_by": "Ganesh"
    }
]

Error Test (no auth, 401):
Invoke-WebRequest -Uri http://127.0.0.1:8000/projects/ -Method GET

Response: {"detail": "Authentication credentials were not provided."}


Update GitHub Repository

Add and Commit:
git add .
git commit -m "Updated project setup and tested all APIs"


Push to GitHub:
git push origin main


Verify on GitHub: Visit https://github.com/Shivam1456/Django-User-Client-Project-Management-System.


Troubleshooting

Dependency Issues: If pip install -r requirements.txt fails, reinstall:pip install Django==5.2.6 djangorestframework==3.15.2 mysqlclient==2.2.4 pytz==2024.2


MySQL Issues: Ensure mysql -u root -proot works and nimap_db exists (SHOW DATABASES;).
User IDs: Verify with:USE nimap_db;
SELECT id, username FROM auth_user;


Git Issues: If git push fails, verify URL (git remote -v) and token.
Response Parsing: Pipe to | ConvertFrom-Json | Format-Table.






---




