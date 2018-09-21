#reading of the bumping file and storing in the list of list
import csv
store_list=[]
soa_list=[]
plato_list=[]
specs_list=[]
Headerfile = open('C:/Users/arnab.jaydeb.basak/Documents/store recovery automation/bumpKeyField-Fix-0835012317.csv','r')
for row in csv.reader(Headerfile):
    if row[0] == 'Plato':
        plato_list.append(row)
    elif row[0] == 'Store':
        store_list.append(row)
    elif row[0] == 'SOA':
        soa_list.append(row)
    else:
        specs_list.append(row)

Headerfile.close()
print("Printing store values\n")
print('Total missing values in the store database ',len(store_list))
print(store_list)
print()
store_flattendlist = [y for x in store_list for y in x]
print(store_flattendlist)
store_set = set(store_flattendlist)
print()
print(store_set)




