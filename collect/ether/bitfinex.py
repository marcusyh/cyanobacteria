from data_agent import data_agent

def get_price(flag):
    url   = 'https://api.bitfinex.com/v1/pubticker/%s' %flag
    temp  = data_agent(url)
    return float(temp['last_price']), float(temp['volume'])
    

def get_depth(flag):
    url  = 'https://api.bitfinex.com/v1/book/%s?limit_bids=10000000&limit_asks=10000000&group=0' %flag
    temp = data_agent(url)
    bids = {}
    asks = {}

    for x in temp['bids']:
        cur_price    = float(x['price'])
        cur_source   = float(x['amount'])
        cur_btc      = cur_price * cur_source

        bids[cur_price] = cur_btc

    for x in temp['asks']:
        cur_price    = float(x['price'])
        cur_source   = float(x['amount'])

        asks[cur_price] = cur_source

    return bids, asks


def get_data():
    markets = {
            'btc': 'ETHBTC', 
            'usd': 'ETHUSD'
            }
    result = {}

    for key, value in markets.iteritems():
        price, volume = get_price(value)
        bids, asks    = get_depth(value)
        result[key] = {
                'price': price,
                'volume': volume,
                'bids': bids,
                'asks': asks
                }
    return result

