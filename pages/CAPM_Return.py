# importing libraries
import streamlit as st
import datetime
import pandas as pd
import yfinance as yf
from pages.utils import capm_functions

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Calculate Beta",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

st.title('Capital Asset Pricing Model 📈')

# ---------------- USER INPUT ----------------
col1, col2 = st.columns([1,1])
with col1:
    stocks_list = st.multiselect(
        "Choose 4 Stocks",
        ('TSLA','AAPL','NFLX','MGM','MSFT','AMZN','NVDA','GOOGL'),
        ['TSLA','AAPL','MSFT','NFLX']
    )
with col2:
    year = st.number_input("Number of Years",1,10)

try:
    # ---------------- DATE RANGE ----------------
    end = datetime.date.today()
    start = datetime.date(end.year - year, end.month, end.day)

    # ---------------- FETCH S&P500 ----------------
    sp500_data = yf.download("^GSPC", start=start, end=end)

    # 🔥 FIX 1: Flatten columns
    sp500_data.columns = sp500_data.columns.get_level_values(0)

    sp500_df = sp500_data[['Close']].rename(columns={'Close': 'sp500'})

    # ---------------- FETCH STOCKS ----------------
    stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data = yf.download(stock, start=start, end=end)

        # flatten columns
        data.columns = data.columns.get_level_values(0)

        stocks_df[stock] = data['Close']

    # ---------------- MERGE ----------------
    stocks_df = pd.merge(stocks_df, sp500_df, left_index=True, right_index=True)

    # 🔥 FIX 2: Remove NaN
    stocks_df = stocks_df.dropna()

    stocks_df.reset_index(inplace=True)

    # ---------------- SHOW DATA ----------------
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('### Dataframe head')
        st.dataframe(stocks_df.head(), use_container_width=True)

    with col2:
        st.markdown('### Dataframe tail')
        st.dataframe(stocks_df.tail(), use_container_width=True)

    # ---------------- PLOTS ----------------
    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('### Price of all the Stocks')
        st.plotly_chart(capm_functions.interactive_plot(stocks_df), use_container_width=True)

    with col2:
        st.markdown('### Price of all the Stocks (After Normalizing)')
        st.plotly_chart(
            capm_functions.interactive_plot(capm_functions.normalize(stocks_df)),
            use_container_width=True
        )

    # ---------------- DAILY RETURNS ----------------
    stocks_daily_return = capm_functions.daily_return(stocks_df)

    # 🔥 FIX 3: Remove NaN
    stocks_daily_return = stocks_daily_return.dropna()

    beta = {}
    alpha = {}

    # ---------------- CALCULATE BETA ----------------
    for i in stocks_daily_return.columns:
        if i != 'Date' and i != 'sp500':

            # 🔥 FIX 4: Ensure 1D
            stocks_daily_return['sp500'] = stocks_daily_return['sp500'].values.flatten()
            stocks_daily_return[i] = stocks_daily_return[i].values.flatten()

            b, a = capm_functions.calculate_beta(stocks_daily_return, i)

            beta[i] = b
            alpha[i] = a

    # ---------------- BETA TABLE ----------------
    col1, col2 = st.columns([1,1])

    beta_df = pd.DataFrame({
        'Stock': list(beta.keys()),
        'Beta Value': [round(i, 2) for i in beta.values()]
    })

    with col1:
        st.markdown('### Calculated Beta Value')
        st.dataframe(beta_df, use_container_width=True)

    # ---------------- CAPM RETURN ----------------
    rf = 0
    rm = stocks_daily_return['sp500'].mean() * 252

    return_df = pd.DataFrame({
        'Stock': list(beta.keys()),
        'Return Value': [round(rf + (value * (rm - rf)), 2) for value in beta.values()]
    })

    with col2:
        st.markdown('### Calculated Return using CAPM')
        st.dataframe(return_df, use_container_width=True)

except Exception as e:
    st.error("Something went wrong. Please check inputs.")
    st.write(e)