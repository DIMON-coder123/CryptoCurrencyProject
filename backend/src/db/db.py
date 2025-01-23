from configparser import ConfigParser

import psycopg2 as pg

def load_config(filename='/home/dmytro/repo/CryptoCurrencyProject/backend/database.ini', section='postgresql') -> dict:
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to postgresql
    configuration: dict = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configuration[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return configuration

def connection():
    try:
        config: dict = load_config()
        conn = pg.connect(host=config["host"],
                        dbname=config["database"],
                        user=config["user"],
                        password=config["password"],
                        port = 5432)
    except (Exception, pg.DatabaseError) as error:
        raise error
    return conn

def run_sql(sql_query: str) -> None:
    conn = connection()
    with conn.cursor() as cursor:
        cursor.execute(sql_query)


def main():
    conn = connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id uuid DEFAULT gen_random_uuid(),
        name VARCHAR(255),
        surname VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(50)
    );""")
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()