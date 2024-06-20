@echo off

rem Create a virtual environment
python -m venv venv

rem Activate the virtual environment
venv\Scripts\activate

rem Install dependencies
pip install -r requirements.txt
