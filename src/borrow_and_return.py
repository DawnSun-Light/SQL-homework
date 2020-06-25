import pymysql


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


def borrow():
    internal, ID_number = register()

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    if (internal == True):
        SQL = 'SELECT overdue FROM internal_staff'
    else:
        SQL = 'SELECT overdue FROM external_staff'
    cursor.execute(SQL)
    result = cursor.fetchone()
    if (result[-1] > 0):
        return -1

    if (internal == True):
        SQL = 'SELECT number_of_books_borrowed FROM internal_staff'
        cursor.execute(SQL)
        result = cursor.fetchone()
        if (result == 5):
            return -1
    else:
        SQL = 'SELECT number_of_books_borrowed FROM external_staff'
        cursor.execute(SQL)
        result = cursor.fetchone()
        if (result == 2):
            return -1

    ISBN = input('ISBN:')

    SQL = 'INSERT INTO borrowing (internal,ID_number,ISBN) VALUES (%s,%s,%s);'

    data = [internal, ID_number, ISBN]

    cursor.execute(SQL, data)

    SQL = 'UPDATE book SET remaining_quantity=book.remaining_quantity-1 WHERE ISBN=%s;'
    data = [ISBN]
    cursor.execute(SQL, data)

    if (internal == True):
        SQL = 'UPDATE internal_staff SET number_of_books_borrowed=internal_staff.number_of_books_borrowed+1 WHERE ID_number=%s'
    else:
        SQL = 'UPDATE external_staff SET number_of_books_borrowed=external_staff.number_of_books_borrowed+1 WHERE ID_number=%s'
    data = [ID_number]
    cursor.execute(SQL, data)

    conn.commit()

    cursor.close()
    conn.close()


def back():
    internal, ID_number = register()

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    ISBN = input('ISBN:')

    SQL = 'UPDATE borrowing SET return_time=CURRENT_TIME WHERE ISBN=%s AND ID_number=%s;'
    data = [ISBN, ID_number]
    cursor.execute(SQL, data)

    SQL = 'SELECT borrow_time FROM borrowing WHERE ISBN=%s AND ID_number=%s;'
    data = [ISBN, ID_number]
    cursor.execute(SQL, data)
    borrow_time = cursor.fetchone()

    SQL = 'SELECT return_time FROM borrowing WHERE ISBN=%s AND ID_number=%s;'
    data = [ISBN, ID_number]
    cursor.execute(SQL, data)
    return_time = cursor.fetchone()

    SQL = 'SELECT TIMESTAMPDIFF(DAY,%s,%s);'
    data = [borrow_time[-1], return_time[-1]]
    cursor.execute(SQL, data)
    result = cursor.fetchone()

    if (result[-1] > 30):
        overdue = result[-1] - 30
        fine = overdue
        if (internal == False):
            fine = overdue * 3
        print(f'超期{overdue}天,罚金{fine}元:')

        SQL = 'UPDATE borrowing SET fine=%s WHERE ISBN=%s AND ID_number=%s;'
        data = [fine, ISBN, ID_number]
        cursor.execute(SQL, data)

    SQL = 'UPDATE book SET remaining_quantity=book.remaining_quantity+1 WHERE ISBN=%s;'
    data = [ISBN]
    cursor.execute(SQL, data)

    if (internal == True):
        SQL = 'UPDATE internal_staff SET number_of_books_borrowed=internal_staff.number_of_books_borrowed-1 WHERE ID_number=%s'
    else:
        SQL = 'UPDATE external_staff SET number_of_books_borrowed=external_staff.number_of_books_borrowed-1 WHERE ID_number=%s'
    data = [ID_number]
    cursor.execute(SQL, data)

    SQL = 'DELETE FROM external_staff WHERE number_of_books_borrowed=0;'
    cursor.execute(SQL)

    conn.commit()

    cursor.close()
    conn.close()
