import psycopg2


def dbd():
    DB_HOST = "ec2-34-247-72-29.eu-west-1.compute.amazonaws.com"
    DB_NAME = "dad1sf5fvfqo64"
    DB_USER = "cdxpreinbalvbw"
    DB_PASS = "8b794319be9f1d93f7067a2544843ef4a466b4f9e1c0461f13185d43be2f9550"
    DB_PORT = "5432"

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT,
                            sslmode='require')
    return conn


connection = dbd()


def test():
    cur = connection.cursor()
    cur.execute('SELECT %s as connected;', ('connection to post was success',))
    print(cur.fetchone())

    cur.close()
    connection.close()


test()
