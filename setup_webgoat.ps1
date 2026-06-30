# setup_webgoat.ps1 - Sets up flask-webgoat for Python 3 on Windows
$ErrorActionPreference = "Stop"
Write-Host "=== flask-webgoat setup ===" -ForegroundColor Cyan
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install "Flask>=2.0,<3.0" "Werkzeug>=2.0,<3.0" "Jinja2>=3.0" "itsdangerous>=2.0" "click>=8.0"
pip install pytest pytest-flask
Write-Host "=== Setup complete ===" -ForegroundColor Green
Write-Host "Run app:   .\.venv\Scripts\Activate.ps1 ; python run.py"
Write-Host "Run tests: .\.venv\Scripts\Activate.ps1 ; pytest tests\ -v"
