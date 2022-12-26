import requests
import private
import json 

def getRecipeByIngredients(ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"

    params = {'ingredients':f'{ingredients}',
            'apiKey':f'{private.key}'      
            }
    response = requests.get(url,params=params)
    recipes = response.json()
    with open('C:\\Users\\aakan\\OneDrive\\Desktop\\In\\api\\recipes.json', 'a') as file:
        for recipe in recipes:
            for item in recipe["missedIngredients"]:
                data = {
                    'ingredients': ingredients,
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
                    'ingredients': ingredients,
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
ingredients = input("Enter the ingredients of your choice: ")
getRecipeByIngredients(ingredients)
