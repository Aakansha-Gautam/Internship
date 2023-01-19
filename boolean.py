import psycopg2
import pandas as pd
def boolean():
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query='''select Path,Id from scrape_info where scraped=false order by id limit 1'''
        cursor.execute(query)
        return(cursor.fetchone())

    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()