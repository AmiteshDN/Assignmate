# AssignMate Project Documentation

- **Project Name:** AssignMate
- Project Type: Django REST Framework + Auth0 authentication
- Prepared By: Amitesh Veeragattam
- Date: 29/10/2025

## 1. Project Overview

## Purpose:
AssignMate is a platform that allows students and tutors to collaborate on coding assignments. It includes secure user management, assignment posting, and tutor interactions.

## Key Features:

User authentication via Auth0 (JWT-based)

Role-based access control (student, tutor)

Assignment management (create, edit, assign)

Comments and review system

Secure API endpoints protected with JWT tokens

## Architecture Diagram:
(Optional: add diagram showing Django backend, Auth0, and client flow)

## 2. Environment Setup

### Prerequisites:

Python 3.13+

Django 4.2+

PostgreSQL database

Virtual environment (venv)

Auth0 account and application

### Steps:

- Clone repository:

git clone <repo_url>
cd AssignMate
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt


Configure .env file:

SECRET_KEY=<your_secret_key>
DB_NAME=assignmate_db
DB_USER=assignmate_user
DB_PASSWORD=<db_password>
DB_HOST=127.0.0.1
DB_PORT=5432
AUTH0_DOMAIN=dev-qveoo10p8efuoeiu.us.auth0.com
AUTH0_CLIENT_ID=<your_auth0_client_id>
AUTH0_CLIENT_SECRET=<your_auth0_client_secret>
AUTH0_AUDIENCE=http://localhost:8000/users


Apply migrations:

python manage.py migrate

3. Auth0 Integration

JWT Validation:

Tokens issued by Auth0 contain claims like sub (user ID), aud (audience), iss (issuer), exp (expiration).

Custom JWT Validator:

users/validator.py validates JWT tokens against Auth0 JWKS.

Checks:

Signature

Issuer (iss)

Audience (aud)

Expiration (exp)

Custom Authentication Class:

users/authentication.py (Auth0Authentication)

Uses Auth0JWTBearerTokenValidator to validate tokens.

Returns (user, token):

user is a Django User object created on-the-fly using the sub claim.

Ensures DRF permission classes (like IsAuthenticated) work properly.

DRF Viewset Configuration:

authentication_classes = [Auth0Authentication]
permission_classes = [IsAuthenticated]


REST Framework Settings in settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'users.authentication.Auth0Authentication',  # JWT first
        'rest_framework.authentication.SessionAuthentication',  # fallback for browsable API
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


Flow Summary:

Client sends JWT token in Authorization header.

Auth0Authentication validates the token.

Local Django user is created/retrieved using sub.

IsAuthenticated permission verifies access.

Viewset executes and returns response.

4. API Endpoints
Endpoint	Method	Authentication	Description
/api/users/	GET	JWT Token	List all users
/api/users/<id>/	GET	JWT Token	Retrieve user details
/api/assignments/	POST	JWT Token	Create a new assignment
/api/assignments/<id>/	GET/PUT/DELETE	JWT Token	Assignment CRUD operations
/api/assignments/<id>/requests/	POST	JWT Token	Send assignment request
/api/assignments/<id>/requests/<req_id>/accept/	POST	JWT Token	Tutor accepts assignment request

(Update/add endpoints as implemented)

5. Progress / Work Done

Configured environment and .env variables for Django + Auth0.

Installed and configured authlib for JWT validation.

Created Auth0JWTBearerTokenValidator for token verification.

Implemented Auth0Authentication class for DRF viewsets.

Secured /api/users endpoint with JWT-based authentication.

Configured DRF settings with authentication priority:

Auth0 JWT first

SessionAuthentication as fallback

Verified flow: token validation → user creation → permission check → view execution.

Learned DRF’s authentication-permission dependency and JWT integration patterns.

6. Next Steps

Secure remaining API endpoints using Auth0 JWT.

Implement role-based access control using Auth0 claims and local user roles.

Test token expiration, revocation, and refresh flows.

Document all endpoints with request/response examples (consider Swagger/OpenAPI).

Add automated tests for authentication and permissions.

7. References

Django REST Framework – Authentication

Django REST Framework – Permissions

Auth0 Docs – Django Integration

Authlib Documentation

