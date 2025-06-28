#!/bin/bash

# 1. Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# 3. Install required dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# 4. Check if SQLite database exists
if [ ! -f "db.sqlite3" ]; then
    echo "WARNING: db.sqlite3 not found. Please make sure you included it."
else
    echo "Using provided db.sqlite3"
fi

# 5. Start Django development server
echo "Starting Django development server..."
python manage.py runserver