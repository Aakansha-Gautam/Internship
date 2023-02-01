import psycopg2
import pandas as pd
import os
from zipfile import ZipFile
from os.path import basename

def access_file_api(id):
    connected=None
    cursor=None
    try:
        connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        cursor=connected.cursor()
        query=f'''with pivot as(SELECT
        max(CASE WHEN "Topic"= 'unique_id' THEN "Value" END) AS ui,
        max(CASE WHEN "Topic"= 'ingredients' THEN "Value" END) AS Ingredients,
        max(CASE WHEN "Topic"= 'id' THEN "Value" END) AS Id,
        max(CASE WHEN "Topic"= 'missedIngredientCount' THEN "Value" END) AS MissedIngredientCount,
        max(CASE WHEN "Topic" = 'type' THEN "Value" END) AS Type,
        max(CASE WHEN "Topic" = 'aisle' THEN "Value" END) AS Aisle,
        max(CASE WHEN "Topic" = 'usedIngridientCount' THEN "Value" END) AS UsedIngridientCount ,
        max(CASE WHEN "Topic" = 'title' THEN "Value" END) AS Title,
        max(CASE WHEN "Topic" = 'name' THEN "Value" END) AS Name,
        max(CASE WHEN "Topic" = 'unit' THEN "Value" END) AS Unit,
        max(CASE WHEN "Topic" = 'amount' THEN "Value" END) AS Amount
        FROM final_api
        group by substr("Index",1,3)) 
        select Ingredients,Id,MissedIngredientCount,MissedIngredientCount,Aisle,UsedIngridientCount,Title,Name,Unit,Amount from pivot where ui='{id}' '''
        cursor.execute(query)
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['Ingredients','Id','MissedIngredientCount','MissedIngredientCount','Aisle','UsedIngridientCount','Title','Name','Unit','Amount'])
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
        first_value=df.iloc[0].Ingredients


        for d in df['Ingredients']:
            i+=1
            if(first_value!=d):
                j+=1
                i=1
                first_value=d
            for a in range (1,c_l+1):
                indexing.append(str(j)+"."+str(i)+"."+str(a))
        folder=f"C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\api_files\\{id}_api"
        df2['Index']=pd.Series(indexing)
        df2.to_csv(os.path.join(folder,f'{id}_api_vertical.csv'),index=False)
        df.to_csv(os.path.join(folder,f'{id}_api.csv'))
        with ZipFile(f'{id}_api.zip', 'w') as zipObj:
            final=f"C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\api_files\\{id}_api"
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
