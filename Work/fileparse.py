import csv

def parse_csv(filename, select = None, types=None):
    with open (filename , "rt") as f:
        rows = csv.reader(f)

        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records=[]

        
        for row in rows:
            if types:
                row = [func(val) for func, val in zip(types, row) ]
            if not row:
                continue
            if indices:
                row = [ row[index] for index in indices ]

            record = dict(zip(headers,row))
            records.append(record)
    return records

