## dumping table from one databse to another

import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine
clientDsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='ayush')
clientConnectionString = cx_Oracle.connect(user=r'hr', password='Ayush1234', dsn=clientDsn_tns)
cstr = 'oracle://{user}:{password}@{sid}'.format(
	user='hr',
	password='Ayush1234',
	sid='ayush'
)
clientEngine =  create_engine(
	cstr,
	convert_unicode=False,
	pool_recycle=10,
	pool_size=50,
	echo=True
)

client = clientConnectionString.cursor()
hostDsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='tyagi604')
hostConnectionString = cx_Oracle.connect(user=r'hr', password='Ayush1234', dsn=hostDsn_tns)
cstr = 'oracle://{user}:{password}@{sid}'.format(
	user='hr',
	password='Ayush1234',
	sid='tyagi604'
)
hostEngine =  create_engine(
	cstr,
	convert_unicode=False,
	pool_recycle=10,
	pool_size=50,
	echo=True
)
host= hostConnectionString.cursor()
def migrator(clientCursor,hostCursor, clientTable,clientEngine,hostEngine):
	query='select * from '+clientTable
	clientCursor.execute(query)
	table=clientCursor.fetchall()
	hostTable = pd.DataFrame(table)
	query = 'select table_name, column_name, data_type from all_tab_columns where table_name='
	clientTable = clientTable.upper()
	query = query + "'" + clientTable + "'"
	#query = query + clientTable + ')'
	print(query)
	clientCursor.execute(query)
	schema = clientCursor.fetchall()
	columnName = []
	for i in schema:
		columnName.append(i[1])
	print(columnName)
	hostTable.columns = columnName[::-1]
	clientTable=clientTable.lower()
	hostTable.to_sql(clientTable,con=hostEngine,if_exists='replace')
	query = 'select * from ' + clientTable
	hostCursor.execute(query)
	res=hostCursor.fetchall()
	for i in res:
		print(i)



migrator(client, host, "trainee", clientEngine, hostEngine)

hostConnectionString.close()
clientConnectionString.close()


