FROM python:3.12-slim

RUN mkdir /app
COPY . /app
WORKDIR /app

CMD ["bash"]
