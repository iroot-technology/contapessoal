import yfinance as yf
from db.conn import insert_psql
#import pdb; pdb.set_trace()

#slist = ["RRRP3.SA", "ALSO3.SA", "ALPA4.SA"]
slist = ["RRRP3.SA","ALSO3.SA","ALPA4.SA","ABEV3.SA","ARZZ3.SA","ASAI3.SA","AZUL4.SA","B3SA3.SA","BBSE3.SA","BBDC3.SA","BBDC4.SA","BRAP4.SA","BBAS3.SA","BRKM5.SA","BRFS3.SA","BPAC11.SA","CRFB3.SA","CCRO3.SA","CMIG4.SA","CIEL3.SA","COGN3.SA","CPLE6.SA","CSAN3.SA","CPFE3.SA","CMIN3.SA","CVCB3.SA","CYRE3.SA","DXCO3.SA","ELET3.SA","ELET6.SA","EMBR3.SA","ENBR3.SA","ENGI11.SA","ENEV3.SA","EGIE3.SA","EQTL3.SA","EZTC3.SA","FLRY3.SA","GGBR4.SA","GOAU4.SA","GOLL4.SA","NTCO3.SA","SOMA3.SA","HAPV3.SA","HYPE3.SA","IGTI11.SA","IRBR3.SA","ITSA4.SA","ITUB4.SA","JBSS3.SA","KLBN11.SA","RENT3.SA","LWSA3.SA","LREN3.SA","MGLU3.SA","MRFG3.SA","CASH3.SA","BEEF3.SA","MRVE3.SA","MULT3.SA","PCAR3.SA","PETR3.SA","PETR4.SA","PRIO3.SA","PETZ3.SA","RADL3.SA","RAIZ4.SA","RDOR3.SA","RAIL3.SA","SBSP3.SA","SANB11.SA","SMTO3.SA","CSNA3.SA","SLCE3.SA","SUZB3.SA","TAEE11.SA","VIVT3.SA","TIMS3.SA","TOTS3.SA","UGPA3.SA","USIM5.SA","VALE3.SA","VIIA3.SA","VBBR3.SA","WEGE3.SA","YDUQ3.SA"]

#slist = ["RRRP3.SA", "ALSO3.SA", "ALPA4.SA"]

for st in slist:
    #print(type(st))
    stock = yf.Ticker(st)
    sql = "DELETE FROM stock_price WHERE id_stock = (SELECT id FROM stock WHERE symbol = '{}') RETURNING id_stock;".format(stock.info["symbol"])
    _stock_id = insert_psql(sql)
    sql = "DELETE FROM stock WHERE id = (SELECT id FROM stock WHERE symbol = '{}') RETURNING id;".format(stock.info["symbol"])
    _stock_id = insert_psql(sql)
    print(stock.info["symbol"])
    sql = "INSERT INTO stock (symbol,name,currency,website) VALUES ('{}','{}','{}','{}') returning id;".format(stock.info["symbol"],stock.info["longName"].replace("'","''"),stock.info["currency"], stock.info["website"])
    print(sql)
    _stock_id = insert_psql(sql)
    sql = "INSERT INTO stock_price (id_stock,price,open,low,high,bid,ask) VALUES ({},{},{},{},{},{},{}) returning id_stock;".format(_stock_id,stock.info["currentPrice"],stock.info["open"],stock.info["dayLow"], stock.info["dayHigh"],stock.info["bid"], stock.info["ask"])
    print(sql)
    _stock_id_price = insert_psql(sql)

