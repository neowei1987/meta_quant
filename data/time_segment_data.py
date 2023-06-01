import os
import time

import pandas as pd

from facade.binance_api import get_historical_klines
from util.date import get_first_and_last_day_of_month, datetime_to_milliseconds

DATA_PATH = "/Users/neowei/quant_data"


class TimeSegmentData:
    """
    TimeSegmentData，代表了一个时间片段内的数据
    1. 支持从文件中读取数据到内存
    2. 将内存中的数据写入到文件中

    读取数据，判断文件是否存在，则直接读取；
    如果不存在，则写入文件
    """

    def __init__(self, symbol, month, time_frame):
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
        self.symbol = symbol
        self.month = month
        self.month_first_day, self.month_last_day = get_first_and_last_day_of_month(month)
        self.file_path = os.path.join(DATA_PATH, symbol, symbol + "_" + month + "_" + time_frame + ".csv")
        self.df = None

    def _read_local_file(self):
        comb_index = None
        data = pd.read_csv(self.file_path,
                           header=0, index_col=0, parse_dates=True,
                           names=["Date", "Open", "High", "Low", "Close", "Volume"])
        # Combine the index to pad forward values
        if comb_index is None:
            comb_index = data.index
        else:
            comb_index.union(data.index)
        # Reindex the dataframes
        data = data.reindex(index=comb_index, method='pad').iterrows()
        return data

    def _fetch_from_remote_server(self):
        data = get_historical_klines(self.symbol, "1m",
                                     datetime_to_milliseconds(self.month_first_day),
                                     datetime_to_milliseconds(self.month_last_day) + (86400 - 1) * 1000)
        df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Volume", *range(6, len(data[0]))])
        if df.empty:
            return df

        df = df.iloc[:, :6]
        df = df.set_index("Date")
        df = df.sort_index(axis=0)
        df.index = pd.to_datetime(df.index, unit="ms")
        df = df.astype("float")
        return df

    def _write_to_local_file(self):
        self.df.to_csv(self.file_path, index=True)
        df_5m = self.df.resample('5T').agg(
            {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        df_5m.to_csv(os.path.join(DATA_PATH, self.symbol + "_" + self.month + "_" + "5m" + ".csv"), index=True)
        df_1h = self.df.resample('1H').agg(
            {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        df_1h.to_csv(os.path.join(DATA_PATH, self.symbol + "_" + self.month + "_" + "1h" + ".csv"), index=True)
        df_1d = self.df.resample('1D').agg(
            {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        df_1d.to_csv(os.path.join(DATA_PATH, self.symbol + "_" + self.month + "_" + "1d" + ".csv"), index=True)

        # df_1d = self.df.resample('1D').agg(
        #    {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum', 'close_time': 'last',
        #     'quote_asset_volume': 'sum', 'number_of_trades': 'sum', 'taker_buy_base_asset_volume': 'sum',
        #     'taker_buy_quote_asset_volume': 'sum', 'ignore': 'last'})


    def get_new_bar(self):
        """
        Returns the latest bar from the data feed.
        """
        if self.df is None:
            if os.path.exists(self.file_path):
                self.df = self._read_local_file()
            else:
                self.df = self._fetch_from_remote_server()
                self._write_to_local_file()
                self.df = self.df.iterrows()

        for b in self.df:
            yield b

    def download_bars(self):
        """
        Returns the latest bar from the data feed.
        """
        if self.df is None:
            if not os.path.exists(self.file_path):
                self.df = self._fetch_from_remote_server()
                self._write_to_local_file()
                time.sleep(20)

