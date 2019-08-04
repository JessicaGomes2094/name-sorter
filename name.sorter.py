# Projects
name-sorter
# Program to sort alphabetically last names, then by any given names the person may have from list provided and print to file 'sorted-names.txt'
import os
import string
path = str(os.getcwd()+'/')
 
 
def getData(filename):

	read = open(path+filename, 'r+').readlines()

	data = [row.replace('\n','') for row in read]



	return data



	

def sortData(list_data):
    
	list_data.sort(key=lambda x: x.split()[-1]) 3Sort by last element in list

 	##list_data.sort(key=lambda x: x.split[1])
 	##list_data.sort(key = lambda x:x.split[0])


	return list_data



def saveValue(sort_value):

	if sort_value :

		with open('sorted-names-list.txt', 'w') as f:

			for item in sort_value:

				f.write("%s\n" % item)

		message = 'List Of Sorted Names Has Been Saved!'

	else:

		message = 'List Of Names Could Not Be Saved.'



	return message

# Get List of Data Values and Print Unsorted Names

list_data = getData('unsorted-names-list.txt')

print('Unsorted Names : ', list_data, '\n')



# Sort Data Values and Print Sorted Names

sort_value = sortData(list_data)

print('Sorted Names : ', sort_value, '\n')



# Save List Of Data Values

save_data = saveValue(sort_value)

print(save_data) 