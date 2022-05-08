FROM python:3.9

RUN mkdir /main

ADD main.py trial.py db.py /main/

WORKDIR /main
RUN pip install requests psycopg2

CMD ["python", "./main.py"]




