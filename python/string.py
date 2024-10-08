str = 'This Is a Fake String For My Test'

upper = str.upper()
print(upper)

lower = str.lower()
print(lower)

if 'Fake' in str:
    print('that\'s fake!')

if 'true' not in str:
    print('false')

slice = str[2:5]
print(slice)

split = str.split(" ")
print(split)

replace = str.replace("T", "L")
print(replace)