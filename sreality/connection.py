import psycopg2


def connect():
    hostname = 'db-scrapy'
    username = 'postgres'
    password = '12345' 
    database = 'postgres'
 
    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

    cur = connection.cursor()
        
    cur.execute("""SELECT * from flats""")

    items = cur.fetchall()

    cur.close()

    #print(items)
    return items



