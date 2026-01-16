@echo off
echo ======================================
echo Starting FastAPI Backend
echo ======================================

REM Move to project directory (where this bat file exists)
cd C:\Data\Projects\Python\APIApp\backend

REM Activate virtual environment (if exists)
IF EXIST .venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
) ELSE (
    echo No virtual environment found. Skipping activation.
)

REM Start FastAPI using uvicorn
echo Starting server...
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
