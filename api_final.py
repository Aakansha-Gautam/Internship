import requests
import private
import json 
import os 
from csv import writer
import pandas as pd
import numpy as np 
from sqlalchemy import create_engine


def getRecipeByIngredients(filename,id):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    with open(filename,'r')as file:
        for i in file.readlines():
            params = {'ingredients':f'{i}',
                    'apiKey':f'{private.key}'      
                    }
            response = requests.get(url,params=params)
            recipes = response.json()
            v_path=r'C:\Users\aakan\OneDrive\Desktop\flask\api_files'
            value_path=os.path.join(v_path,id+"_api")
            if not os.path.exists(value_path):
                    os.mkdir(value_path)
            # final=os.path.join(value_path,i)
            # if not os.path.exists(final):
            #         os.mkdir(final)
            with open(f'C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\recipes.json', 'a') as file:
                for recipe in recipes:
                    for item in recipe["missedIngredients"]:
                        data = {
                            'ingredients': i,
                            'id': recipe['id'],
                            'missedIngredientCount': recipe['missedIngredientCount'],
                            'type':'missed__ingredient',
                            'aisle':item["aisle"],
                            'usedIngridientCount':recipe['usedIngredientCount'],
                            'title': recipe['title'],
                            'name':item['name'],
                            'unit':item['unit'],
                            'amount':item["amount"],
                        }
                        json.dump(data, file)
                        file.write('\n')
                    
                    for item in recipe['usedIngredients']:
                        data = {
                            'ingredients': i,
                            'id': recipe['id'],
                            'missedIngredientCount': recipe['missedIngredientCount'],
                            'type':'used__ingredient',
                            'aisle':item["aisle"],
                            'usedIngridientCount':recipe['usedIngredientCount'],
                            'title': recipe['title'],
                            'name':item['name'],
                            'unit':item['unit'],
                            'amount':item["amount"],
                        }
                        json.dump(data, file)
                        file.write('\n')
                file.close()
                df = pd.read_json ('C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\recipes.json', lines=True)
                df=pd.DataFrame(df)
                df['unit'] = df['unit'].replace("", np.nan)
                df['unique_id']=id
                df.dropna(inplace=True)
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
                first_value=df.iloc[0].ingredients
                for d in df['ingredients']:
                    i+=1
                    if(first_value!=d):
                        j+=1
                        i=1
                        first_value=d
                    for a in range (1,c_l+1):
                        indexing.append(str(j)+"."+str(i)+"."+str(a))
                df2['Index']=pd.Series(indexing)
                engine = create_engine("postgresql+psycopg2://postgres:1223@localhost:5432/first")
                df2.to_sql(name='final_api',con=engine,index=False,if_exists='append')