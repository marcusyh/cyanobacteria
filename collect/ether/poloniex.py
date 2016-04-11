from data_agent import data_agent

def get_prices():
    url   = 'https://poloniex.com/public?command=returnTicker'
    rslt  = data_agent(url)
    return rslt

def get_24hVolumes():
    url  = 'https://poloniex.com/public?command=return24hVolume'
    rslt = data_agent(url)
    return rslt

def get_depth(flag):
    url  = 'https://poloniex.com/public?command=returnOrderBook&currencyPair=%s&depth=100000' %flag

    bids = {}
    asks = {}

    temp = data_agent(url)

    for x in temp['bids']:
        cur_price    = float(x[0])
        cur_source   = x[1]
        cur_btc      = cur_price * cur_source

        bids[cur_price] = cur_btc

    for x in temp['asks']:
        cur_price    = float(x[0])
        cur_source   = x[1]

        asks[cur_price] = cur_source

    return bids, asks

def get_data():
    markets = {
            'btc': 'BTC_ETH', 
            'usd': 'USDT_ETH'
            }
    result = {}

    prices  = get_prices()
    volumes = get_24hVolumes()

    for key, value in markets.iteritems():
        bids, asks = get_depth(value)
        result[key] = {
                'price': float(prices[value]['last']),
                'volume': float(volumes[value]['ETH']),
                'bids': bids,
                'asks': asks
                }
    return result
