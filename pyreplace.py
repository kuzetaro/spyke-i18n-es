import json

with open('recursos\splat3_USes.json') as first_file:
    first_json = json.load(first_file)
    
with open('file.json', encoding='utf-8') as second_file:
    second_json = json.load(second_file)    

new_data = []

"""
print(type(second_json['game_lang']['brand']))
for i in second_json['game_lang']['brand'].keys():
    print(first_json[i])
    second_json['game_lang']['brand'].update({i:first_json[i]})

print(second_json['game_lang']['brands'].keys())

falta sub y special

shoes
skill
main
stage
stat
weapon_class
"""
for j in second_json['game_lang']['special'].keys():
    print(j)
    try:
        print("cambiar")
        second_json['game_lang']['special'].update({j:first_json['special'][j]})
    except:
        pass

with open('file.json', 'w') as file:
     file.write(json.dumps(second_json))
