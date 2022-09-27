from python:3.10-bullseye
workdir /app
copy requirements.txt .
run pip install -r requirements.txt
copy . .
cmd ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
expose 5000