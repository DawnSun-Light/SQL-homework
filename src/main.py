import pymysql
import book
import staff
import borrow_and_return
import os


def index():
    os.system('cls')
    print('罗东旭-18180100109')
    print('图书馆借还书系统')
    print('1.图书管理')
    print('2.人员管理')
    print('3.借还书')
    function = input('请选择您要使用的功能,或按N键退出系统\n>')
    if(function == '1'):
        os.system('cls')
        book_manage()
    elif(function == '2'):
        os.system('cls')
        staff_manage()
    elif(function == '3'):
        os.system('cls')
        borrow_return_book()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        print('您已退出系统')
    else:
        os.system('cls')
        print('您的输入有误')
        index()


def book_manage():
    print('图书管理')
    print('1.插入图书信息')
    print('2.删除图书信息')
    print('3.修改图书信息')
    print('4.查询图书信息')
    function = input('请选择您要使用的功能,或按N键返回\n>')
    if(function == '1'):
        os.system('cls')
        print('插入图书信息')
        book.insert()
        print('插入成功')
        book_manage()
    elif(function == '2'):
        os.system('cls')
        print('删除图书信息')
        book.delete()
        print('删除成功')
        book_manage()
    elif(function == '3'):
        os.system('cls')
        print('修改图书信息')
        book.update()
        print('修改成功')
        book_manage()
    elif(function == '4'):
        os.system('cls')
        print('查询图书信息')
        book.select()
        print('查询结束')
        book_manage()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        print('您的输入有误')
        book_manage()


def staff_manage():
    print('人员管理')
    print('1.插入内部人员信息')
    print('2.删除内部人员信息')
    print('3.登记外部人员信息')
    function = input('请选择您要使用的功能,或按N键返回\n>')
    if(function == '1'):
        os.system('cls')
        print('插入内部人员信息')
        staff.insert()
        print('插入成功')
        staff_manage()
    elif(function == '2'):
        os.system('cls')
        print('删除内部人员信息')
        staff.delete()
        print('删除成功')
        staff_manage()
    elif(function == '3'):
        os.system('cls')
        print('登记外部人员信息')
        borrow_and_return.register()
        print('登记成功')
        staff_manage()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        print('您的输入有误')
        staff_manage()


def borrow_return_book():
    print('借还书')
    print('1.借书')
    print('2.还书')
    function = input('请选择您要使用的功能,或按N键返回\n>')
    if (function == '1'):
        os.system('cls')
        print('借书')
        borrow_and_return.borrow()
        print('借书成功')
        index()
    elif (function == '2'):
        os.system('cls')
        print('还书')
        borrow_and_return.back()
        print('还书成功')
        index()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        print('您的输入有误')
        borrow_return_book()


index()
