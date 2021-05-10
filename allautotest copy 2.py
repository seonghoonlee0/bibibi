import time
import pyupbit
import datetime

access = "xhySnaRtv3EYW6QC3b7Zwo888a5cc8h0SXqUTE7M"
secret = "8gxbf9Ra5GhbFS86JWnXSYHmxm0rg3xrgyIwprWi"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        boc = 25000  #코인 1개당 구매할 금액 입력

# BTC 시작
        if get_balance("BTC") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-BTC", 0.2)
                current_price = get_current_price("KRW-BTC")
                high = pyupbit.get_ohlcv("KRW-BTC").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-BTC", boc*0.9995)
    
        else:
            btc = get_balance("BTC")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-BTC")
                high = pyupbit.get_ohlcv("KRW-BTC").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-BTC", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
            time.sleep(1)
# 여기까지

# ETH 시작
        if get_balance("ETH") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-ETH", 0.2)
                current_price = get_current_price("KRW-ETH")
                high = pyupbit.get_ohlcv("KRW-ETH").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-ETH", boc*0.9995)
    
        else:
            btc = get_balance("ETH")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-ETH")
                high = pyupbit.get_ohlcv("KRW-ETH").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-ETH", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-ETH", btc*0.9995)
            time.sleep(1)
# 여기까지

# NEO 시작
        if get_balance("NEO") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-NEO", 0.2)
                current_price = get_current_price("KRW-NEO")
                high = pyupbit.get_ohlcv("KRW-NEO").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-NEO", boc*0.9995)
    
        else:
            btc = get_balance("NEO")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-NEO")
                high = pyupbit.get_ohlcv("KRW-NEO").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-NEO", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-NEO", btc*0.9995)
            time.sleep(1)
# 여기까지

# MTL 시작
        if get_balance("MTL") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-MTL", 0.2)
                current_price = get_current_price("KRW-MTL")
                high = pyupbit.get_ohlcv("KRW-MTL").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-MTL", boc*0.9995)
    
        else:
            btc = get_balance("MTL")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-MTL")
                high = pyupbit.get_ohlcv("KRW-MTL").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-MTL", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-MTL", btc*0.9995)
            time.sleep(1)
# 여기까지

# LTC 시작
        if get_balance("LTC") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-LTC", 0.2)
                current_price = get_current_price("KRW-LTC")
                high = pyupbit.get_ohlcv("KRW-LTC").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-LTC", boc*0.9995)
    
        else:
            btc = get_balance("LTC")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-LTC")
                high = pyupbit.get_ohlcv("KRW-LTC").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-LTC", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-LTC", btc*0.9995)
            time.sleep(1)
# 여기까지

# XRP 시작
        if get_balance("XRP") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-XRP", 0.2)
                current_price = get_current_price("KRW-XRP")
                high = pyupbit.get_ohlcv("KRW-XRP").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-XRP", boc*0.9995)
    
        else:
            btc = get_balance("XRP")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-XRP")
                high = pyupbit.get_ohlcv("KRW-XRP").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-XRP", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-XRP", btc*0.9995)
            time.sleep(1)
# 여기까지

# ETC 시작
        if get_balance("ETC") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-ETC", 0.2)
                current_price = get_current_price("KRW-ETC")
                high = pyupbit.get_ohlcv("KRW-ETC").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-ETC", boc*0.9995)
    
        else:
            btc = get_balance("ETC")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-ETC")
                high = pyupbit.get_ohlcv("KRW-ETC").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-ETC", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-ETC", btc*0.9995)
            time.sleep(1)
# 여기까지

# OMG 시작
        if get_balance("OMG") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-OMG", 0.2)
                current_price = get_current_price("KRW-OMG")
                high = pyupbit.get_ohlcv("KRW-OMG").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-OMG", boc*0.9995)
    
        else:
            btc = get_balance("OMG")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-OMG")
                high = pyupbit.get_ohlcv("KRW-OMG").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-OMG", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-OMG", btc*0.9995)
            time.sleep(1)
# 여기까지

