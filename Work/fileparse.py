import csv

def parse_csv(filename, select = None, types=None, has_headers=True):
    with open (filename , "rt") as f:
        rows = csv.reader(f)

        headers = next(rows) if has_headers else []
        
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
    
    
        records=[]

        
        for row in rows:
            if types:
                row = [func(val) for func, val in zip(types, row) ]
            if not row:
                continue
            
            if select:
                row = [ row[index] for index in indices ]

            record = tuple(row)
            records.append(record)

    return records

