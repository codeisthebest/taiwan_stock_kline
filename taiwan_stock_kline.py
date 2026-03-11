import yfinance as yf
import mplfinance as mpf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker_input, start_date, end_date):
    """
    抓取台灣股票資料。自動判斷並處理上市 (.TW) 與上櫃 (.TWO) 代號。
    """
    ticker = ticker_input.strip()
    
    # 如果使用者只輸入數字，自動嘗試上市或上櫃後綴
    if ticker.isdigit():
        print(f"正在嘗試抓取上市股票 {ticker}.TW ...")
        df = yf.download(f"{ticker}.TW", start=start_date, end=end_date)
        
        if df.empty:
            print(f"找不到上市資料，正在嘗試抓取上櫃股票 {ticker}.TWO ...")
            df = yf.download(f"{ticker}.TWO", start=start_date, end=end_date)
            ticker_used = f"{ticker}.TWO"
        else:
            ticker_used = f"{ticker}.TW"
    else:
        # 如果使用者已經輸入完整代號 (包含英文字母)
        df = yf.download(ticker, start=start_date, end=end_date)
        ticker_used = ticker

    return df, ticker_used

def plot_kline(df, ticker, start, end):
    """
    使用 mplfinance 繪製 K線圖與成交量
    """
    if df.empty:
        print("警告：該區間沒有找到任何股價資料，請確認代號或日期是否正確。")
        return

    # 設定 K線圖的樣式 (使用類似 Yahoo Finance 的經典配色)
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True) # 台灣股市習慣紅漲綠跌
    s  = mpf.make_mpf_style(marketcolors=mc)

    print(f"正在繪製 {ticker} 從 {start} 到 {end} 的 K線圖...")
    
    # 繪製圖表
    mpf.plot(df, 
             type='candle',       # K線圖
             style=s,             # 自訂紅漲綠跌樣式
             title=f"Stock: {ticker}",
             ylabel='Price (TWD)',
             volume=True,         # 顯示成交量
             ylabel_lower='Volume')

def main():
    print("=== 台灣股市 K線圖產生器 ===")
    ticker_input = input("請輸入股票代號 (例如: 2330 或 0050): ")
    start_date = input("請輸入起始日期 (格式 YYYY-MM-DD，例如 2023-01-01): ")
    end_date = input("請輸入結束日期 (格式 YYYY-MM-DD，例如 2023-12-31): ")

    # 基礎的防呆機制，若未輸入日期則給予預設值
    if not start_date:
        start_date = "2023-01-01"
    if not end_date:
        end_date = datetime.today().strftime('%Y-%m-%d')

    # 抓取資料
    df, actual_ticker = fetch_stock_data(ticker_input, start_date, end_date)
    
    # 畫圖
    
    plot_kline(df, actual_ticker, start_date, end_date)

if __name__ == "__main__":
    main()
