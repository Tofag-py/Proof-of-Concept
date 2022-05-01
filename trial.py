import os
import psycopg2
import main

DB_HOST = "ec2-34-247-72-29.eu-west-1.compute.amazonaws.com"
DB_NAME = "dad1sf5fvfqo64"
DB_USER = "cdxpreinbalvbw"
DB_PASS = "8b794319be9f1d93f7067a2544843ef4a466b4f9e1c0461f13185d43be2f9550"

# DATABASE_URL = os.environ['postgres://pglpycxcttzwwv:846f5e5b4a51c20a95c81115b2eb5fc739429f2f3b10326e2a84fb28661d1da0@ec2-63-32-248-14.eu-west-1.compute.amazonaws.com:5432/d9fvhj9uj2modd']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn = None
cur = None
try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS Proof_of_Concept (
        ID text PRIMARY KEY, 
        Name VARCHAR, 
        brewery_type VARCHAR, 
        street VARCHAR, 
        address_2 VARCHAR, 
        address_3 VARCHAR, 
        city VARCHAR, 
        state VARCHAR, 
        county_province VARCHAR, 
        postal_code VARCHAR, 
        website_url VARCHAR, 
        phone INT, 
        country VARCHAR, 
        longitude decimal, 
        latitude decimal,
        tags VARCHAR, 
        ratings DECIMAL, 
        number_of_ratings INT);"""
    )

    conn.commit()

    myDict = main.r

    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in myDict.values())
    cur.execute("INSERT INTO %s ( %s ) values (%s);" % ('Proof_of_Concept', values))


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()