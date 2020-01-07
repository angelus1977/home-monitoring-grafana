FROM python:3.7-alpine

LABEL maintainer="cpu" \
      description="python for weather forecast"

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "-u", "forecast2.py"]
