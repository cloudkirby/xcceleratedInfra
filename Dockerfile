# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your local script (and requirements if any) into the container
COPY main .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Command to run your script when the container starts
CMD ["python", "main.py"]