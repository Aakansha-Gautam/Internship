
import psycopg2
import pandas as pd
def create_db(final_path):
    connected=None
    cursor=None
    try:
        location=final_path
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        create='''create table if not exists scrape_info (id Serial Primary Key, time timestamp,platform varchar(20),path text,scraped Boolean,csv_file text default null);'''
        cursor.execute(create)
        connected.commit()
        print("table created")
        insert=f'''insert into scrape_info(time,platform,path,scraped) values(current_timestamp,'google','{location}',false)'''
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