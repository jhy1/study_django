import pymysql
con=pymysql.connect(
    user='root',
    password='123456',
    port='3308',
    database='test'
)
cur=con.cursor(cursor=pymysql.cursors.DictCursor)
sql=''
res=cur.execute(sql)
print(res)

respon=cur.fetall()
print(respon)

