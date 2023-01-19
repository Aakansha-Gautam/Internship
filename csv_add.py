import psycopg2
import pandas as pd
def csv_add(csv_name,id):
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query0='''select path from scrape_info order by id limit 1'''
        print(query0)
        cursor.execute(query0)
        query=f'''update scrape_info set scraped=true,csv_file='{csv_name}.csv' where id={id}'''
        cursor.execute(query)
        connected.commit()

    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()