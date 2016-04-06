from data_agent import data_agent

def get_price(flg):
    url   = 'https://api.kraken.com/0/public/Ticker?pair=%s' %flag
    rslt  = data_agent(url)

    return float(rlst['result'][flag]['c'][0])

def get_depth(flag):
    url  = 'https://api.kraken.com/0/public/Depth?pair=%s&count=100000000000' %flag

    bids = {}
    asks = {}

    temp = data_agent(url)['result'][flag]
    asks = temp['asks']
    for x in rslt['bids']:
        cur_price    = float(x[0])
        cur_source   = float(x[1])
        cur_btc      = cur_price * cur_source

        bids[cur_price] = cur_btc

    return bids, asks

def get_poloniex():
    markets = {
            'btc': 'xethxxbt', 
            'eur': 'xethzeur', 
            'usd': 'xethzusd', 
            'cad': 'xethzcad', 
            'gbp': 'xethzgbp', 
            'jpy': 'xethzjpy'
            }
    price = get_price()
    bids, asks = get_depth()
    return price, bids, asks
