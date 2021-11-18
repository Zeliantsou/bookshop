FROM python:3.8

#ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

COPY . /code/

#RUN chmod +x ./entrypoint.sh

#ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]