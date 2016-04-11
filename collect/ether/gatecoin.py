from data_agent import data_agent

def get_prices(flags):
    url  = 'https://www.gatecoin.com/api/Public/LiveTickers'
    rslt = {}
    for item in data_agent(url)['tickers']:
        flag = item['currencyPair']
        if flag in flags: rslt[flag] = item
    return rslt

def get_depth(flag):
    url  = 'https://www.gatecoin.com/api/Public/MarketDepth/%s' %flag
    temp = data_agent(url)
    bids = {}
    asks = {}

    for x in temp['bids']:
        cur_price    = x['price']
        cur_source   = x['volume']
        cur_btc      = cur_price * cur_source

        bids[cur_price] = cur_btc

    for x in temp['asks']:
        cur_price    = x['price']
        cur_source   = x['volume']
        cur_btc      = cur_price * cur_source

        asks[cur_price] = cur_source

    return bids, asks


def get_data():
    markets = {
            'btc': 'ETHBTC', 
            'eur': 'ETHEUR', 
            }
    result = {}

    prices = get_prices(markets.values())
    
    for key, value in markets.iteritems():
        bids, asks = get_depth(value)
        result[key] = {
                'price': prices[value]['last'],
                'volume': prices[value]['volume'],
                'bids': bids,
                'asks': asks
                }
    return result

