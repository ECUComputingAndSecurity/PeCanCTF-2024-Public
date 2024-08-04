FROM alpine:3.20.1

RUN apk add --no-cache python3=3.12.3-r1 py3-pip=24.0-r2 bash=5.2.26-r0

COPY ./src/ /app

WORKDIR /app

RUN pip3 install --no-cache-dir --break-system-packages pyjwt==2.4.0 Flask==2.0.1 Jinja2==3.0.1 Werkzeug==2.3.8 cryptography==43.0.0

RUN addgroup -S morty && adduser -S morty -G morty

RUN chown -R morty:morty /app

USER morty

ENV FLASK_APP=app.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "-p", "8000"]

EXPOSE 8000
