dict = {
"name": "bamba",
"age": 15,
"senegalese": True,
"work": "developer",
"skills": ["html","css","js","Python"]
}

print(dict['name'])

print(len(dict))

print(dict.values())

print(dict.keys())

print (type(dict.keys()))

dict['age'] = 16
print(dict)

dict["skills"].append('github')
print(dict["skills"])