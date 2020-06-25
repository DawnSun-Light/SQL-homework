import pymysql


def insert():
    ID_number = input('身份证号:')
    full_name = input('姓名:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'INSERT INTO internal_staff (ID_number,full_name) VALUES (%s,%s);'

    data = [ID_number, full_name]

    cursor.execute(SQL, data)

    conn.commit()

    cursor.close()
    conn.close()


def delete():
    ID_number = input('身份证号:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'DELETE FROM internal_staff WHERE ID_number=%s;'

    data = [ID_number]

    cursor.execute(SQL, data)

    conn.commit()

    cursor.close()
    conn.close()
