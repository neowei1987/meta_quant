择时--买入

## 趋势跟随型策

创新高时，入场；
市场逆转，并且逆转趋势维持了几个星期就会退出。

大的趋势很少出现，这也就意味着胜率小于50%，海龟说"65%～70%"的交易都是赔钱的。

回撤：持续时间、程度（回撤比例）
回撤程度，大致接近于他们的回报水平。 如果你的期望年化回报率是30%，那么在回撤期，你的账号可能从高点下跌30%。

趋势追随，需要动用较大的资金量【TODO，！！资金量做模拟！】才能确保合理的风险控制。入市价位与止损价位，一般有很大的差距。


###海龟交易法

以海龟交易法则为例

市场：买卖什么？
    跨市场、高流动性！！最基本！！

头寸规模：买卖多少？
    波动性N：N=（19*PDN+TR）/20
    PDN=前一日的N值
    TR=当日的真实波动幅度
    真实波动幅度=MaX（H-L，H-PDC，PDC-L）
    其中：
    H=当日最高价
    L=当日最低价
    PDC=前一日收盘价
    头寸规模单位=账户的1%/（N*每一点数所代表的美元）
    每一点数所代表的美元》》》每一最小交易单位的资金（1手股票）

还有一些限制：
限制范围 头寸单位上限
单个市场 4
高度关联的多个市场 6
松散关联的多个市场 10
单个方向（多头或者空头） 12

入市：什么时候买卖？ 
    突破法----突破推最高点
    在每一个交易日结束后，都计算高低突破点。

   系统1： 以20（4个交易周）日突破为基础的短期系统 ；如果上一次突破是一次赢利性突破，那么当前的入市信号将被忽略 55日突破点保障性信号
    系统2： 60日（12个交易周）日突破为基础的长期系统

逐步加仓
    在突破点建立1个单位的头寸
    按N/2的价格间隔逐步扩大头寸
    以上一份订单的实际成交价为基准
    直到头寸达到规模上限

止损：什么时候放弃一个亏损的头寸？
    海龟止损标准
    任何一笔交易的风险程度不超过两个N（两个真实波动幅度均值），其实也就是账户的 2%
    
    价格变动的上限就是2N ；

    对于加仓情况，止损点上浮

退出：什么时候退出一个盈利的头寸？
    系统1：10日反向突破退出
    系统2： 20日反向突破退出
    就这么简单？
    退出不易
    克服提早退出的冲动
    坦然面对利润的蒸发


金叉：macd金叉、kd金叉
上穿均线：K线上穿5日均线、10日均线
单针探底：当日K线呈现单针探底形状
开收盘：开盘后5分钟、收盘前5分钟
筑底：在同一底部反复获得支撑
资金：主力资金加速流入

择时-卖出
死叉：macd死叉、kd死叉
下穿均线：K线下穿5日均线、10日均线
上冲回落：当日K线呈现长上影线形状
开收盘：开盘后5分钟、收盘前5分钟
筑顶：反复冲击同一顶部，而无法突破
资金：主力资金加速流出

四周法则最高价

双均线交叉信号

低市盈率加速上涨策略

股票池：
1. 股票池容量 50以内
2. 0 < PE < 35
3. 调仓周期：30交易日

择时：
买入：日K线上穿10、15、20日移动均线
卖出：日K线下穿10、15、20日移动均线

追随强者:海龟交易法则！
一个交易系统的要素


战术：怎么买卖？

实战中的交易处理：

你有预案吗？

流动性瞬间枯竭====》 
    限价单VS.市价单【局势缓和下来之后，如何量化？】
跳空
    一系列交易信号，怎么办？
跨市场选择
    买强卖弱
合约滚动
    ？
为什么是20/10和55/20？
    参数选择：经验选择

市场在大多数时间是无效震荡
大的趋势只在少数时间内出现
小幅震荡VS.大幅趋势
蚂蚁战术Vs.高收益高回撤


### 均值回复型

高位卖空，低位买入。 
盈利源泉：市场的支撑与阻力机制。

理论依据：
一个运动员的表现可以被认为是围绕均值随机分布的

#### 短期市场反转

建立一个股票池：

过去3（或者1）表现最差的N只股票构成的组合
再平衡周期：1个月

头寸管理：
- 所有入选股票均仓
- 按照市值加权

多空组合：
做多表现最差，同时 最空表现最好

#### 长期市场反转

与短期反转的区别
过去1年/3年/5年表现最差的
N只股票构成投资组合
再平衡周期加长
比如1年
也可以多空
注意N的选择


### 两者的冲突&关系
取决于观察尺度

高抛低吸Or追涨杀跌
观察的尺度决定了你的判断
完全相同的周期，两者的结果必然相反
在不同的周期尺度下，两者都可以带来正收益

微小尺度：随机游走
小尺度：均值回复
中尺度：趋势跟随+均值回复
大尺度：趋势+反转


### 配对策略

套利模式

两只股票之间-完美替代品问题
    替代选择？ 做空成本比较高？ 
    在收到外力影响（例如负面新闻），价格出现偏离的时候，例如下跌
    买入A股票，同时做空B股票。

两组股票之间一测定相关性
    原理一样

2种或3种ETF之间
    EFT就是一揽子股票

ETF与一揽子股票之间


现货与期货之间
    跨期逃离

套利限制：

（1）基本面风险
替代性证券是不完美的，往往不完美。

（2）噪音交易者风险
没有最坏，只有更坏。【迫使交易者清仓】

（3）实施成本
不仅是费用，还有人的选择成本、！流动性枯竭！

如何寻找**定价错误**？ 付出的观测成本很高！

期现套利策略
![image](https://cdn.staticaly.com/gh/neowei1987/blog_assets@main/image.t4k5grsr2io.webp)


分级基金套利策略

母子基金比价出现折溢价时的套利
当母基金出现折价时，买入母基金并进行分拆，在二级市场
上分别卖出分级基金的A和B份额。
当母基金出现溢价时，在二级市场分别买入分级基金的A类
份额和B类份额，然后进行合并后卖出或者赎回母基金。


考虑不同的时间和空间尺度，并且把成交量因素引进到策路中

尺度量价

![image](https://cdn.staticaly.com/gh/neowei1987/blog_assets@main/image.1gkowf2lzh0g.webp)

缺口方式

寻找受到惊吓的股票

1.选择“缺口型”股票：开盘瞬间，选择所有的自前一日最低价至今
日开盘价之间的收益率低于一个标准差的股票。标准差定义为90
天的日间收盘价的收益率的标准差
川.缩小范围：只保留当日开盘价高于收盘价20日移动平均线的股票
川.在剩余股票中，按当日开盘价与前一日最低价相比得出的收益率由
低到高排序，买入排名前10的股票，不足10只就都买入
V.收盘之前清算（A股T+1怎么办？）

# 技术面
# 趋势方向如何
# 涨跌空间大小
# 有无买/卖信号

当日交易

头寸交易、抢帽子（做市商）、套利



======

四种市场状态：

稳定平静：小范围内上下波动
    
稳定波动：再大的日间或者周间变化，但没有重大的月际变化。
    反趋势交易者、波段交易者最爱
平静趋势：几个月中，呈现出缓慢的运动或者趋势，但始终没有大的回调或者反方向运动
    趋势交易者最喜欢
波动趋势：价格有大的变化，偶尔有剧烈的短期逆转

趋势的强度、波动性的程度

不预测市场会走成什么样，而是去寻找市场市场处于某种特定状态的指示信号。
