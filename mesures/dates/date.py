from datetime import datetime, timedelta

def last_hour_of_day(self, timestamp):
    return (datetime.strptime(timestamp, '%Y/%m/%d %H:%M:%S') - timedelta(days=1)).strftime('%Y/%m/%d')