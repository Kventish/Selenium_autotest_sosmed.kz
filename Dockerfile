FROM python:3.9

WORKDIR /app

# install gcc
# RUN apk add --no-cache gcc g++

USER root

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY requirements.txt .
RUN pip install -r requirements.txt
