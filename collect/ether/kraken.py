from data_agent import data_agent

def get_prices(flags):
    url   = 'https://api.kraken.com/0/public/Ticker?pair=%s' %flags
    return data_agent(url)['result']
    

def get_depth(flag):
    url  = 'https://api.kraken.com/0/public/Depth?pair=%s&count=100000000000' %flag
    temp = data_agent(url)['result'][flag]
    bids = {}
    asks = {}

    for x in temp['bids']:
        cur_price    = float(x[0])
        cur_source   = float(x[1])
        cur_btc      = cur_price * cur_source

        bids[cur_price] = cur_btc

    for x in temp['asks']:
        cur_price    = float(x[0])
        cur_source   = float(x[1])

        asks[cur_price] = cur_source

    return bids, asks


def get_data():
    markets = {
            'btc': 'XETHXXBT', 
            'eur': 'XETHZEUR', 
            'usd': 'XETHZUSD', 
            'cad': 'XETHZCAD', 
            'gbp': 'XETHZGBP', 
            'jpy': 'XETHZJPY'
            }
    result = {}

    prices = get_prices(','.join(markets.itervalues()))
    
    for key, value in markets.iteritems():
        bids, asks = get_depth(value)
        result[key] = {
                'price': float(prices[value]['c'][0]),
                'volume': float(prices[value]['v'][1]),
                'bids': bids,
                'asks': asks
                }
    return result

