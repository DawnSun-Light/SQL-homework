import pymysql


def insert():
    ISBN = input('ISBN:')
    book_name = input('图书名:')
    press = input('出版社:')
    author = input('作者:')
    book_classification = input('图书分类:')
    year_of_publication = input('出版年份:')
    remaining_quantity = input('剩余数量:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'INSERT INTO book (ISBN,book_name,press,author,book_classification,year_of_publication,remaining_quantity) VALUES (%s,%s,%s,%s,%s,%s,%s);'

    data = [ISBN, book_name, press, author, book_classification,
            year_of_publication, remaining_quantity]

    cursor.execute(SQL, data)

    conn.commit()

    cursor.close()
    conn.close()


def update():
    ISBN = input('ISBN:')
    remaining_quantity = input('剩余数量:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'UPDATE book SET remaining_quantity=%s WHERE ISBN=%s;'

    data = [remaining_quantity, ISBN]

    cursor.execute(SQL, data)

    conn.commit()

    cursor.close()
    conn.close()


def delete():
    ISBN = input('ISBN:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'DELETE FROM book WHERE ISBN=%s;'

    data = [ISBN]

    cursor.execute(SQL, data)

    conn.commit()

    cursor.close()
    conn.close()


def select():
    info = input('info:')

    conn = pymysql.connect(host="192.168.1.104", port=3305, user="root",
                           password="123456", database="library", charset="utf8")

    cursor = conn.cursor()

    SQL = 'SELECT * FROM book WHERE ISBN=%s OR book_name=%s OR press=%s OR author=%s OR book_classification=%s OR year_of_publication=%s;'

    data = [info, info, info, info, info, info]

    cursor.execute(SQL, data)

    results = cursor.fetchall()
    for result in results:
        print(result)

    cursor.close()
    conn.close()
