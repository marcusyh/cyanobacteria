from data_agent import data_agent

def get_price():
    url   = 'https://poloniex.com/public?command=returnTicker'
    rslt  = data_agent(url)

    return float(rlst[flag]['last'])

def get_depth():
    flag = 'BTC_ETH'
    url  = 'https://poloniex.com/public?command=returnOrderBook&currencyPair=%s&depth=100000' %flag

    bids = {}
    asks = {}

    temp = data_agent(url)
    asks = temp['asks']
    for x in rslt['bids']:
        cur_price    = float(x[0])
        cur_source   = x[1]
        cur_btc      = cur_price * cur_source

        bids[cur_price] = cur_btc

    return bids, asks

def get_poloniex():
    price = get_price()
    bids, asks = get_depth()
    return price, bids, asks