# SNT 시작
        if get_balance("SNT") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-SNT", 0.2)
                current_price = get_current_price("KRW-SNT")
                high = pyupbit.get_ohlcv("KRW-SNT").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-SNT", boc*0.9995)
    
        else:
            btc = get_balance("SNT")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-SNT")
                high = pyupbit.get_ohlcv("KRW-SNT").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-SNT", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-SNT", btc*0.9995)
            time.sleep(1)
# 여기까지

# WAVES 시작
        if get_balance("WAVES") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-WAVES", 0.2)
                current_price = get_current_price("KRW-WAVES")
                high = pyupbit.get_ohlcv("KRW-WAVES").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-WAVES", boc*0.9995)
    
        else:
            btc = get_balance("WAVES")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-WAVES")
                high = pyupbit.get_ohlcv("KRW-WAVES").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-WAVES", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-WAVES", btc*0.9995)
            time.sleep(1)
# 여기까지

# XEM 시작
        if get_balance("XEM") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-XEM", 0.2)
                current_price = get_current_price("KRW-XEM")
                high = pyupbit.get_ohlcv("KRW-XEM").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-XEM", boc*0.9995)
    
        else:
            btc = get_balance("XEM")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-XEM")
                high = pyupbit.get_ohlcv("KRW-XEM").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-XEM", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-XEM", btc*0.9995)
            time.sleep(1)
# 여기까지

# QTUM 시작
        if get_balance("QTUM") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-QTUM", 0.2)
                current_price = get_current_price("KRW-QTUM")
                high = pyupbit.get_ohlcv("KRW-QTUM").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-QTUM", boc*0.9995)
    
        else:
            btc = get_balance("QTUM")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-QTUM")
                high = pyupbit.get_ohlcv("KRW-QTUM").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-QTUM", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-QTUM", btc*0.9995)
            time.sleep(1)
# 여기까지

# LSK 시작
        if get_balance("LSK") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-LSK", 0.2)
                current_price = get_current_price("KRW-LSK")
                high = pyupbit.get_ohlcv("KRW-LSK").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-LSK", boc*0.9995)
    
        else:
            btc = get_balance("LSK")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-LSK")
                high = pyupbit.get_ohlcv("KRW-LSK").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-LSK", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-LSK", btc*0.9995)
            time.sleep(1)
# 여기까지

# STEEM 시작
        if get_balance("STEEM") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-STEEM", 0.2)
                current_price = get_current_price("KRW-STEEM")
                high = pyupbit.get_ohlcv("KRW-STEEM").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-STEEM", boc*0.9995)
    
        else:
            btc = get_balance("STEEM")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-STEEM")
                high = pyupbit.get_ohlcv("KRW-STEEM").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-STEEM", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-STEEM", btc*0.9995)
            time.sleep(1)
# 여기까지

# XLM 시작
        if get_balance("XLM") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-XLM", 0.2)
                current_price = get_current_price("KRW-XLM")
                high = pyupbit.get_ohlcv("KRW-XLM").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-XLM", boc*0.9995)
    
        else:
            btc = get_balance("XLM")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-XLM")
                high = pyupbit.get_ohlcv("KRW-XLM").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-XLM", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-XLM", btc*0.9995)
            time.sleep(1)
# 여기까지

# ARDR 시작
        if get_balance("ARDR") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-ARDR", 0.2)
                current_price = get_current_price("KRW-ARDR")
                high = pyupbit.get_ohlcv("KRW-ARDR").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-ARDR", boc*0.9995)
    
        else:
            btc = get_balance("ARDR")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-ARDR")
                high = pyupbit.get_ohlcv("KRW-ARDR").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-ARDR", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-ARDR", btc*0.9995)
            time.sleep(1)
# 여기까지

# KMD 시작
        if get_balance("KMD") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-KMD", 0.2)
                current_price = get_current_price("KRW-KMD")
                high = pyupbit.get_ohlcv("KRW-KMD").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-KMD", boc*0.9995)
    
        else:
            btc = get_balance("KMD")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-KMD")
                high = pyupbit.get_ohlcv("KRW-KMD").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-KMD", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-KMD", btc*0.9995)
            time.sleep(1)
