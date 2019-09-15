"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
from datetime import date
from datetime import datetime
from datetime import timedelta

def decrease_month(current_date):
    day = current_date.day
    if current_date.month == 1:
        month = 12
        year = current_date.year - 1
    else:
        month = current_date.month - 1
        year = current_date.year
    return date(year, month, day)

def print_days():
    today = date.today()
    yesterday = today - timedelta(days=1)
    month_ago = decrease_month(today)

    print("Today is", today)
    print("Yesterday was", yesterday)
    print("Month ago was", month_ago)   
    
def str_2_datetime(string):
    return datetime.strptime(string, "%m/%d/%y %H:%M:%S.%f")

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
