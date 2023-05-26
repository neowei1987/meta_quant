
# 技术面
# 趋势方向如何
# 涨跌空间大小
# 有无买/卖信号


# 资金面
# 大盘/板块资金流向
# 个股资金流向
# 主力大单的表现 【影响很大】

# 基本面，选股有用
# 业绩表现
# 潜力大小
# 是否抗跌

# 消息面
# 市场情绪
# 利多/利空的消息/新闻
# 公告事件

# 数据


if __name__ == "__main__":
    csv_dir = '/path/to/your/csv/file'  # CHANGE THIS!
    symbol_list = ['SPY']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(2006,1,3)

    backtest = Backtest(
        csv_dir, symbol_list, initial_capital, heartbeat,
        start_date, HistoricCSVDataHandler, SimulatedExecutionHandler,
        Portfolio, SPYDailyForecastStrategy
    )
    backtest.simulate_trading()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