# 여기까지

# ARK 시작
        if get_balance("ARK") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-ARK", 0.2)
                current_price = get_current_price("KRW-ARK")
                high = pyupbit.get_ohlcv("KRW-ARK").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-ARK", boc*0.9995)
    
        else:
            btc = get_balance("ARK")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-ARK")
                high = pyupbit.get_ohlcv("KRW-ARK").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-ARK", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-ARK", btc*0.9995)
            time.sleep(1)
# 여기까지

# STORJ 시작
        if get_balance("STORJ") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-STORJ", 0.2)
                current_price = get_current_price("KRW-STORJ")
                high = pyupbit.get_ohlcv("KRW-STORJ").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-STORJ", boc*0.9995)
    
        else:
            btc = get_balance("STORJ")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-STORJ")
                high = pyupbit.get_ohlcv("KRW-STORJ").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-STORJ", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-STORJ", btc*0.9995)
            time.sleep(1)
# 여기까지

# GRS 시작
        if get_balance("GRS") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-GRS", 0.2)
                current_price = get_current_price("KRW-GRS")
                high = pyupbit.get_ohlcv("KRW-GRS").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-GRS", boc*0.9995)
    
        else:
            btc = get_balance("GRS")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-GRS")
                high = pyupbit.get_ohlcv("KRW-GRS").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-GRS", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-GRS", btc*0.9995)
            time.sleep(1)
# 여기까지

# REP 시작
        if get_balance("REP") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-REP", 0.2)
                current_price = get_current_price("KRW-REP")
                high = pyupbit.get_ohlcv("KRW-REP").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-REP", boc*0.9995)
    
        else:
            btc = get_balance("REP")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-REP")
                high = pyupbit.get_ohlcv("KRW-REP").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-REP", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-REP", btc*0.9995)
            time.sleep(1)
# 여기까지

# EMC2 시작
        if get_balance("EMC2") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-EMC2", 0.2)
                current_price = get_current_price("KRW-EMC2")
                high = pyupbit.get_ohlcv("KRW-EMC2").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-EMC2", boc*0.9995)
    
        else:
            btc = get_balance("EMC2")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-EMC2")
                high = pyupbit.get_ohlcv("KRW-EMC2").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-EMC2", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-EMC2", btc*0.9995)
            time.sleep(1)
# 여기까지

# ADA 시작
        if get_balance("ADA") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-ADA", 0.2)
                current_price = get_current_price("KRW-ADA")
                high = pyupbit.get_ohlcv("KRW-ADA").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-ADA", boc*0.9995)
    
        else:
            btc = get_balance("ADA")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-ADA")
                high = pyupbit.get_ohlcv("KRW-ADA").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-ADA", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-ADA", btc*0.9995)
            time.sleep(1)
# 여기까지

# SBD 시작
        if get_balance("SBD") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-SBD", 0.2)
                current_price = get_current_price("KRW-SBD")
                high = pyupbit.get_ohlcv("KRW-SBD").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-SBD", boc*0.9995)
    
        else:
            btc = get_balance("SBD")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-SBD")
                high = pyupbit.get_ohlcv("KRW-SBD").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-SBD", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-SBD", btc*0.9995)
            time.sleep(1)
# 여기까지

# POWR 시작
        if get_balance("POWR") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-POWR", 0.2)
                current_price = get_current_price("KRW-POWR")
                high = pyupbit.get_ohlcv("KRW-POWR").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-POWR", boc*0.9995)
    
        else:
            btc = get_balance("POWR")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-POWR")
                high = pyupbit.get_ohlcv("KRW-POWR").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-POWR", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-POWR", btc*0.9995)
            time.sleep(1)
# 여기까지

