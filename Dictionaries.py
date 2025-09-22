#Unordered mappings for storing objects, uses key value pair so that you just have to call the key
#easier for calling specific things without needing to know the exact index, but you cannot sort them

my_dict = {'key1':'value1','key2':'value2'}     #Dictionary creation is denoted by the curly braces "{}"

print(my_dict['key1'])
#value1

prices_lookup = {'apple':2.99, 'oranges':1.99,'milk':5.80}
print(prices_lookup['apple'])
#2.99

d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}    #Dictionaries can also have lists or other dictionaries nested inside

print(d['k2'])
#[0, 1, 2]

print(d['k3'])
#{'insideKey': 100}

print(d['k3']['insideKey'])
#100

d = {'key1': ['a','b','c']}

print(d['key1'][2].upper())
#C

d = {'k1': 100, 'k2': 200}
print(d)
#{'k1': 100, 'k2': 200}

d['k3'] = d['k1'] + d['k2']
print(d)
#{'k1': 100, 'k2': 200, 'k3': 300}

print(d.keys())
print(d.values())
print(d.items())

#dict_keys(['k1', 'k2', 'k3'])
#dict_values([100, 200, 300])
#dict_items([('k1', 100), ('k2', 200), ('k3', 300)])