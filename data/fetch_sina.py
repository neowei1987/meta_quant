
import urllib3

#beautifulsoup

#创建连接池
conn_pool = urllib3.PoolManager()
#获取行情数据
response = conn_pool.request('GET','http://hq.sinajs.cn/?list=sh601989')
#解析抓取结果
hq_str = response.data.decode('GBK')
print(hq_str)
hq_str = hq_str[hq_str.index('="')+2:-3]
hq_fields = hq_str.split(',')
stock_realtime = {
'name':hq_fields[0],
'open':hq_fields[1],
'pre_close':hq_fields[2]
}
print(stock_realtime)


#pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

# 神奇的链接http://hq.sinajs.cn/list=sh600000,sh600004

# 本程序的作用是：从新浪网上，将所有股票最新的数据抓取下来并且保存。
# 可以每天定期运行，然后就能得到每天的数据了。