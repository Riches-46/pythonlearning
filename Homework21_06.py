#create a list
names = ['richie','summer','rachel','richard']
ages = ['9','11','46','47']

#adds a name to the end of list
names.append('bob')
#prints name in spot 3
print(names[3])
#finds names in the first two positions
print(names[:2])
#finds a name in list
print('richie'in names)
#concantinates the two list
print(names + ages)
#extends one list to another
ages.extend(names)
#turns a list into a tuple
ages = tuple(ages)

#creates a dictionary
richdict = {'name': 'nick','age': '16','address': '6 turnout lane',
            'phone numbe': '0851111111'}
#prints a value from the dictionary
print(richdict['age'])
#prints key value names
print(richdict.keys())
#prints out value in dictionary
print(f"the address of nick is {richdict['address']}")