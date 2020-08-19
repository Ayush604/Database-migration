## connection to Oracle

import cx_Oracle

dsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='ayush')
conn = cx_Oracle.connect(user=r'hr', password='Ayush1234', dsn=dsn_tns)
c = conn.cursor()
c.execute('select * from student1') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()
