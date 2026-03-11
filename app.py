import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 設定網頁標題與佈局
st.set_page_config(page_title="台積電股價查詢", layout="centered")
st.title("📈 台積電 (2330.TW) 股價查詢系統")

# 側邊欄：設定查詢條件
st.sidebar.header("設定日期區間")
today = datetime.today()
default_start = today - timedelta(days=180) # 預設顯示過去半年

start_date = st.sidebar.date_input("開始日期", default_start)
end_date = st.sidebar.date_input("結束日期", today)

# 邏輯檢查：確保日期正確
if start_date > end_date:
    st.error("錯誤：結束日期必須大於或等於開始日期！")
else:
    # 顯示目前查詢狀態
    st.write(f"目前顯示區間：**{start_date}** 至 **{end_date}**")

    # 擷取資料並加入載入動畫
    with st.spinner('正在從 Yahoo Finance 擷取資料...'):
        # 2330.TW 是台積電在 Yahoo Finance 的台股代號
        df = yf.download("2330.TW", start=start_date, end=end_date)

    if not df.empty:
        # 取出收盤價
        close_price = df['Close']
        
        # 繪製折線圖
        st.line_chart(close_price)
        
        # 展開查看詳細數據
        with st.expander("查看詳細歷史數據"):
            # 將日期反向排序，讓最新的資料在最上面
            st.dataframe(df.sort_index(ascending=False))
    else:
        st.warning("這個日期區間查無資料，請嘗試調整日期（例如避開未開盤的假日）。")
