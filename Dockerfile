FROM python:3.10

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["uvicorn", "weatherapi.app:app"]
