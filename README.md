# 🧑‍💻 AssignMate - Coding Assignment Collaboration Platform

AssignMate is a role-based web platform built with Django that connects students and tutors to collaborate on coding assignments. It supports secure OAuth login via Google and GitHub, enforces role-based access control (RBAC), and is designed with a RESTful API-first approach.

---

## 🚀 Features

### ✅ User Management
- Custom user model with email as the primary identifier
- OAuth 2.0 based login and registration using **Google** and **GitHub**
- Roles: **Student**, **Tutor**, **Admin**
- Secure login, logout, and session/token handling (OAuth-based)
- Role-based permissions for different actions

### 🛡 Role-Based Access Control (RBAC)
- `Role`, `Permission`, and `UserRole` models
- Each role (Student, Tutor, Admin) has a set of defined permissions
- Permissions include actions like:
  - Posting or editing assignments
  - Sending/accepting assignment requests
  - Managing comments and reviews
  - Admin-level control of roles and permissions
- Role-based view restrictions (to be implemented with decorators or permission checks)

### 🧩 Assignment & Collaboration (Upcoming)
- REST APIs for:
  - Creating and managing assignments
  - Sending/receiving assignment requests
  - Commenting and reviewing
- Permissions enforced per role

---

## ⚙️ Tech Stack

| Layer         | Technology               |
|---------------|---------------------------|
| Backend       | Django, Django REST Framework |
| Auth          | `django-allauth`, `dj-rest-auth`, OAuth2 |
| OAuth Providers | Google, GitHub         |
| Database      | PostgreSQL               |
| Frontend (Planned) | React / JS SPA     |

---

## 📂 Project Structure (simplified)

```
assignmate/
├── users/
│   ├── models.py            # Custom User, Role, Permission, UserRole
│   ├── serializers.py       # For user-related REST APIs
│   ├── views.py             # Login/Logout/Register (OAuth managed)
├── assignment/
│   ├── models.py            # Assignment, AssignmentRequest (planned)
│   ├── views.py             # Role-based protected APIs
├── core/
│   ├── settings.py          # Config: Installed apps, middleware, auth backends
├── templates/
│   ├── account/             # Social login templates (used by allauth)
├── README.md
└── manage.py
```

---

## 🔐 OAuth Setup

You’ve configured `django-allauth` for:
- Google login (with redirect URI: `http://localhost:8000/accounts/google/login/callback/`)
- GitHub login (with redirect URI: `http://localhost:8000/accounts/github/login/callback/`)

### To configure social login:
- Register your app credentials on:
  - [Google Developer Console](https://console.developers.google.com/)
  - [GitHub Developer Settings](https://github.com/settings/developers)
- Add the corresponding **client ID/secret** in Django Admin > Social Applications

---

## 🧪 Development Status

| Feature                            | Status        |
|------------------------------------|---------------|
| Custom User Model                  | ✅ Complete   |
| Social Login (Google, GitHub)      | ✅ Complete   |
| Role/Permission Models             | ✅ Complete   |
| REST APIs for Assignment Tasks     | 🚧 In Progress |
| Token-based Auth Integration       | ⚙️ Planned   |
| Role-Based Decorators              | ⚙️ Planned   |
| Frontend React Integration         | 🕓 Planned   |

---

## 🛠 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/assignmate.git
cd assignmate
```

2. **Create a virtual environment & install dependencies**

```bash
python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. **Apply migrations & run server**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

4. **Test social login**
- Navigate to `/accounts/login/` and try logging in with Google or GitHub.

---

## 📌 Notes

- The backend is being built REST-first, so even though `django-allauth` provides default templates, a modern React frontend is planned.
- OAuth handles authentication; authorization is handled via your custom RBAC system.
- JWT/token handling will be integrated as needed during frontend integration or external API usage.

---

## ✍️ Author

**Amitesh Veeragattam**  
[LinkedIn](https://linkedin.com/in/your-profile)  
Backend Developer | Cybersecurity Enthusiast

---

## 📄 License

This project is licensed under the MIT License.
