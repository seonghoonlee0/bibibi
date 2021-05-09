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

# BTC 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("BTC") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-BTC", 0.2)
                    current_price = get_current_price("KRW-BTC")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-BTC", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("BTC") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-BTC")
                    open = pyupbit.get_ohlcv("KRW-BTC").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-BTC").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        btc = get_balance("BTC")
                        if btc > 0:
                            upbit.sell_market_order("KRW-BTC", btc*0.9995)
                            count - 1

                else:
                    btc = get_balance("BTC")
                    if btc > 0:
                        upbit.sell_market_order("KRW-BTC", btc*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2

                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# ETH 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("ETH") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-ETH", 0.2)
                    current_price = get_current_price("KRW-ETH")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-ETH", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("ETH") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-ETH")
                    open = pyupbit.get_ohlcv("KRW-ETH").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-ETH").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        eth = get_balance("ETH")
                        if eth > 0:
                            upbit.sell_market_order("KRW-ETH", eth*0.9995)
                            count - 1

                else:
                    eth = get_balance("ETH")
                    if eth > 0:
                        upbit.sell_market_order("KRW-ETH", eth*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# ETC 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETC")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("ETC") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-ETC", 0.2)
                    current_price = get_current_price("KRW-ETC")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-ETC", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("ETC") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-ETC")
                    open = pyupbit.get_ohlcv("KRW-ETC").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-ETC").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        etc = get_balance("ETC")
                        if etc > 0:
                            upbit.sell_market_order("KRW-ETC", etc*0.9995)
                            count - 1

                else:
                    etc = get_balance("ETC")
                    if etc > 0:
                        upbit.sell_market_order("KRW-ETC", etc*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# XRP 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-XRP")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("XRP") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-XRP", 0.2)
                    current_price = get_current_price("KRW-XRP")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-XRP", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("XRP") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-XRP")
                    open = pyupbit.get_ohlcv("KRW-XRP").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-XRP").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        xrp = get_balance("XRP")
                        if xrp > 0:
                            upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                            count - 1

                else:
                    xrp = get_balance("XRP")
                    if xrp > 0:
                        upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# EOS 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-EOS")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("EOS") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-EOS", 0.2)
                    current_price = get_current_price("KRW-EOS")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-EOS", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("EOS") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-EOS")
                    open = pyupbit.get_ohlcv("KRW-EOS").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-EOS").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        eos = get_balance("EOS")
                        if eos > 0:
                            upbit.sell_market_order("KRW-EOS", eos*0.9995)
                            count - 1

                else:
                    eos = get_balance("EOS")
                    if eos > 0:
                        upbit.sell_market_order("KRW-EOS", eos*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# NEO 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-NEO")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("NEO") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-NEO", 0.2)
                    current_price = get_current_price("KRW-NEO")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-NEO", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("NEO") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-NEO")
                    open = pyupbit.get_ohlcv("KRW-NEO").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-NEO").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        neo = get_balance("NEO")
                        if neo > 0:
                            upbit.sell_market_order("KRW-NEO", neo*0.9995)
                            count - 1

                else:
                    neo = get_balance("NEO")
                    if neo > 0:
                        upbit.sell_market_order("KRW-NEO", neo*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# VET 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-VET")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("VET") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-VET", 0.2)
                    current_price = get_current_price("KRW-VET")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-VET", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("VET") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-VET")
                    open = pyupbit.get_ohlcv("KRW-VET").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-VET").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        vet = get_balance("VET")
                        if vet > 0:
                            upbit.sell_market_order("KRW-VET", vet*0.9995)
                            count - 1

                else:
                    vet = get_balance("VET")
                    if vet > 0:
                        upbit.sell_market_order("KRW-VET", vet*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# LSK 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-LSK")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("LSK") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-LSK", 0.2)
                    current_price = get_current_price("KRW-LSK")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-LSK", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("LSK") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-LSK")
                    open = pyupbit.get_ohlcv("KRW-LSK").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-LSK").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        lsk = get_balance("LSK")
                        if lsk > 0:
                            upbit.sell_market_order("KRW-LSK", lsk*0.9995)
                            count - 1

                else:
                    lsk = get_balance("LSK")
                    if lsk > 0:
                        upbit.sell_market_order("KRW-LSK", lsk*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# MTL 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-MTL")
        end_time = start_time + datetime.timedelta(days=1)

        count = 2
        if count == 2:
            if get_balance("MTL") == 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    target_price = get_target_price("KRW-MTL", 0.2)
                    current_price = get_current_price("KRW-MTL")
                    if target_price < current_price:
                        krw = 100000 / 4 / get_balance("KRW") # 총 매입금액 / 매입 코인수 / 현재 잔액
                        if get_balance("KRW") > 5000:
                            upbit.buy_market_order("KRW-MTL", krw*0.9995)
                            count - 1

        elif count == 1:
            if get_balance("MTL") > 0:
                if start_time < now < end_time - datetime.timedelta(minutes=10):
                    current_price = get_current_price("KRW-MTL")
                    open = pyupbit.get_ohlcv("KRW-MTL").iloc[-1]["open"]
                    high = pyupbit.get_ohlcv("KRW-MTL").iloc[-1]["high"]
                    up = (current_price / open) * 100 - 100    # 상승률
                    gap = (0.07 * up) + (3 * current_price)
                    if current_price < high - gap:
                        mtl = get_balance("MTL")
                        if mtl > 0:
                            upbit.sell_market_order("KRW-MTL", mtl*0.9995)
                            count - 1

                else:
                    mtl = get_balance("MTL")
                    if mtl > 0:
                        upbit.sell_market_order("KRW-MTL", mtl*0.9995)
                        count - 1

        elif count == 0:
            if end_time - datetime.temedelta(minutes=10) < now < end_time - datetime.timedelta(minutes=1):
                count + 2
                time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)