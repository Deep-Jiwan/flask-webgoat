#!/usr/bin/env bash
# setup_webgoat.sh - Sets up flask-webgoat for Python 3 on Linux/macOS
set -e

echo "=== flask-webgoat setup ==="
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install "Flask>=2.0,<3.0" "Werkzeug>=2.0,<3.0" "Jinja2>=3.0" "itsdangerous>=2.0" "click>=8.0"
pip install pytest pytest-flask
echo ""
echo "=== Setup complete ==="
echo "Run app:   source .venv/bin/activate && python run.py"
echo "Run tests: source .venv/bin/activate && pytest tests/ -v"
