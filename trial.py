import psycopg2
from db import dbd


def data_model(data):
    conn = None
    cur = None
    try:
        conn = dbd()
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute('SELECT %s as connected;', ('connection to post was success',))
        print(cur.fetchone())
        if cur.execute('DROP TABLE IF EXISTS Brewery'):
            print("Table already exists")
        else:
            cur.execute(
                """CREATE TABLE Brewery(
                    ID_db SERIAL NOT NULL,
                    id VARCHAR(128), 
                    name VARCHAR(128), 
                    brewery_type VARCHAR(128), 
                    street VARCHAR(128), 
                    address_2 VARCHAR(128), 
                    address_3 VARCHAR(128), 
                    city VARCHAR(128), 
                    state VARCHAR(128), 
                    county_province VARCHAR(128), 
                    postal_code VARCHAR(128), 
                    website_url VARCHAR(128), 
                    phone VARCHAR(128), 
                    country VARCHAR(128), 
                    longitude VARCHAR(128), 
                    latitude VARCHAR(128),
                    tags VARCHAR(128), 
                    ratings DECIMAL, 
                    number_of_ratings VARCHAR(128))"""
            )
            # converting list of dict to list of turple

            data_tuples = [tuple(datum.values()) for datum in data]
            values_template = ','.join(['%s'] * len(data_tuples))

            cur.execute("INSERT INTO Brewery(id, name, brewery_type, street, address_2, " \
                        "address_3, city, state, county_province, postal_code, website_url, phone, country, " \
                        "longitude, latitude, tags, ratings, number_of_ratings) VALUES {}".format(values_template),
                        data_tuples)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
