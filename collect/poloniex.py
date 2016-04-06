currencies_url = 'https://poloniex.com/public?command=returnCurrencies'
trade_history  = 'https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_NXT&start=1410158341&end=1410499372'
order_book     = 'http://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_NXT&depth=50'

#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from mysql_conn import MysqlConn

class Orders():
    def __init__(self, conf):
        self.l_db = MysqlConn(conf, 'local')
        self.__init_table()

    def __init_table(self):
        mysql = self.l_db.get_conn()
        cur = mysql.cursor()

        exist_tables = []
        cur.execute("show tables;")
        for line in cur.fetchall():
            exist_tables.append(line[0])

        if 'expense_orders' not in exist_tables:
            cur.execute("""
                    create table expense_orders(
                        order_id int not null primary key,
                        content_type_id int,
                        object_pk mediumint unsigned,
                        user_id int,
                        source_id tinyint unsigned not null,
                        purchase_date timestamp,
                        expiry_date timestamp,
                        price decimal(6,1),
                        gift decimal(6,1),
                        duration smallint unsigned
                );  
                    """)

            init_values = ['content_type_id', 'object_pk', 'user_id', \
                           'order_id', 'source_id', 'purchase_date', 'expiry_date']
            for i in init_values:
                cur.execute('create index idx_expense_orders_%s on expense_orders(%s);' %(i, i))

        mysql.close()

    def get_max_date(self):
        l_mysql = self.l_db.get_conn()
        l_cur = l_mysql.cursor()

        # check local db to make sure which id to start from
        l_cur.execute("select max(purchase_date) from expense_orders;")
        rslt = l_cur.fetchone()[0]
        max_order_date = rslt if rslt else -1
        try:
            l_cur.fetchall()
        except:
            pass
        l_mysql.close()

        return max_order_date


    def update(self, doc):
        """
        doc = [order_id, content_type_id, object_pk, user_id, 
              source_id, purchase_date, expiry_date, price, duration]
        """
        l_mysql = self.l_db.get_conn()
        l_cur = l_mysql.cursor()

        sqlstr = """insert ignore into expense_orders(
                        order_id, content_type_id, object_pk, 
                        user_id, source_id,
                        purchase_date, expiry_date,
                        price, duration)
                        values(%s, %s, %s, %s, %s, '%s', '%s', %s, %s)""" %tuple(doc)
        l_cur.execute(sqlstr)
        l_mysql.close()


    def update_lenovo(self, order_id, cash, gift):
        l_mysql = self.l_db.get_conn()
        l_cur = l_mysql.cursor()
        sqlstr = """update expense_orders 
                    set price = %s, gift = %s, purchase_date = purchase_date, expiry_date = expiry_date 
                    where order_id = %s """ %(cash, gift, order_id)
        l_cur.execute(sqlstr)
        l_mysql.close()
