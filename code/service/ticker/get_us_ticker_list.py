import requests
import pandas
import io
import datetime

# 获取tickers
from code.dao import mysql_dao
from code.util import parsePrice, parseNumber


def get_us_tickers():
    sql = "select distinct symbol from tickers_us where version = (select max(version) as current_version from tickers_us)"
    data = mysql_dao.executeSql(sql, queryType=True)
    return [item[0] for item in data]


def get_us_raw_data():
    url = 'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'
    dataString = requests.get(url).content
    return pandas.read_csv(io.StringIO(dataString.decode("utf-8")))


# 存入本地文件
def save_us_data():
    dataToday = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    # file = '../../data/TickListUS/TickerList-'+dataToday+'.csv'
    # get_us_raw_data().to_csv(file, index=False)

    rowDataList = get_us_raw_data()
    length = rowDataList.shape[0]
    for i in range(0, length):
        rowData = rowDataList.loc[i]
        sql = """insert into tickers_us (
        symbol,
        name,
        last_sale,
        market_cap,
        ipo_year,
        sector,
        industry,
        summary_quote,
        version) 
        values(
        '{0}','{1}',{2},{3},{4},'{5}','{6}','{7}', '{8}')
        """.format(rowData['Symbol'], rowData['Name'], parseNumber(rowData['LastSale']), parsePrice(rowData['MarketCap']),
                   parseNumber(rowData['IPOyear']), rowData['Sector'], rowData['industry'], rowData['Summary Quote'],
                   dataToday)
        mysql_dao.executeSqlBatch(sql)
    mysql_dao.closeConnect(True)
    print("获取US-Tickers数据成功，并完成保存")


save_us_data()