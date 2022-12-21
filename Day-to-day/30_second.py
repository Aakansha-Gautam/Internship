# 30 th november Merge, Group_by,concat,joinn
# Json to dataframe"

# to covert json file to dataframe we have to make use of:
# json_normalize()
# read_json()
# DataFrame.from_dict()

dict=json.loads(data)
df=json_normalize(dict['rechnologies'])

