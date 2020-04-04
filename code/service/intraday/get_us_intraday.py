import pandas
import requests
import io
import os


def stock_us_price_intraday(ticker, folder):
    url = 'https://www.alphavantage.co/' \
        'query?apikey=L1XLJ8IDL5LHZ7NQ&function=TIME_SERIES_INTRADAY&symbol={ticker}' \
        '&interval=1min&outputsize=full&datatype=csv'.format(ticker=ticker)
    dataString = requests.get(url).content
    intraday = pandas.read_csv(io.StringIO(dataString.decode("utf-8")), index_col=0)

    file = folder + '/' + ticker + '.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)

    intraday.sort_index(inplace=True)
    intraday.to_csv(file)

    print("获取"+ticker+":US-Intraday数据成功，并完成保存")
