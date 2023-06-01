import datetime
import time

from data.time_segment_data import TimeSegmentData
from util.date import get_months_between

if __name__ == "__main__":

    symbol_list = ['BTCUSDT']
    start_date = datetime.datetime(2017, 8, 14, 0, 0, 0)
    end_date = datetime.datetime(2023, 6, 1, 0, 0, 0)

    for symbol in symbol_list:
        months = get_months_between(start_date, end_date)
        for month in months:
            time_segment_data = TimeSegmentData(symbol, month, "1m")
            time_segment_data.download_bars()
            try:
                time_segment_data.download_bars()
            except IOError:
                print("Error downloading bars " + str(month))
            else:
                print("download bars success " + str(month))
