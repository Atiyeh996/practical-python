import csv

def parse_csv(filename, select = None,types=None, has_headers=False, delimiter=','):
    with open (filename , "rt") as f:
        rows = csv.reader(f,delimiter=delimiter)

        headers = next(rows) if has_headers else []
        
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
    
    
        records=[]
        try:
        
            for row in rows:
                
                if not row:
                    continue
            
                if select:
                    row = [ row[index] for index in indices ]
                if headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
    
                    records.append(record)
                if types:
                    row = [func(val) for func,val in zip(types,row)]

        except ValueError as e:
            print(f"{row}:cant be converted, since {e} " )
           
    return records

portfolio = parse_csv('Data/missing.csv', types=[str, int, float])