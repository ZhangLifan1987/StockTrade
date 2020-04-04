from code.service.intraday.get_cn_intraday import stock_cn_price_intraday
from code.service.ticker.get_cn_ticker_list import get_cn_tickers, save_cn_data

save_cn_data()
tickers = get_cn_tickers()
for i, ticker in enumerate(tickers):
    try:
        print('Intraday', ticker, i, '/', len(tickers))
        stock_cn_price_intraday(ticker, folder="../../data/IntradayCN")
    except:
        pass
    if i > 3:
        break
print("CN-Intraday for all stocks got.")