# BTG 시작
        if get_balance("BTG") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-BTG", 0.2)
                current_price = get_current_price("KRW-BTG")
                high = pyupbit.get_ohlcv("KRW-BTG").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-BTG", boc*0.9995)
    
        else:
            btc = get_balance("BTG")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-BTG")
                high = pyupbit.get_ohlcv("KRW-BTG").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-BTG", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-BTG", btc*0.9995)
            time.sleep(1)
# 여기까지

# ICX 시작
        if get_balance("ICX") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-ICX", 0.2)
                current_price = get_current_price("KRW-ICX")
                high = pyupbit.get_ohlcv("KRW-ICX").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-ICX", boc*0.9995)
    
        else:
            btc = get_balance("ICX")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-ICX")
                high = pyupbit.get_ohlcv("KRW-ICX").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-ICX", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-ICX", btc*0.9995)
            time.sleep(1)
# 여기까지

# EOS 시작
        if get_balance("EOS") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-EOS", 0.2)
                current_price = get_current_price("KRW-EOS")
                high = pyupbit.get_ohlcv("KRW-EOS").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-EOS", boc*0.9995)
    
        else:
            btc = get_balance("EOS")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-EOS")
                high = pyupbit.get_ohlcv("KRW-EOS").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-EOS", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-EOS", btc*0.9995)
            time.sleep(1)
# 여기까지

# TRX 시작
        if get_balance("TRX") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-TRX", 0.2)
                current_price = get_current_price("KRW-TRX")
                high = pyupbit.get_ohlcv("KRW-TRX").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-TRX", boc*0.9995)
    
        else:
            btc = get_balance("TRX")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-TRX")
                high = pyupbit.get_ohlcv("KRW-TRX").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-TRX", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-TRX", btc*0.9995)
            time.sleep(1)
# 여기까지

# TRX 시작
        if get_balance("TRX") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-TRX", 0.2)
                current_price = get_current_price("KRW-TRX")
                high = pyupbit.get_ohlcv("KRW-TRX").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-TRX", boc*0.9995)
    
        else:
            btc = get_balance("TRX")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-TRX")
                high = pyupbit.get_ohlcv("KRW-TRX").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-TRX", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-TRX", btc*0.9995)
            time.sleep(1)
# 여기까지

# SC 시작
        if get_balance("SC") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-SC", 0.2)
                current_price = get_current_price("KRW-SC")
                high = pyupbit.get_ohlcv("KRW-SC").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-SC", boc*0.9995)
    
        else:
            btc = get_balance("SC")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-SC")
                high = pyupbit.get_ohlcv("KRW-SC").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-SC", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-SC", btc*0.9995)
            time.sleep(1)
# 여기까지

# IGNIS 시작
        if get_balance("IGNIS") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-IGNIS", 0.2)
                current_price = get_current_price("KRW-IGNIS")
                high = pyupbit.get_ohlcv("KRW-IGNIS").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-IGNIS", boc*0.9995)
    
        else:
            btc = get_balance("IGNIS")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-IGNIS")
                high = pyupbit.get_ohlcv("KRW-IGNIS").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-IGNIS", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-IGNIS", btc*0.9995)
            time.sleep(1)
# 여기까지

# BCH 시작
        if get_balance("BCH") == None:
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                target_price = get_target_price("KRW-BCH", 0.2)
                current_price = get_current_price("KRW-BCH")
                high = pyupbit.get_ohlcv("KRW-BCH").iloc[-1]["high"]
                if target_price < current_price:
                    if current_price > 0.995*high:
                        if get_balance("KRW") > boc:
                            upbit.buy_market_order("KRW-BCH", boc*0.9995)
    
        else:
            btc = get_balance("BCH")
            if start_time < now < end_time - datetime.timedelta(minutes=10):
                current_price = get_current_price("KRW-BCH")
                high = pyupbit.get_ohlcv("KRW-BCH").iloc[-1]["high"]

                if current_price < 0.98*high:
                    upbit.sell_market_order("KRW-BCH", btc*0.9995)

            else:
                upbit.sell_market_order("KRW-BCH", btc*0.9995)
            time.sleep(1)
# 여기까지

    except Exception as e:
        print(e)
        time.sleep(1)
