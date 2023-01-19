import psycopg2
import pandas as pd
def unscraped():
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query='''select path from scrape_info where scraped=false'''
        cursor.execute(query)
        return(cursor.fetchone()[0].split('\\')[-1])

    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()