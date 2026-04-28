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

## 📂 Data Source
Live data fetched via **yfinance** API — no dataset download needed.

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/Niya3-Navya/stock-market-analysis.git
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

## 📸 App Screenshots
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/af0a2458-d122-4ae1-bcb2-4013020ed106" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/8f5c2947-667e-4188-a266-131d4cbbd91f" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/5bdc7596-1e79-4626-a091-0fa33953b94a" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/cbfd474a-ae18-4433-be56-9122672016a4" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/0d231aac-0fce-4056-8154-90ae0413ee48" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/2cbddecb-5987-4618-9943-5d5a03958ff8" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/5625a6a3-68de-4400-bbac-3134b724b648" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/6f56d349-5460-4053-b920-8852a3e2af3a" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/e58d70b0-e772-4aa7-bf62-4c306f1da6a5" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/57fe39d8-e6d7-44ee-94b7-ee10266a6a9a" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/530f7031-a148-4a8d-a163-0cb1088deb6d" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/e479d42f-7333-4add-aef5-2580d227a8bb" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/4385105f-4fba-492b-ab37-328835631eae" />
<img width="768" height="432" alt="image" src="https://github.com/user-attachments/assets/2b59eba7-7196-4a3f-b08f-18fccb4149c9" />

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
