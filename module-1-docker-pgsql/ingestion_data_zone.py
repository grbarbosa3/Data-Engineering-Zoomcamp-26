import pandas as pd
from time import time
from sqlalchemy import create_engine
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    engine = create_engine(f'postgresql+psycopg://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df_iter = pd.read_csv(
        url,
        iterator=True,
        chunksize=100000
    )

    df = next(df_iter)


    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

    while True:
        try:
            t_start = time()
            df = next(df_iter)

            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            t_end = time()
            print(f"Inserted another chunk..., took {t_end - t_start:.3f} seconds")

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='db for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='URL of the CSV file to ingest')

    args = parser.parse_args()

    main(args)







