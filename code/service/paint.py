import pandas
import matplotlib
import mpl_finance
import matplotlib.pyplot as plt
import pymysql

matplotlib.style.use('ggplot')


def stock_price_plot(ticker):
    # history = pandas.read_csv('../../data/IntradayUS/' + ticker + '.csv', parse_dates=True, index_col=0)
    history = pandas.read_sql_query(
        sql="select timestamp,open,high,low,close,volume from intraday_us where symbol='{0}'".format(ticker),
        con=pymysql.connect("rm-2ze0gur4knf5f648joo.mysql.rds.aliyuncs.com",
                            "zhanglifan", "Larry@1987", "stock_trade"), parse_dates=True, index_col='timestamp')
    close = history['close']
    close = close.reset_index()
    close['timestamp'] = close['timestamp'].map(matplotlib.dates.date2num)

    ohlc = history[['open', 'high', 'low', 'close']].resample('1H').ohlc()
    ohlc = ohlc.reset_index()
    ohlc['timestamp'] = ohlc['timestamp'].map(matplotlib.dates.date2num)

    subplot1 = plt.subplot2grid((2, 1), (0, 0), rowspan=1, colspan=1)
    subplot1.xaxis_date()
    subplot1.plot(close["timestamp"], close['close'], 'b.')
    plt.title(ticker)

    subplot2 = plt.subplot2grid((2, 1), (1, 0), rowspan=1, colspan=1, sharex=subplot1)
    mpl_finance.candlestick_ohlc(ax=subplot2, quotes=ohlc.values, width=0.01, colorup='r', colordown='g')

    plt.show()


stock_price_plot('TXG')
