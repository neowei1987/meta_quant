from data.time_segment_data import TimeSegmentData
from util.date import get_months_between


class TimeRangeData:
    """
    TimeRangeData，代表了一个时间段内的数据
    """

    def __init__(self, symbol, begin_time, end_time, time_frame):
        """
        Initialises the historic data handler by requesting
        the location of the CSV files and a list of symbols.
        It will be assumed that all files are of the form
        ’symbol.csv’, where symbol is a string in the list.
        Parameters:
        events - The Event Queue.
        csv_dir - Absolute directory path to the CSV files.
        symbol_list - A list of symbol strings.
        """
        months = get_months_between(begin_time, end_time)
        segment_data = []
        for month in months:
            segment_data.append(TimeSegmentData(symbol, month, time_frame))
        self.segments = segment_data
        self.seg_idx = 0

    def get_new_bar(self):
        while True:
            try:
                if self.seg_idx == len(self.segments):
                    return None
                bar = next(self.segments[self.seg_idx].get_new_bar())
            except StopIteration:
                if self.seg_idx == len(self.segments):
                    return None
                self.seg_idx += 1
            else:
                return bar
