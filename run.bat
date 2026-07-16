@echo off
echo ============================
echo 1. Export Employee CSV
echo 2. Export Student CSV
echo ============================

set /p choice=Enter your choice:

if %choice%==1 (
    python csv_export.py
)

if %choice%==2 (
    python student_csv_export.py
)

pause