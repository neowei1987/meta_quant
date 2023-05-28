import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from binance.client import Client
import pandas as pd
import mplfinance as mpl
from binance.cm_futures import CMFutures

api_key = "Y2kKcBDco2qrE94Ik0zHsKtl7jQQGSF170sVRLkA5oVPf8KITmIro5hZRxeSAI8z"
api_secret = "FF7DzkcriUpEAQyW9v5rEsLUAMdhqIjlzYCFu3ietKJfi7SyAoDtxIEdc80Os4i8"
client=Client(api_key, api_secret)


def download_klines(symbol, timeframe, begin, end, limit):
    all_klines = []
    while True:
        klines = client.get_historical_klines(symbol, timeframe, begin, end, limit)
        all_klines.extend(klines)
        if len(klines) == limit:
            last_open_time = klines[-1][0]
            begin = last_open_time + 1000
            time.sleep(0.1)
        else:
            break
    return all_klines


def get_historical_klines(symbol, timeframe, start, end, limit=1000):
    delta = end - start
    num_threads = (delta // (limit * 60 * 1000)) + 1
    delta_per_thread = delta // num_threads
    begin = start
    end = begin + delta_per_thread
    futures = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            if i == num_threads - 1:
                end = end + delta % delta_per_thread
            futures.append(executor.submit(download_klines, symbol, timeframe, begin, end, limit))
            begin = end + 1
            end = begin + delta_per_thread - 1
    all_klines = []
    for future in as_completed(futures):
        all_klines.extend(future.result())
    return all_klines
