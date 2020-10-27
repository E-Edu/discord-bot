FROM python:3.9-alpine

COPY . /Discord/
WORKDIR /Discord/

RUN apk add --update libxml2-dev libxslt-dev gcc g++
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["bot.py"]