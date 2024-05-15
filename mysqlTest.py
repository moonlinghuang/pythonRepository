import pymysql
SQL_IP = '192.168.182.132'
SQL_USERNAME = 'root'
SQL_PASSWORD = 'root'
SQL_DB = 'TestingPython'

sql_connection = pymysql.connect(host=SQL_IP, user=SQL_USERNAME, password=SQL_PASSWORD, db=SQL_DB)

employee1 = {
    "id": 3,
    "fname": "meng",
    "lname": "ling",
    "Title": "NW_ENG"
}
employee2 = {
    "id": 2,
    "fname": "ling",
    "lname": "huang",
    "Title": "DEVELOPER"
}

employees = [employee1,employee2]
cursor = sql_connection.cursor()

# for record in employees:
#     SQL_COMMAND = """INSERT INTO TestTable(id, fname, lname, Title) VALUES
#     ({0},'{1}','{2}','{3}')""".format(record["id"],record["fname"],record["lname"],record['Title'])
#     print(SQL_COMMAND)
#     try:
#         cursor.execute(SQL_COMMAND)
#         sql_connection.commit()
#     except:
#         sql_connection.rollback()
#         print(SQL_COMMAND+"failed")
cursor.execute("select * from TestTable")
print(cursor.fetchall())

sql_connection.close()