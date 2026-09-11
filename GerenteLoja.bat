@echo off
cd /d "%~dp0"
where python >nul 2>nul
if not errorlevel 1 (
    python main.py
) else (
    py main.py
)
if errorlevel 1 (
    echo.
    echo O programa foi encerrado com erro.
)
pause
