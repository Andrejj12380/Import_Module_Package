# coding=utf-8
from application.salary import *
from application.db.people import *
from datetime import datetime

date = datetime.ctime(datetime.now())

if __name__ == '__main__':
    calculate_salary(date)
    get_employees(date)