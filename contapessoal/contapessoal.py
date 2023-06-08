import yfinance as yf
from datetime import datetime
from db.conn import *

#stock = yf.Ticker("WEGE3.SA")

#print(stock.info)
dt = datetime.now()
hour = int(dt.strftime("%H"))
open_market = 0
if hour >= 9 and hour <= 17:
    print("\n[Open Market]: Get data yahoo finance\n-------------------------------------")
    open_market = 1
else:
    print("\n[Close Market]: Get data offline database\n-----------------------------------------")

sql = """
with cte_stock as(
    select * from stock s join stock_price sp on (s.id = sp.id_stock) 
    --where s.id = 20
), cte_orders as (
select 
    s.id as id, 
    sum(quantity) as qtde,
    sum(quantity * o.price) as total,
    round(sum(quantity * o.price)/sum(quantity),2) as pm
  from orders o 
  join stock s on (o.id_stock=s.id) 
 group by s.id
)
select 
      o.id,
      s.symbol,
      o.qtde,
      trunc(o.total, 2) AS total_investido,
      trunc(o.qtde * s.price, 2) as total_mercado,
      trunc(o.pm, 2) AS preco_medio,
      trunc(s.price, 2) AS preco_mercado,
      o.qtde * s.price - o.total AS saldo
 from cte_stock s 
 join cte_orders o using (id)
;
"""
#.format(stock.info["symbol"])
stocks = fetch_psql(sql)



for r in stocks:
    id = r[0]
    ticker = r[1]
    qtd = r[2]
    total = r[3]
    total_market = r[4]
    pm = r[5]
    price = r[6]
    result = r[7]
    data_output = "\nId: {} Ticker: {} Qtd: {} Total: {} Total Market: {} PM: {} Price: {} Result: {}".format(id, ticker, qtd, total, total_market, pm, price, result)
    # print(stock)
    if open_market == 0:
        print(data_output)
    else:
        # import pdb; pdb.set_trace()
        stock = yf.Ticker(ticker)
        price = stock.info["currentPrice"]
        total_market = qtd * price
        result = (qtd * price) - float(total)
        print(data_output)

print("\n\nDone!\n")