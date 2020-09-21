FROM python:3.8

WORKDIR /code

# Avoid copying in Dockerfile and egg-info and ..
COPY fanpi /code/fanpi
COPY setup.py /code/
COPY MANIFEST.in /code
COPY README.md /code

RUN pip install -e .

ENV FLASK_APP fanpi
CMD flask run
