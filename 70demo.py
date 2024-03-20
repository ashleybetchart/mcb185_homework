# 70 demo by Ashley Betchart


# dictionary: list but w string instead of numeric indices. no append(for dict)
	# list[0] = 0 is numeric index
	# dict['hey'] = 'hey' is a string index
# empty dict created w empty brackets {} or dict () fctn

d = {}
d = dict()

#dict w predefined items, {key: value} pairs
d = {'cow': 'moo', 'pig': 'oink'}
print(d)

#access items using []. got error w 'moo'
print(d['cow'])

#add items to dict w new key:value pair. adds onto line 13
d['goat'] = 'baa'
print(d)

#change value of item by accessing it w its key. 
#will print line 13 +20. and line 13 w change to moove
d['cow'] = 'moove'
print(d)

#check if key exists, use "in"
if 'cow' in d: print(d['cow'])

#Iteration
	#for loop iterates over the keys in which they were created
	#to get specific element use key as an index to dict
	#(below) cow says moove, pig says oink
for key in d: print(f'{key} says {d[key]}')

	#most common way to iterate thru dict is dict.items(). says same as above
for k, v in d.items(): print(k, 'says', v)

	#if only want kwys or values, pythoon has dict.keys() and dict.values()
	#if you want them as lists, coerce them w list()
	#d.val()= dict_values[moove, oin, etc] while the list only returns ['moove', 'oink']
print(d.keys(), d.values(), list(d.values()))