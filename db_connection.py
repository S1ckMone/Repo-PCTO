import psycopg2 as pg

conn = pg.connect(
    host="db-gruppo-5.cykdo1jweq0j.us-east-1.rds.amazonaws.com",
    database="lavoropcto",
    user="postgres",
    password="Sim$pri24db")

def json_deconstructer(data):
    s=1
cursor = conn.cursor()
query = "INSERT INTO sensor_values values("
cursor.execute(query)
record = cursor.fetchall()

for row in record:
    print("Riga =", row)