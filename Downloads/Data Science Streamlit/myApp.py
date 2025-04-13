import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App
         
Shown are the **stock closing price** and **volume of Apple**!

""")

# Define the ticker symbol
tickerSymbol = 'AAPL'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2025-3-31')
# Open High  Low Close  Volume Dividends  Stock Splits

st.write("""
         ## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
         ## Volume Price
""")
st.line_chart(tickerDf.Volume)

import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(
    x=tickerDf.index,
    open=tickerDf['Open'],
    high=tickerDf['High'],
    low=tickerDf['Low'],
    close=tickerDf['Close']
)])
st.plotly_chart(fig)



