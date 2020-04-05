import datetime

from code.service.intraday.get_us_intraday import stock_us_price_intraday
from code.service.ticker.get_us_ticker_list import get_us_tickers
import time

tickers = get_us_tickers()
version = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
for i, ticker in enumerate(tickers):
    try:
        print('Intraday', ticker, i, '/', len(tickers))
        stock_us_price_intraday(ticker, version)
        time.sleep(1)
    except:
        pass
    if i > 3:
        break
print("US-Intraday for all stocks got.")

