import pymysql

# �����ݿ�����
db = pymysql.connect(host="127.0.0.1",port=3306,user="user", password="password", database="databaseName",charset="utf8")

# ʹ��cursor()������ȡ�����α�
cursor = db.cursor()

# SQL ��ѯ���
sql = "SELECT * FROM `mobile_log`.`dbsvr_login_lobby` \
WHERE`logtime` BETWEEN '2020-09-07 21:21:10' AND '2020-09-07 22:10:10' \
cursor.execute(sql)
print(cursor.rowcount)
result = cursor.fetchall()
for item in result:
    print(item)
db.close()
