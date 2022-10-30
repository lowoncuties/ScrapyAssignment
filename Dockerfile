FROM python:3.8-alpine
WORKDIR /sreality
COPY . .
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install -r sreality/requirements.txt --no-cache-dir
ENV FLASK_APP=/sreality/sreality/app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["flask", "run"]