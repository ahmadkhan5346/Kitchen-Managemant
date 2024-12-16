# Base Image
FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /kitchen

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run the application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]