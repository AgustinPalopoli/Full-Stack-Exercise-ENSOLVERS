# 🗒️ Lime Notes – Personal Note Manager

**Lime Notes** is a Django-based web application that allows users to manage personal notes with features such as archiving, categorization, and filtering.

---

## ✅ Features

### 📌 Phase 1 – Notes Management
- Users can create, edit, and delete notes.
- Users can archive and unarchive notes.
- Users can list their **active notes**.
- Users can list their **archived notes**.

### 🗂️ Phase 2 – Categories
- Users can add or remove one or more categories to/from notes.
- Users can filter notes by category.

---

## 🚀 Quick Start – Linux/macOS

To launch the app with one command:

```bash
./start.sh
````

This script will:

* Create and activate a virtual environment (if not present)
* Install dependencies from `requirements.txt`
* Use the included `db.sqlite3` file as the database
* Start the Django development server

> ✅ Requirements: Python 3 and Bash installed

---

## 🪟 Quick Start – Windows

Run the app by opening the terminal or Command Prompt and typing:

```bat
start.bat
```

This script will:

* Create and activate a virtual environment (if not present)
* Install dependencies from `requirements.txt`
* Use the included `db.sqlite3` file
* Launch the Django server

> ✅ Works with CMD or the integrated terminal in Visual Studio Code

---

## ⚙️ Tech Stack

* **Backend**: Python 3, Django 4
* **Architecture**: Layered pattern – Views → Services → Repositories
* **Database**: SQLite (via Django ORM)
* **Frontend**: HTML, CSS (Bootstrap), Javascript

---

## 📁 Project Structure

```
LimeNotes/
├── backend/               # Main Django app (views, models, services, repositories)
├── frontend/              # Static assets and HTML templates
├── db.sqlite3             # Pre-built SQLite database
├── requirements.txt       # Project dependencies
├── start.sh               # Startup script for Linux/macOS
├── start.bat              # Startup script for Windows
└── manage.py              # Django management script
```

---

## 🔐 Authentication

* Registration and login are required to access notes.
* Each user can only see and manage their own notes.
* A logout option is available from the UI.
* Default user:
  * User: user1
  * Password: Password1#

---

## 🗃️ Data Persistence

* The application uses a **relational SQLite database**.
* Data is stored via **Django’s ORM** (Object Relational Mapping).
* No in-memory storage or mock data is used.

---

## 📌 Setup Notes

* Ensure you have Python 3 installed.
* Use the appropriate script for your operating system.
* Do **not delete** the `db.sqlite3` file, as it contains the required schema and initial data.

---

## 👤 Author

Developed by **Agustin Palopoli**
I’d love to hear any suggestions you may have for improving this project.

---