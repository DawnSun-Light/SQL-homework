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
    print('3.借书')
    print('4.还书')
    function = input('请选择您要使用的功能,或按N键退出系统\n>')
    if(function == '1'):
        os.system('cls')
        book_manage()
    elif(function == '2'):
        os.system('cls')
        staff_manage()
    elif(function == '3'):
        os.system('cls')
        borrow_book()
    elif(function == '4'):
        os.system('cls')
        return_book()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        print('您已退出系统')
    else:
        os.system('cls')
        print('您的输入有误')
        index()


def book_manage():
    print('罗东旭-18180100109')
    print('图书馆借还书系统')
    print('图书管理')
    print('1.插入图书信息')
    print('2.删除图书信息')
    print('3.修改图书信息')
    print('4.查询图书信息')
    function = input('请选择您要使用的功能,或按N键返回\n>')
    if(function == '1'):
        os.system('cls')
        book.insert()
        book_manage()
    elif(function == '2'):
        os.system('cls')
        book.delete()
        book_manage()
    elif(function == '3'):
        os.system('cls')
        book.update()
        book_manage()
    elif(function == '4'):
        os.system('cls')
        book.select()
        book_manage()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        print('您的输入有误')
        book_manage()


def staff_manage():
    print('罗东旭-18180100109')
    print('图书馆借还书系统')
    print('人员管理')
    print('1.插入内部人员信息')
    print('2.删除内部人员信息')
    print('3.登记外部人员信息')
    function = input('请选择您要使用的功能,或按N键返回\n>')
    if(function == '1'):
        os.system('cls')
        staff.insert()
        staff_manage()
    elif(function == '2'):
        os.system('cls')
        staff.delete()
        staff_manage()
    elif(function == '3'):
        os.system('cls')
        borrow_and_return.register()
        staff_manage()
    elif(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        print('您的输入有误')
        staff_manage()


def borrow_book():
    print('罗东旭-18180100109')
    print('图书馆借还书系统')
    print('借书')
    function = input('按任意键借书,按N键返回\n>')
    if(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        borrow_and_return.borrow()


def return_book():
    print('罗东旭-18180100109')
    print('图书馆借还书系统')
    print('还书')
    function = input('按任意键还书,按N键返回\n>')
    if(function == 'n' or function == 'N'):
        os.system('cls')
        index()
    else:
        os.system('cls')
        borrow_and_return.back()


index()
