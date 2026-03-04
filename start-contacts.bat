@echo off
cd /d "%~dp0"
echo Starting Contacts Database...
start /B python app.py
timeout /t 2 /nobreak >nul
start http://localhost:5000
