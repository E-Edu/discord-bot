FROM python:3.7-alpine

COPY . /Discord/
WORKDIR /Discord/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["bot.py"]