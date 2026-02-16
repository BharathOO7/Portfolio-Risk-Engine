🛡️ Universal Portfolio Risk Engine (UPRE)Multi-Asset Institutional-Style Quantitative Analytics & Risk ManagementUPRE is a high-performance quantitative engine designed to bridge the gap between retail investing and institutional-grade risk management. It utilizes Modern Portfolio Theory (MPT) and Stochastic Modeling to provide actionable intelligence across global equities, ETFs, Cryptocurrencies, and Indian Mutual Funds.🚀 Core CapabilitiesFeatureDescriptionGlobal ReachUnified data fetching for NSE/BSE, NYSE/NASDAQ, and Global Crypto markets.Advanced Simulation5,000+ path Monte Carlo simulations using Cholesky Decomposition for correlated assets.Risk MetricsParametric and Non-parametric VaR (Value at Risk) & CVaR (Expected Shortfall).OptimizationMean-Variance Optimization (MVO) to find the Tangency Portfolio (Max Sharpe).Actionable AIHeuristic-based Decision Engine: SELL🏗️ System ArchitectureThe engine follows a modular pipeline:Data Ingestion: Asynchronous fetching via yfinance and AMFI APIs.Processing: Log-normal return transformation and covariance matrix shrinkage.Sim Engine: Brownian motion simulation for forward-looking risk.Analytics Layer: Computation of MCTR and Risk Attribution.Strategy Layer: Rebalancing logic based on deviation from the Efficient Frontier.📊 Mathematical FoundationsThe engine doesn't just "crunch numbers"; it applies rigorous financial modeling:1. Risk AttributionWe calculate the Marginal Contribution to Risk (MCTR) to identify which asset is driving portfolio volatility:$$MCTR_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{(Vw)_i}{\sigma_p}$$Where $V$ is the covariance matrix, $w$ is the weight vector, and $\sigma_p$ is the portfolio volatility.2. Monte Carlo ProjectionAsset paths are modeled using Geometric Brownian Motion (GBM):$$S_t = S_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)$$💻 Installation & QuickstartPrerequisitesPython 3.9+Pandas, NumPy, SciPy, Matplotlib, YFinanceSetupBash# Clone the architecture
git clone https://github.com/your-username/PortfolioRiskProject.git
cd PortfolioRiskProject

# Environment isolation
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
ExecutionBashpython portfolio_risk_model.py
📋 Sample Dashboard OutputPlaintext===========================================================
PORTFOLIO RISK ANALYSIS REPORT
===========================================================
Assets: [RELIANCE.NS, BTC-USD] | Weights: [50%, 50%]
-----------------------------------------------------------
STATISTICS:
- Expected Annual Return: 13.37%
- Annual Volatility:    37.46%
- Sharpe Ratio:         0.36
- VaR (95%):           ₹6,450 (Max likely loss)
- CVaR (95%):          ₹5,674 (Avg. loss in tail)

OPTIMIZATION (Mean-Variance):
- Current vs. Optimal: 50/50 -> 88/12
- Suggested Action: REDUCE BTC-USD (High Volatility Contribution)
===========================================================
🗺️ Roadmap & Future Enhancements[ ] Black-Litterman Integration: Incorporate investor views with market equilibrium.[ ] Interactive Dashboard: Build a Streamlit UI for real-time "What-If" analysis.[ ] Fat-Tail Modeling: Move beyond Gaussian assumptions using Student's T-distributions.[ ] Transaction Cost Awareness: Factor in slippage and STT for Indian markets.⚖️ DisclaimerThis software is for educational purposes only. Past performance is not indicative of future results. Quantitative models are approximations of reality and can fail during "Black Swan" events.Author: Bharath Priyan KumarRole: Quantitative Finance & Data ScienceYear: 2026
