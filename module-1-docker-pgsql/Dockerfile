FROM python:3.14

RUN apt-get update && apt-get install -y wget
RUN pip install pandas sqlalchemy psycopg2-binary psycopg

WORKDIR /app

COPY ingestion_data_zone.py ingestion_data_zone.py

ENTRYPOINT ["python", "ingestion_data_zone.py"]
