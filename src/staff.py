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


def register():
    internal = False
    ID_number = input('身份证号:')
    full_name = input('姓名:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'SELECT * FROM internal_staff WHERE ID_number=%s;'

    data = [ID_number]

    result = cursor.execute(SQL, data)
    if (result != 0):
        internal = True
        return internal, ID_number
    else:
        SQL = 'SELECT * FROM external_staff WHERE ID_number=%s;'
        data = [ID_number]
        result = cursor.execute(SQL, data)
        if (result != 0):
            return internal, ID_number
        else:
            deposit = input('按Y键交押金,按N键不交\n>')
            if (deposit == 'y' or deposit == 'Y'):
                print('已交押金')
                SQL = 'INSERT INTO external_staff (ID_number,full_name) VALUES (%s,%s)'
                data = [ID_number, full_name]
                cursor.execute(SQL, data)

                conn.commit()

                cursor.close()
                conn.close()
                return internal, ID_number
            elif (deposit == 'n' or deposit == 'N'):
                while (deposit != 'y' and deposit != 'Y'):
                    deposit = input('未交押金,请按Y键交押金\n>')
                    if (deposit == 'y' or deposit == 'Y'):
                        print('已交押金')
                        SQL = 'INSERT INTO external_staff (ID_number,full_name) VALUES (%s,%s)'
                        data = [ID_number, full_name]
                        cursor.execute(SQL, data)

                        conn.commit()

                        cursor.close()
                        conn.close()
                        return internal, ID_number
