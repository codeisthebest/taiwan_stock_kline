import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

def main():
    print("歡迎使用台積電 (2330.TW) K 線圖產生器！")
    print("-" * 40)
    
    # 讓使用者輸入日期區間
    start_date = input("請輸入起始日期 (格式 YYYY-MM-DD，例如 2023-01-01): ")
    end_date = input("請輸入結束日期 (格式 YYYY-MM-DD，例如 2023-12-31): ")
    
    print(f"\n正在為您擷取 {start_date} 到 {end_date} 的股價資料，請稍候...")

    try:
        # 使用 yfinance 下載台積電資料
        # 台股代號後面需加上 .TW
        df = yf.download('2330.TW', start=start_date, end=end_date)
        
        # 檢查是否有抓到資料
        if df.empty:
            print("找不到資料。請確認日期格式是否正確，或是該區間是否沒有交易日。")
            return

        # 確保資料格式正確，移除多層索引 (如果 yfinance 版本較新)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)

        # 使用 plotly 建立互動式 K 線圖
        fig = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='K線'
        )])

        # 設定圖表的外觀與標題
        fig.update_layout(
            title=f'台積電 (2330.TW) 股價 K 線圖 ({start_date} ~ {end_date})',
            yaxis_title='股價 (TWD)',
            xaxis_title='日期',
            xaxis_rangeslider_visible=False, # 隱藏底部的範圍滑桿，讓畫面更乾淨
            template='plotly_white'
        )

        # 在瀏覽器中顯示圖表
        fig.show()
        print("圖表已在您的預設瀏覽器中開啟！")

    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    main()
