import psycopg2
import pandas as pd
import os
from zipfile import ZipFile
from os.path import basename

def access_file_daraz(id):
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query=f'''with pivot as(SELECT
        max(CASE WHEN "Topic"= 'Id' THEN "Value" END) AS scrape_id,
        max(CASE WHEN "Topic"= 'Search_Query' THEN "Value" END) AS search_topic,
        max(CASE WHEN "Topic"= 'Title' THEN "Value" END) AS title,
        max(CASE WHEN "Topic" = 'Description' THEN "Value" END) AS price,
        max(CASE WHEN "Topic" = 'Link' THEN "Value" END) AS link
        FROM final_daraz
        group by substr("Index",1,3)) 
        select search_topic,title,price,link from pivot where scrape_id='{id}' '''
        cursor.execute(query)
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['Search_query','Title','Price','Link'])
        df2 = df.stack().reset_index()
        df2= df2.rename(columns={'level_0': 'Index','level_1':'Topic', 0: 'Value'})
        column_length=df.columns[:]
        c_l=len(column_length)
        df2.drop(df2.loc[df2['Topic']=="index"].index, inplace=True)
        loc_index=0
        i=0
        j=1
        k=1
        indexing=[]
        first_value=df.iloc[0].Search_query
        for d in df['Search_query']:
            i+=1
            if(first_value!=d):
                j+=1
                i=1
                first_value=d
            for a in range (1,c_l+1):
                indexing.append(str(j)+"."+str(i)+"."+str(a))
        folder=f"C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\files\\{id}_daraz"
        df2['Index']=pd.Series(indexing)
        df2.to_csv(os.path.join(folder,f'{id}_daraz_vertical.csv'),index=False)
        df.to_csv(os.path.join(folder,f'{id}_daraz.csv'))
        with ZipFile(f'{id}_daraz.zip', 'w') as zipObj:
            final=f"C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\files\\{id}_daraz"
            for folderName, subfolders, filenames in os.walk(final):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, basename(filePath))
    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if connected is not None:
            connected.close()
        if cursor is not None:
            cursor.close()