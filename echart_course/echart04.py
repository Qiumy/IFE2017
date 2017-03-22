import csv
import json

# 读csv文件
def read_csv(file, ticker=None):
	if ticker==None:
		csv_rows = []
		with open(file) as csvfile:
			reader = csv.DictReader(csvfile)
			title = reader.fieldnames
			for row in reader:
				csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
			return csv_rows
	else:
		csv_rows = []
		with open(file) as csvfile:
			reader = csv.DictReader(csvfile)
			title = reader.fieldnames
			for row in reader:
				if row['Ticker']==ticker:
					csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
				else:
					continue
			return csv_rows

# 写json文件
def write_json(data, json_file, format=None):
    with open(json_file, "w") as f:
        if format == "good":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False))
        else:
            f.write(json.dumps(data))

write_json(read_csv(r'E:\githubCode\ife2017\echart_course\data\sp500hst.txt',"PBG"), 'PBG.json', 'good')





