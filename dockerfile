FROM python:3.12


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory
WORKDIR /app

# PYTHON REQUIREMENTS
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Project Code
COPY . /app/


