import os
import time
import ccxt

API_KEY = os.getenv("API_KEY", "YOUR_API_KEY")
API_SECRET = os.getenv("API_SECRET", "YOUR_API_SECRET")

def main():
    print("Bot is starting...")
    
    exchange = ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
    })
    
    while True:
        try:
            ticker = exchange.fetch_ticker('BTC/USDT')
            print(f"BTC Price: {ticker['last']}")
            time.sleep(60)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
