From python:3.9
COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt
CMD python ./src/main.py