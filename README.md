# 📈 Stock Market Analysis & Prediction using ARIMA

> A full-stack financial analytics platform that combines **time-series forecasting** (ARIMA), **CAPM return modeling**, and a **real-time market dashboard** — helping investors make data-driven decisions with statistical confidence.

---

## 🎯 Business Problem

Stock market volatility makes investment decisions risky without proper analytical tools. Retail investors and analysts lack access to institutional-grade forecasting systems. This platform democratizes financial analytics by combining statistical modeling (ARIMA), risk assessment (CAPM Beta), and live market data into a single, accessible dashboard — enabling informed decision-making backed by quantitative evidence.

---

## 📊 Results at a Glance

| Metric | Detail |
|---|---|
| Forecasting Model | ARIMA (AutoRegressive Integrated Moving Average) |
| Evaluation Metrics | RMSE, MAE, AIC, BIC, Log Likelihood |
| Market Coverage | Any global stock via Yahoo Finance ticker |
| Database | MongoDB (user data, session management) |
| Stocks Analyzed | Major technology & index stocks |
| Key Module | CAPM Beta & Expected Return Calculator |

---

## 🚀 Key Features

- **User Authentication System** — Secure registration & login with MongoDB credential storage
- **Dynamic Stock Analysis** — Enter any global ticker symbol (AAPL, TSLA, RELIANCE.NS) with custom date ranges
- **Real-Time Market Data** — Live current price, daily delta (color-coded), and last 10 days OHLCV table via `yfinance`
- **ARIMA Forecasting Engine** — Auto-fits ARIMA model to historical prices; overlays actual vs fitted values on interactive Plotly chart
- **Statistical Diagnostics** — AIC, BIC, Log Likelihood scores with plain-English explanations for non-technical users
- **CAPM Module** — Calculates Beta coefficient and Expected Return using Capital Asset Pricing Model
- **Admin Dashboard** — Backend user management panel with MongoDB Compass integration
- **Feedback System** — User feedback collection module integrated into sidebar navigation

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Frontend | Streamlit |
| Statistical Modeling | Statsmodels (ARIMA) |
| Financial Data | yfinance (Yahoo Finance API) |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Database | MongoDB, MongoDB Compass |
| Authentication | Custom session-based login |

---

## 🧠 How It Works

```
User Login / Registration
        │
        ▼
Select Stock Ticker + Date Range
        │
        ▼
yfinance API → Fetch Historical OHLCV Data
        │
        ├──► Real-Time Price Dashboard
        │    (Current Price + Delta + OHLCV Table)
        │
        ├──► ARIMA Model Fitting
        │    (Stationarity Check → Differencing → AR + MA fitting)
        │    → Actual vs Fitted Chart (Plotly)
        │    → AIC / BIC / Log-Likelihood Diagnostics
        │
        └──► CAPM Analysis
             (Beta Calculation → Expected Return Estimation)
```

---

## 📐 Model & Analysis Details

### ARIMA Breakdown

| Component | What It Does |
|---|---|
| **AR (AutoRegression)** | Uses lagged observations — past prices predict future prices |
| **I (Integrated)** | Differencing makes the series stationary (removes trend/seasonality) |
| **MA (Moving Average)** | Models residual errors from lagged moving average terms |

### Model Evaluation Metrics
- **RMSE (Root Mean Squared Error)** — Measures average prediction error in price units
- **MAE (Mean Absolute Error)** — Average absolute deviation between actual and predicted price
- **AIC (Akaike Information Criterion)** — Lower = better model fit with fewer parameters
- **BIC (Bayesian Information Criterion)** — Stricter version of AIC; penalizes model complexity
- **Log Likelihood** — Higher = model explains data variation more effectively

### CAPM Module
```
Beta (β)         = Cov(Stock Returns, Market Returns) / Var(Market Returns)
Expected Return  = Risk-Free Rate + β × (Market Return − Risk-Free Rate)
```
- Beta < 1 → Stock less volatile than market (defensive)
- Beta > 1 → Stock more volatile than market (aggressive)
- Expected Return guides portfolio allocation decisions

---

## 📁 Project Structure

```
Stock-Market-Analysis/
│
├── app.py                    # Main Streamlit application entry point
├── pages/
│   ├── stock_analysis.py     # ARIMA modeling & visualization module
│   ├── capm.py               # CAPM Beta & Return calculator
│   ├── admin.py              # Admin dashboard
│   └── feedback.py           # User feedback module
├── auth/
│   ├── login.py              # User authentication logic
│   └── register.py           # New user registration
├── database/
│   └── mongo_connect.py      # MongoDB connection & CRUD operations
├── utils/
│   ├── fetch_data.py         # yfinance data fetching functions
│   └── arima_model.py        # ARIMA fitting & diagnostics
└── README.md
```

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/your-username/stock-market-analysis.git
cd stock-market-analysis

# Configure MongoDB
# Update mongo_connect.py with your MongoDB connection string
# (Local: mongodb://localhost:27017/ or MongoDB Atlas URI)

# Run the application
streamlit run app.py
```

### Requirements
```
streamlit
pandas
numpy
yfinance
statsmodels
matplotlib
plotly
pymongo
scikit-learn
```

---

## 📈 Sample Analysis — How to Use

1. **Register/Login** with your credentials
2. Navigate to **Stock Analysis** from the sidebar
3. Enter a ticker (e.g., `AAPL`, `TSLA`, `TCS.NS`) and set your date range
4. View **real-time price**, daily change, and OHLCV table
5. Scroll to **ARIMA Modeling** — view fitted vs actual price chart
6. Check **AIC/BIC diagnostics** to evaluate model reliability
7. Navigate to **CAPM Return** to assess risk-adjusted expected returns

---

## 💡 Business Impact & Applications

| Use Case | Impact |
|---|---|
| Retail investors | Quantitative forecasting without Bloomberg terminal access |
| Portfolio managers | Beta-based risk assessment for asset allocation |
| Financial analysts | Rapid multi-stock screening with statistical backing |
| FinTech startups | Ready-to-integrate forecasting API backbone |

---

## 🔮 Future Enhancements

- [ ] Add **Prophet model** for better seasonality handling in stock trends
- [ ] Implement **LSTM-based forecasting** as an alternative to ARIMA for non-linear patterns
- [ ] Build **Portfolio Optimizer** using Modern Portfolio Theory (Markowitz)
- [ ] Add **Sentiment Analysis** on financial news to combine NLP signals with price data
- [ ] Deploy on **AWS / Heroku** with real-time auto-refresh for live trading use cases
- [ ] Export reports as **PDF** for client presentations

---

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

*Built to make institutional-grade financial analysis accessible to everyone.*
