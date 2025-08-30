FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY app/ ./app/

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 8000
# ENV MONGOURI="mongodb://localhost:27017"
ENTRYPOINT ["python", "-m", "app.main"]
