from datetime import datetime, timedelta

DATE_MASK = '%Y/%m/%d %H'
DATETIME_MASK = '%Y/%m/%d %H:%M:%S'
REE_END_DATE = '30000101'

def last_hour_of_day(timestamp):
    return (datetime.strptime(timestamp, DATETIME_MASK) - timedelta(days=1)).strftime('%Y/%m/%d')