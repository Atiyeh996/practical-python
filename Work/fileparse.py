import csv


def parse_csv(filename, select=None, types= None, delimiter=' '):
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows)
        

        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select 
        else:
            indices = []


        try: 
            records = []
            for row in rows:
                if not row:    
                    continue
            
                if select:
                    row = [row[index] for index in indices ]

                if types:
                    row = [func(val) for func, val in zip(types, row) ]
            
                if headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            
        except TypeError as e:
            raise RuntimeError("select argument requires column headers")

    return records
        
file = parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)