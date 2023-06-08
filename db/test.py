from conn import psql
#import pdb; pdb.set_trace()

sql = "select 1"

row_list = psql(sql)
for i in range(len(row_list)):
    r = str(row_list[i])
    print(r)

