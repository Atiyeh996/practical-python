import csv

def parse_csv(filename):
    with open (filename , "rt") as f:
        rows = csv.reader(f)

        headers = next(f)
        records=[]
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers,row))
            records.append(record)
    return records

records = parse_csv("Data/portfolio.csv")
print(records)