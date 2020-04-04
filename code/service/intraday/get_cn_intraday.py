import tushare
import pandas
import os


def stock_cn_price_intraday(ticker, folder):
    intraday = tushare.get_hist_data(ticker, ktype='5')
    file = folder + '/' + ticker + '.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)

    intraday.sort_index(inplace=True)
    intraday.index.name = 'timestamp'
    intraday.to_csv(file)

    print("获取"+ticker+":CN-Intraday数据成功，并完成保存")
