
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

