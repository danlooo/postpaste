FROM python:3.8.13-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
  libpq-dev \
  python-dev \
  build-essential

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./* ./
EXPOSE 80
CMD sh main.sh