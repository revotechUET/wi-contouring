FROM python:3.7.3-slim

MAINTAINER DoDang "dodv212@gmail.com"

WORKDIR /app

RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    python3-dev

COPY . /app

RUN pip install --upgrade pip --no-cache-dir \
    &&python -m pip install --no-cache-dir -r requirements.txt \
    && rm -f requirements.txt \
    && apt-get remove -y gcc python3-dev curl \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

CMD ["gunicorn", "--bind=0.0.0.0:5000", "wsgi:app"]
