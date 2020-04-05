import pandas
import requests
import io

from code.dao import mysql_dao
from code.util import parseNumber


def stock_us_price_intraday(ticker, version):
    url = 'https://www.alphavantage.co/' \
        'query?apikey=L1XLJ8IDL5LHZ7NQ&function=TIME_SERIES_INTRADAY&symbol={ticker}' \
        '&interval=1min&outputsize=full&datatype=csv'.format(ticker=ticker)
    dataString = requests.get(url).content
    intraday = pandas.read_csv(io.StringIO(dataString.decode("utf-8")))

    # file = folder + '/' + ticker + '.csv'
    # if os.path.exists(file):
    #     history = pandas.read_csv(file, index_col=0)
    #     intraday.append(history)
    #
    # intraday.sort_index(inplace=True)
    # intraday.to_csv(file)

    length = intraday.shape[0]
    print(intraday)
    for i in range(0, length):
        rowData = intraday.loc[i]
        sql = """insert into intraday_us (
        symbol,
        timestamp,
        open,
        high,
        low,
        close,
        volume,
        version) 
        values(
        '{0}','{1}',{2},{3},{4},{5},{6},'{7}')
        """.format(ticker, rowData['timestamp'], parseNumber(rowData['open']), parseNumber(rowData['high']),
                   parseNumber(rowData['low']), parseNumber(rowData['close']), parseNumber(rowData['volume']), version)
        mysql_dao.executeSqlBatch(sql)
    mysql_dao.closeConnect(True)
    print("获取"+ticker+":US-Intraday数据成功，并完成保存")