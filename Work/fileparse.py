import csv

types = []
def parse_csv(filename, select=None):
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = []
        record =()
        records = []
        for row in rows:
            if not row:    
                continue
            
            if indices:
                row = ( row[index] for index in indices )

            if types:
                row = [func(val) for func, val in zip(types, row) ]
            
            record = ()
            records.append(record)

    return records
        
#parse = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types = [str,int])