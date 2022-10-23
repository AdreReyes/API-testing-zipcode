#format of csv 
#column 1 name,column 2 name, column 3 name
#first row data 1,first row data 2,first row data 3

# Python program to read json file and output to csv

import json
import pandas

#Function that reads the JSON file as python dictionary
def read_json(filename: str) -> dict:

	try:
		with open(filename, "r") as f:
			data = json.loads(f.read())
	except:
		raise Exception(f"Reading {filename} file encountered an error")

	return data


#Function that passes the python dictionary to json.dumps() function returns a string
def write_json(filename: str, jsondict: dict): 

	try:
		with open(filename, "w") as f:
			f.write(json.dumps(jsondict))
	except:
		raise Exception(f"writing {filename} file encountered an error")

    
#Function that uses pandas to manipulate the data 
def create_dataframe(data: list) -> pandas.DataFrame:

	# Declares an empty dataframe to append records
	dataframe = pandas.DataFrame()

	# Looping through each record
	for d in data:
		
		# Normalizes the column levels
		record = pandas.json_normalize(d)
		
		# Appends it to the dataframe
		dataframe = dataframe.append(record, ignore_index=True)

	return dataframe


def main():
	jsondict = read_json("test.json")
	
#if the key "places" appears in dictionary then remove it
	if "places" in jsondict:
		jsondict.update(jsondict["places"][0])
		jsondict.pop("places")
		
#For the values that are not in square brackets, append the dictionary and remove any format like this: [jsondict[item]]
	notlist = []
	for data in jsondict:
		if not isinstance(jsondict[data], list):
			notlist.append(data)

	for item in notlist:
		templist = [jsondict[item]]
		jsondict.pop(item)
		jsondict[item] = templist

#Make these changes in the JSON file
	write_json("test.json", jsondict)
#Read the JSON file as python dictionary and manipulate data
	dataframe = pandas.read_json("test.json")
#Convert dataframe to CSV
	dataframe.to_csv("zipinfo.csv", index=False)

if __name__ == '__main__':
	main()
