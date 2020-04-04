import requests
import pandas
import io
import datetime


# 获取tickers
def get_us_tickers():
    return get_us_raw_data()['Symbol'].tolist()


def get_us_raw_data():
    url = 'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'
    dataString = requests.get(url).content
    return pandas.read_csv(io.StringIO(dataString.decode("utf-8")))


# 存入本地文件
def save_us_data():
    dataToday = datetime.datetime.today().strftime('%Y%m%d')
    file = '../../data/TickListUS/TickerList-'+dataToday+'.csv'
    get_us_raw_data().to_csv(file, index=False)
    print("获取US-Tickers数据成功，并完成保存")
