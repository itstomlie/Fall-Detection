# app/Dockerfile

# Use Python 3.11.4 as base image
FROM python:3.11.4-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY rtsp.py .

# Run the application
CMD ["python", "rtsp.py"]
