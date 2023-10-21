FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# COPY create_examples.py .

# RUN python create_examples.py

EXPOSE 8000

CMD ["python", "main.py"]