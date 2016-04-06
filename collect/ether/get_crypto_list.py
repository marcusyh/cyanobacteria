from urllib.request import urlopen
from htmldom import htmldom

def analysis_single(dom):
    coin = []
    for tr in dom.children:
        value = tr.getText().replace('\\n', '').strip()
        if not value:
            continue
        coin.append(value)
    return coin

conn = urlopen("http://coinmarketcap.com/currencies/views/all/")
html = conn.read()
conn.close()

dom = htmldom.HtmlDom()
dom.parseHTML(str(html))
src = dom.find('table#currencies-all>tbody>tr').toList()
for item in src:
    coin = []
    for tr in item.children:
        value = tr.getText().replace('\\n', '').strip()
        if not value:
            continue
        coin.append(value)
    print(coin)

