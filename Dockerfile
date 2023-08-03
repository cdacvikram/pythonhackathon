From python:3.9
WORKDIR /app
COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt
CMD python ./src/main.py