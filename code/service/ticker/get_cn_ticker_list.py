import tushare
import datetime


# 获取tickers
def get_cn_tickers():
    tickersRawData = get_cn_raw_data()
    tickers = tickersRawData.index.tolist()
    return tickers


def get_cn_raw_data():
    return tushare.get_stock_basics()


def save_cn_data():
    # 存入本地文件
    dataToday = datetime.datetime.today().strftime('%Y%m%d')
    file = '../../data/TickListCN/TickerList-' + dataToday + '.csv'
    get_cn_raw_data().to_csv(file)
    print("获取CN-Tickers数据成功，并完成保存")
