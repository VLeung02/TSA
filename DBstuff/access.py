# PostgreSQL Python wrapper
import psycopg2 as sql

# Custom
from config import config
# from datacollect import Data   # This will collect and return the data

# Default modules
import random
import time


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        # print("Connecting to the PostgreSQL database...")
        conn = sql.connect(**params)

        # create a cursor
        cur = conn.cursor()



        # execute a statement
        # execute(cur)

        voltage = random.randint(1, 25)
        current = random.randint(1, 30)
        power = voltage * current
        battery_temperature = random.randint(0, 90)

        data = [voltage, current, power, battery_temperature]

        cur.execute('INSERT INTO tsa_data (voltage, current, power, battery_temperature) VALUES ({}, {}, {}, {})'.format(voltage, current, power, battery_temperature))
        
        print("Data inserted.")

        conn.commit()
        cur.close()

    except (Exception, sql.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed')




if __name__ == '__main__':
    while True:
        connect()
        time.sleep(10)
        



def generate_str_array(count, max, min): 
    return ",".join([str(random.randint(min, max)) for i in range(0, count)])

