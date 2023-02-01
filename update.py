import psycopg2
import pandas as pd
def update_val(id):
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query=f'''update api_info set extracted=true where id={id} '''
        cursor.execute(query)
        connected.commit()

    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()