import pymysql

baglantı = pymysql.connect(host='localhost',
                             user='username',
                             password='password',
                             db='databaseadi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)