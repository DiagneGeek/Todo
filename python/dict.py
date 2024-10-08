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


if "name" in dict:
    print("yes, bamba is in dict")

if dict['age'] < 18:
    print(f"you cannot getting a card because you are {dict['age']} ")

if not ("react" in dict["skills"] and  "vue" in dict['skills']):
    print('you are not ready')


for skill in dict["skills"]:
    if skill == "Python":
        print("you are hired")