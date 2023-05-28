
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
import datetime

from backtest.backtest import Backtest
from data.smart_data import SmartDataHandler
from execution.execution import SimulatedExecutionHandler
from portfolio.portfolio import Portfolio
from strategy.mac import MovingAverageCrossStrategy

if __name__ == "__main__":

    csv_dir = '/path/to/your/csv/file'  # CHANGE THIS!
    symbol_list = ['BTCUSDT']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
    end_date = datetime.datetime(2023, 1, 10, 0, 0, 0)
    backtest = Backtest(
        csv_dir, symbol_list, initial_capital, heartbeat,
        start_date, end_date, "1m", SmartDataHandler, SimulatedExecutionHandler,
        Portfolio, MovingAverageCrossStrategy
    )
    backtest.simulate_trading()
