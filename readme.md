Universal Portfolio Risk Engine

A Multi-Asset Institutional-Style Portfolio Analytics System
Built using Python, Quantitative Finance & Modern Portfolio Theory.

📌 Overview

This project is a Universal Multi-Asset Portfolio Risk Engine that supports:

🇮🇳 Indian Stocks (e.g., RELIANCE.NS)

🇺🇸 US Stocks (AAPL, MSFT)

📊 ETFs (SPY, QQQ)

🪙 Cryptocurrencies (BTC-USD, ETH-USD)

📈 Indian Mutual Funds (via AMFI scheme codes)

The engine performs:

Monte Carlo Simulation

Value at Risk (VaR)

Conditional VaR (CVaR)

Sharpe Ratio

Mean-Variance Optimization

Marginal Risk Contribution

Portfolio Rebalance Suggestion

SELL / REDUCE / KEEP / INCREASE Decision Engine

🧠 Key Features
📊 Risk Modeling

Log return calculation

Covariance matrix estimation

Monte Carlo simulation (5000 scenarios)

1-year forward projection

📉 Risk Metrics

Expected Annual Return

Annual Volatility

Sharpe Ratio

VaR (95%)

CVaR (95%)

📈 Optimization

Mean-Variance (Markowitz) optimization

Minimum variance portfolio

Optimal weight comparison

Deviation from optimal allocation

⚖ Risk Attribution

Marginal Contribution to Risk (MCTR)

Asset-level risk contribution

🤖 Intelligent Recommendation Engine

Based on:

Expected Return

Sharpe Ratio

Optimal weight deviation

Risk contribution

Outputs:

🔴 SELL

🟠 REDUCE

🟡 KEEP

🟢 INCREASE

📂 Project Structure
PortfolioRiskProject/
│
├── portfolio_risk_model.py
├── README.md
├── requirements.txt

⚙ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/PortfolioRiskProject.git
cd PortfolioRiskProject

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶ How to Run
python portfolio_risk_model.py

📝 Example Input
Enter assets: RELIANCE.NS, BTC-USD
Enter weights: 50, 50
Enter investment: 10000

📊 Example Output
Expected Annual Return: 13.37%
Annual Volatility: 37.46%
Sharpe Ratio: 0.36
VaR 95%: ₹6,450
CVaR 95%: ₹5,674

Optimal Weights:
RELIANCE.NS: 88%
BTC-USD: 12%

Recommendation:
RELIANCE.NS → REDUCE
BTC-USD → REDUCE

📚 Methodology

Fetch historical price data:

yfinance for stocks/ETFs/crypto

AMFI API for mutual funds

Compute log returns

Estimate covariance matrix

Run Monte Carlo simulation:

5000 simulated paths

Cholesky decomposition

Optimize portfolio (Markowitz)

Compute:

Risk attribution

Deviation from optimal

Rebalance logic

🎯 Use Cases

Academic final-year project

Portfolio risk evaluation

Robo-advisor prototype

Quantitative finance learning

Asset allocation experimentation

⚠ Limitations

Assumes normal distribution

No regime switching

No transaction costs

No macroeconomic modeling

Historical-data-based predictions

🚀 Future Improvements

Black-Litterman Model

Ledoit-Wolf Shrinkage Covariance

Efficient Frontier Visualization

Walk-forward backtesting

Web Dashboard (FastAPI / Streamlit)

Deployment as REST API

👨‍💻 Author

Bharath Priyan Kumar
Quantitative Finance & Data Science
2026