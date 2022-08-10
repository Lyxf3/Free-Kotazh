FROM python:3.8

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip wheel

COPY requirements.txt .

RUN apt-get update && apt-get install -y libwebp-dev g++ gcc gettext 
RUN apt install gettext -y
RUN pip install -r requirements.txt --no-cache-dir

COPY entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]