FROM alpine:latest

RUN apk add --no-cache python3

WORKDIR /app

COPY tuple_source.py script.py

CMD ["python3", "script.py"]