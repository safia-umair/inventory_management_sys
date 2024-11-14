# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_sys

# copy all files to inventory_management_sys directory
COPY . /inventory_management_system/

RUN pip install poetry

RUN poetry install

# command to run on container start
CMD ["poetry", "run", "python", "inventory_management_sys/main.py"]