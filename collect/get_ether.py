import importlib
import os
from operator import itemgetter

def get_data():
    ether_sites = []
    for fname in os.listdir('ether'):
        if fname in ['__init__.py', 'data_agent.py']:
            continue
        if fname.split('.')[1] == 'pyc':
            continue
        ether_sites.append(fname.split('.')[0])
    
    ether_tmp = []
    for site in ether_sites:
        print site
        mod = importlib.import_module('ether.%s' %site)
        tmp = mod.get_data()
        
        for market, data in tmp.iteritems():
            data.update({
                'platform': site,
                'market': market
                })
            ether_tmp.append(data)
    
    ether_data = sorted(ether_tmp, key=itemgetter('volume'))
    ether_data.reverse()
    return ether_data

def get_volumes(ether_data):
    volumes = {}
    for item in ether_data:
        volumes[item['market']] = volumes.get(item['market'], 0) + item['volume']
    return volumes


def get_prices(ether_data, volumes):
    prices  = {}
    for item in ether_data:
        prices[item['market']] = prices.get(item['market'], 0) + item['price'] * item['volume'] / volumes[item['market']]
    return prices


def write_to_file(ether_data, volumes, prices):
    plot_data = []
    
    brief = [['market', 'volume', 'price']]
    tmp = sorted(volumes.items(), key=itemgetter(1))
    tmp.reverse()
    for v in tmp:
        brief.append([v[0], v[1], prices[v[0]]])
    plot_data.append(brief)
    
    for item in ether_data:
        tmp = []
        tmp.append(['%s_%s' %(item['market'], item['platform']), 'bids', 'asks'])
        for price in sorted(item['bids']):
            tmp.append([price, item['bids'][price], ''])
        for price in sorted(item['asks']):
            tmp.append([price, '', item['asks'][price]])
        plot_data.append(tmp)
    
    file_data = []
    max_length = max([len(item) for item in plot_data])
    cur = 0
    while cur < max_length:
        line = []
        for item in plot_data:
            line += item[cur] if cur < len(item) else ['', '', '']
        file_data.append(line)
        cur += 1
    
    h = open('/tmp/ether.csv', 'w')
    for l in file_data:
        h.write('%s\n' %', '.join(str(x) for x in l))
    h.close()

ether_data = get_data()
volumes = get_volumes(ether_data)
prices  = get_prices(ether_data, volumes)
write_to_file(ether_data, volumes, prices)
