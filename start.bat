@echo off
echo Checking for virtual environment...

:: 1. Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: 2. Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: 3. Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: 4. Check if the database exists
if not exist "db.sqlite3" (
    echo WARNING: db.sqlite3 not found. Please make sure you included it.
) else (
    echo Using provided db.sqlite3
)

:: 5. Run the Django development server
echo Starting Django development server...
python manage.py runserver

pause