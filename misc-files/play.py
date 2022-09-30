#v = [
#				{'i': 101, 'n': 'Jane Doe', 'c': 'Malaysia'},
#				{'i': 102, 'n': 'John Dan', 'c': 'Malaysia'},
#				{'i': 103, 'n': 'Shab Ace', 'c': 'Malaysia'}
#]

# add new dict in list
# list_name.insert(index, new_item)
#v.insert(3,{'i': 104, 'n': 'Shazreen', 'c': 'Singapore'})

# change jane doe country to Brunei
#v[0]['c'] = 'Brunei'

# delete shaz because she's useless
#v.pop(3)

# maybe just delete all because i am sleepy
#del v

#for k in v:
#	print (k)

v = [
				{'ic':'1000', 'fn':'Luke Filewalker', 'c':'MY', 'hv':'0'},
				{'ic':'1001', 'fn':'Monte Zummar', 'c':'MY', 'hv':'0'}
]

for d in v:
    if 'fn' in d:
        print ('Luke Filewalker' in d['fn'])

#mylist= [{'powerpoint_color': 'blue', 'client_name': 'Sport Parents (Regrouped)'}, {'sort_order': 'ascending', 'chart_layout': '1', 'chart_type': 'bar'}]

#print ([d["sort_order"] for d in mylist if "sort_order" in d] == 'ascending')

#print ([d["fn"] for d in v if "fn" in d][0])

#for key in v:
#	if v[0]['ic'] == q:
#		print ("Same!")
#	else:
#		print ("Different!")