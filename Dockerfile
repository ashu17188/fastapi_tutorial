FROM python:3.9

LABEL  maintainer "Ashutosh Shukla <ashu17188@gmail.com>"

WORKDIR /app
COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install

CMD ["python","app.py"]