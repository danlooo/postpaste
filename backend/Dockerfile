FROM python:3.8.13-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./* ./
EXPOSE 80
CMD sh main.sh