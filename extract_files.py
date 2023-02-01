import psycopg2
import pandas as pd
def files_extract():
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query='''select id,path from api_info where extracted=true order by id '''
        cursor.execute(query)
        full_path=[]
        data=cursor.fetchall()
        for j in data:
            full_path.append((j[0],j[1]))
        return(full_path)
    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()
