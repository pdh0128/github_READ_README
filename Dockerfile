FROM python:3.11.7

WORKDIR /app
COPY app/ app/
COPY .env /app/.env
COPY templates/ templates/
COPY tools/ tools/
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
