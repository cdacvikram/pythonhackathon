From python:3.9
COPY requirements.txt .
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
CMD python -m main.py