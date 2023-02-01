
import psycopg2
import pandas as pd
def create_db_api(final_path):
    connected=None
    cursor=None
    try:
        location=final_path
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        create='''create table if not exists api_info (id Serial Primary Key, time timestamp,path text,extracted boolean);'''
        cursor.execute(create)
        connected.commit()
        print("table created")
        insert=f'''insert into api_info(time,path,extracted) values(current_timestamp,'{location}',false)'''
        cursor.execute(insert)
        connected.commit()
        print("value inserted")

    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()
