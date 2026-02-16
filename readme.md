Portfolio Risk Engine

A Multi-Asset Institutional-Grade Portfolio Analytics System
Built using Python, Quantitative Finance, and Modern Portfolio Theory

Overview

The Universal Portfolio Risk Engine is a quantitative portfolio analytics framework designed to evaluate risk, optimize allocations, and generate intelligent rebalancing recommendations across multiple asset classes.

The system supports:

Indian equities (e.g., RELIANCE.NS)

US equities (AAPL, MSFT)

ETFs (SPY, QQQ)

Cryptocurrencies (BTC-USD, ETH-USD)

Indian mutual funds via AMFI scheme codes

This project integrates statistical modeling, optimization theory, and simulation-based risk analysis into a unified portfolio decision engine.

Core Capabilities
Risk Modeling

Log return calculation

Covariance matrix estimation

Cholesky decomposition

Monte Carlo simulation (5,000 scenarios)

1-year forward projection

Risk Metrics

Expected annual return

Annualized volatility

Sharpe ratio

Value at Risk (95%)

Conditional Value at Risk (95%)

Portfolio Optimization

Mean-Variance (Markowitz) framework

Minimum variance portfolio construction

Optimal weight estimation

Allocation deviation analysis

Risk Attribution

Marginal Contribution to Risk (MCTR)

Asset-level risk contribution

Portfolio-level volatility decomposition

Intelligent Decision Engine

Based on:

Expected return

Risk-adjusted return (Sharpe ratio)

Deviation from optimal allocation

Risk contribution

Outputs structured portfolio actions:

SELL

REDUCE

KEEP

INCREASE

Project Architecture
PortfolioRiskProject/
│
├── portfolio_risk_model.py
├── README.md
├── requirements.txt


The system is modular and can be extended into an API service, dashboard application, or quantitative research framework.

Installation
1. Clone the Repository
git clone https://github.com/your-username/Universal-Portfolio-Risk-Engine.git
cd Universal-Portfolio-Risk-Engine

2. Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

How to Run
python portfolio_risk_model.py

Example Usage

Input:

Enter assets: RELIANCE.NS, BTC-USD
Enter weights: 50, 50
Enter investment: 10000


Sample Output:

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

Methodology

Historical price data retrieval:

yfinance for stocks, ETFs, crypto

AMFI API for mutual funds

Log return computation

Covariance matrix estimation

Monte Carlo simulation:

5,000 correlated return paths

Cholesky factorization

Forward portfolio value projection

Mean-Variance optimization

Risk attribution analysis

Allocation deviation and rebalance logic

Quantitative Foundations

The system is based on:

Modern Portfolio Theory (Harry Markowitz)

Mean-Variance Optimization

Stochastic Monte Carlo Simulation

Parametric VaR estimation

Risk decomposition mathematics

This project demonstrates applied quantitative finance principles in a practical multi-asset setting.

Use Cases

Academic final-year project (Quantitative Finance / Data Science)

Portfolio risk analysis prototype

Robo-advisor decision engine foundation

Asset allocation experimentation

Risk-aware capital allocation modeling

Limitations

Assumes normally distributed returns

No regime-switching volatility modeling

No macroeconomic factor integration

No transaction cost modeling

Historical data–based projections only

This system provides probabilistic risk estimates, not deterministic predictions.

Future Enhancements

Black-Litterman model integration

Ledoit-Wolf shrinkage covariance estimator

Efficient Frontier visualization

Walk-forward out-of-sample backtesting

Multi-factor CAPM extension

REST API deployment (FastAPI)

Interactive dashboard (Streamlit or React)

Production deployment support

Technical Stack

Python

NumPy

Pandas

SciPy

Matplotlib

Seaborn

yfinance

AMFI API

Author

Bharath Priyan Kumar
Quantitative Finance & Data Science
2026

License

This project is developed for educational and research purposes.
