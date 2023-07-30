import datetime
import streamlit as st
import yfinance as yf

st.write("""
# Stock Price Analyser """)

# get data for Apple's Stock
symbol = st.selectbox("How would you like to be contacted?", ('AAPL', 'NFLX', 'NVDA'))

col1, col2 = st.columns(2)

with col1:
    startDate = st.date_input("Start Date", datetime.datetime(2019, 7, 6))

with col2:
    endDate = st.date_input("End Date", datetime.datetime(2019, 7, 10))

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d", start=startDate, end=endDate)

st.write(f"""
### {symbol}'s Stock Price Data """)
st.dataframe(ticker_df)  # shows the data table

st.write(f"""
### {symbol}'s Closing Price Chart """)
st.line_chart(ticker_df["Close"])  # shows line chart for closing price
