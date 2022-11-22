import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='db2' ,  auth_plugin='mysql_native_password')

mycursor = cnx.cursor()
mycursor.execute("select sum(amount) as a ,shop_id from main_payments_payment where time_stamp>='2021-11-19' group by shop_id ;")
result = mycursor.fetchall()
print("")
for a, shop_id ,  in result:
    print(shop_id," has to be paid ",a," amount")
cnx.close()