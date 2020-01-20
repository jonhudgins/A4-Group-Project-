# Data cleaning for bar-chart1, "Conservative Media Stories Associate Socialism with Democrats at 
# Seven Times the Rate of Progressive Media Stories" (analysis page)

# NOTE:  This converter was run with the input csv and output json files in the same folder.
# I have since moved them.  As a result, the code won't run unless the filepath for the 
# input is changed. If you want to test that, the csvs are in data/original-csvs

# import relevent libraries and packages

from pprint import pprint
from datetime import datetime
import csv
import json
import pandas as pd

#open csv  and convert it to a list of dictionaries saved to the variable stories

with open('socialist_democrat_15-words_all-conservative-progressive_19.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	stories = [dict(row) for row in rows]	

# created a data model that matches the required input, broken out by quarter

Q1dic = {'categorie': 'Q1',  'values': [{"value": 0, "rate": "Progressive"}, {"value": 0, "rate": "Conservative"}]}
Q2dic = {'categorie': 'Q2',  'values': [{"value": 0, "rate": "Progressive"}, {"value": 0, "rate": "Conservative"}]}
Q3dic = {'categorie': 'Q3',  'values': [{"value": 0, "rate": "Progressive"}, {"value": 0, "rate": "Conservative"}]}
Q4dic = {'categorie': 'Q4',  'values': [{"value": 0, "rate": "Progressive"}, {"value": 0, "rate": "Conservative"}]}

# loop through stories

for story in stories:
	
	# return the quarter of the date using datetime and pandas
	dateOld = story["date"]
	parsed_date = datetime.strptime(dateOld, "%Y-%m-%d")
	quarter = pd.Timestamp(parsed_date).quarter

	# identify the quarter value and loop through the data model defined above, adding the number of 
	# conservative and progressive stories to get a total for each quarter in the dicts defined above
	# use debugging print statements

	if quarter == 1:

		for val in Q1dic["values"]:
			if val["rate"] == "Progressive":
				val["value"] += int(story["Progressive-count"])
			elif val["rate"] == "Conservative":
				val["value"] += int(story["Conservative-count"])
			else:
				print("error in Q1dic for loop")

	elif quarter == 2:

		for val in Q2dic["values"]:
			if val["rate"] == "Progressive":
				val["value"] += int(story["Progressive-count"])
			elif val["rate"] == "Conservative":
				val["value"] += int(story["Conservative-count"])
			else:
				print("error in Q2dic for loop")

	elif quarter == 3:

		for val in Q3dic["values"]:
			if val["rate"] == "Progressive":
				val["value"] += int(story["Progressive-count"])
			elif val["rate"] == "Conservative":
				val["value"] += int(story["Conservative-count"])
			else:
				print("error in Q3dic for loop")

	elif quarter == 4:

		for val in Q4dic["values"]:
			if val["rate"] == "Progressive":
				val["value"] += int(story["Progressive-count"])
			elif val["rate"] == "Conservative":
				val["value"] += int(story["Conservative-count"])
			else:
				print("error in Q4dic for loop")

	else:
		print("error in else!") 
		break

# add the dicts made for each quarter to a list, stories_by_quarter

stories_by_quarter = [Q1dic, Q2dic, Q3dic, Q4dic]


# write stories_by_quarter to a json file

with open('clean_socialist_democrat_15-words_all-conservative-progressive_19.json', 'w') as f:
    json.dump(stories_by_quarter, f, indent = 4)



