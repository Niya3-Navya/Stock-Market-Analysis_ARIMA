# importing libraries
import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
from pages.utils import capm_functions
import numpy as np
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CAPM",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

st.title('Calculate Beta and Return for individual stock')

# ---------------- USER INPUT ----------------
col1, col2 = st.columns([1,1])
with col1:
    stock = st.selectbox("Choose a stock", ('AAPL','TSLA','NFLX','MGM','MSFT','AMZN','NVDA','GOOGL'))
with col2:
    year = st.number_input("Number of Years", 1, 10)

# ---------------- DATE RANGE ----------------
end = datetime.date.today()
start = datetime.date(end.year - year, end.month, end.day)

# ---------------- DATA FETCH ----------------
stock_data = yf.download(stock, start=start, end=end)
sp500_data = yf.download("^GSPC", start=start, end=end)

# 🔥 FIX 1: Flatten columns (important)
stock_data.columns = stock_data.columns.get_level_values(0)
sp500_data.columns = sp500_data.columns.get_level_values(0)

# ---------------- DATA PREPARATION ----------------
stock_df = stock_data[['Close']].rename(columns={'Close': stock})
sp500_df = sp500_data[['Close']].rename(columns={'Close': 'sp500'})

# merge both datasets
stocks_df = pd.merge(stock_df, sp500_df, left_index=True, right_index=True)

# 🔥 FIX 2: Remove missing values
stocks_df = stocks_df.dropna()

# reset index
stocks_df.reset_index(inplace=True)

# ---------------- DAILY RETURNS ----------------
stocks_daily_return = capm_functions.daily_return(stocks_df)

# 🔥 FIX 3: Remove NaN again after returns
stocks_daily_return = stocks_daily_return.dropna()

# 🔥 FIX 4: Ensure 1D arrays
stocks_daily_return['sp500'] = stocks_daily_return['sp500'].values.flatten()
stocks_daily_return[stock] = stocks_daily_return[stock].values.flatten()

# ---------------- CALCULATIONS ----------------
rm = stocks_daily_return['sp500'].mean() * 252

beta, alpha = capm_functions.calculate_beta(stocks_daily_return, stock)

# risk free rate
rf = 0

# expected return
return_value = round(rf + (beta * (rm - rf)), 2)

# ---------------- OUTPUT ----------------
st.markdown(f'### Beta : {round(beta, 4)}')
st.markdown(f'### Expected Return : {return_value}')

# ---------------- PLOT ----------------
fig = px.scatter(
    stocks_daily_return,
    x='sp500',
    y=stock,
    title=f'{stock} vs Market (CAPM)'
)

# regression line
fig.add_scatter(
    x=stocks_daily_return['sp500'],
    y=beta * stocks_daily_return['sp500'] + alpha,
    name='Expected Return Line',
    line=dict(color="crimson")
)

st.plotly_chart(fig, use_container_width=True)