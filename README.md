# Taiwan Stock K-Line Generator (台灣股市 K線圖產生器)

這是一個輕量級的 Python 腳本，讓使用者只需輸入台灣股票代號與日期區間，即可自動從 Yahoo Finance 抓取股價歷史資料，並繪製出包含成交量的專業 K 線圖。

## 功能特色
* 自動判斷台灣上市 (`.TW`) 與上櫃 (`.TWO`) 股票。
* 採用台灣股市習慣的「紅漲綠跌」配色。
* 結合價格 K線與成交量 (Volume) 顯示。

## 如何使用

1. 安裝所需套件：
   ```bash
   pip install -r requirements.txt
