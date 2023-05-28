
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_months_between(begin, end):
    months = []
    while begin <= end:
        months.append(begin.strftime('%Y-%m'))
        begin += relativedelta(months=1)
    return months


def is_current_month(date_time):
    now = datetime.now()
    return date_time.year == now.year and date_time.month == now.month


def get_first_and_last_day_of_month(month_str):
    month = datetime.strptime(month_str, '%Y-%m')
    first_day = month.replace(day=1)
    next_month = first_day.replace(day=28) + timedelta(days=4)
    last_day = next_month - timedelta(days=next_month.day)
    return first_day, last_day


def datetime_to_milliseconds(dt):
    epoch = datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000.0)