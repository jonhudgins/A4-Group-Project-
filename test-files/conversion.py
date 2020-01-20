from pprint import pprint
from datetime import datetime
import csv

#open csv  and convert it to a list of dictionaries saved to the variable df

with open('all_center-conservative-progressiv-stories_2019.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	stories = [dict(row) for row in rows]


# write the the needed key values to rows in a new csv with parsed dates to match 
# the needed csv format

with open('clean_all_center-conservative-progressiv-stories_2019.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['date', 'progressive', 'conservative'])
	for story in stories:
		progressive = story["Progressive-count"]
		conservative = story["Conservative-count"]
		dateOld = story["date"]
		parsed_date = datetime.strptime(dateOld, "%Y-%m-%d")
		date_output = parsed_date.strftime("%y-%b-%d")
		writer.writerow([date_output, progressive, conservative])

