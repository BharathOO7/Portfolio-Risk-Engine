# ==========================================================
# UNIVERSAL INSTITUTIONAL PORTFOLIO RISK ENGINE
# Stocks + ETFs + Crypto + Mutual Funds
# With Optimization + Risk Attribution + Rebalance Engine
# ==========================================================

import numpy as np
import pandas as pd
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

plt.style.use("ggplot")
np.random.seed(42)


class UniversalPortfolioRiskEngine:

    def __init__(self, assets, weights, initial_investment):
        self.assets = assets
        self.weights = np.array(weights)
        self.initial_investment = initial_investment

        self.price_data = {}
        self.returns = None
        self.mean_daily = None
        self.cov_daily = None
        self.optimal_weights = None

    # ---------------------------------------------------
    # Asset Type Detection
    # ---------------------------------------------------
    def is_mutual_fund(self, asset):
        return asset.isdigit()

    # ---------------------------------------------------
    # Fetch Data
    # ---------------------------------------------------
    def fetch_data(self):
        
        print("\nFetching data...\n")
        for asset in self.assets:

            try:
                if self.is_mutual_fund(asset):

                    url = f"https://api.mfapi.in/mf/{asset}"
                    response = requests.get(url)

                    if response.status_code != 200:
                        print(f"Failed to fetch MF {asset}")
                        continue

                    data = response.json()
                    df = pd.DataFrame(data["data"])
                    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
                    df["nav"] = pd.to_numeric(df["nav"])
                    df = df.sort_values("date")

                    series = df.set_index("date")["nav"]

                    if not series.empty:
                        self.price_data[asset] = series

                else:
                    data = yf.download(asset, period="5y", auto_adjust=True)

                    if data.empty:
                        print(f"No data for {asset}")
                        continue

                    if "Close" in data.columns:
                        series = data["Close"]
                    else:
                        series = data.iloc[:, 0]

                    if not series.empty:
                        self.price_data[asset] = series

            except Exception as e:
                print(f"Error fetching {asset}: {e}")

        if len(self.price_data) == 0:
            raise ValueError("No valid asset data fetched.")

        combined = pd.concat(self.price_data.values(), axis=1)
        combined.columns = self.price_data.keys()
        combined = combined.dropna()

        self.returns = np.log(combined / combined.shift(1)).dropna()

        print("Data Ready.\n")

    # ---------------------------------------------------
    # Statistics
    # ---------------------------------------------------
    def calculate_statistics(self):

        self.mean_daily = self.returns.mean()
        self.cov_daily = self.returns.cov()

        self.cov_daily += np.eye(len(self.assets)) * 1e-8

    # ---------------------------------------------------
    # Monte Carlo
    # ---------------------------------------------------
    def monte_carlo(self, simulations=5000, days=252):

        chol = np.linalg.cholesky(self.cov_daily)
        portfolio_paths = np.zeros((days, simulations))

        for sim in range(simulations):
            Z = np.random.normal(size=(days, len(self.assets)))
            correlated = Z @ chol.T
            returns = correlated + self.mean_daily.values
            portfolio_daily = returns @ self.weights
            portfolio_paths[:, sim] = self.initial_investment * np.exp(
                np.cumsum(portfolio_daily)
            )

        return portfolio_paths

    # ---------------------------------------------------
    # Risk Report
    # ---------------------------------------------------
    def risk_report(self, paths):

        final_values = paths[-1]
        expected_value = np.mean(final_values)
        volatility = np.std(final_values)

        var_95 = np.percentile(final_values, 5)
        cvar_95 = final_values[final_values <= var_95].mean()

        annual_return = (expected_value / self.initial_investment - 1)
        annual_vol = volatility / self.initial_investment
        sharpe = annual_return / annual_vol if annual_vol != 0 else 0

        print("\n========== PORTFOLIO RISK REPORT ==========")
        print(f"Expected Annual Return: {annual_return*100:.2f}%")
        print(f"Annual Volatility: {annual_vol*100:.2f}%")
        print(f"Sharpe Ratio: {sharpe:.2f}")
        print(f"VaR 95%: ₹{var_95:,.2f}")
        print(f"CVaR 95%: ₹{cvar_95:,.2f}")
        print("===========================================\n")

    # ---------------------------------------------------
    # Mean-Variance Optimization
    # ---------------------------------------------------
    def optimize_portfolio(self):

        mean_returns = self.mean_daily * 252
        cov_matrix = self.cov_daily * 252
        num_assets = len(self.assets)

        def portfolio_vol(weights):
            return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))
        init_guess = num_assets * [1. / num_assets]

        result = minimize(portfolio_vol, init_guess,
                          method='SLSQP',
                          bounds=bounds,
                          constraints=constraints)

        self.optimal_weights = result.x

        print("Optimal Weights (Min Variance):")
        for asset, weight in zip(self.assets, self.optimal_weights):
            print(f"{asset}: {weight:.4f}")

    # ---------------------------------------------------
    # Risk Attribution
    # ---------------------------------------------------
    def risk_attribution(self):

        cov = self.cov_daily * 252
        portfolio_vol = np.sqrt(np.dot(self.weights.T, np.dot(cov, self.weights)))

        marginal_contribution = np.dot(cov, self.weights) / portfolio_vol
        contribution = self.weights * marginal_contribution

        print("\nRisk Contribution:")
        for asset, rc in zip(self.assets, contribution):
            print(f"{asset}: {rc:.4f}")

    # ---------------------------------------------------
    # Rebalance + Recommendation Engine
    # ---------------------------------------------------
    def recommendation_engine(self):

        print("\n========== PORTFOLIO RECOMMENDATIONS ==========\n")

        annual_returns = self.mean_daily * 252
        annual_vol = self.returns.std() * np.sqrt(252)
        sharpe = annual_returns / annual_vol

        for i, asset in enumerate(self.assets):

            ret = annual_returns.iloc[i]
            vol = annual_vol.iloc[i]
            sr = sharpe.iloc[i]

            current_weight = self.weights[i]
            optimal_weight = self.optimal_weights[i]
            deviation = current_weight - optimal_weight

            print(f"\nAsset: {asset}")
            print(f"Current Weight: {current_weight:.2f}")
            print(f"Optimal Weight: {optimal_weight:.2f}")
            print(f"Expected Return: {ret*100:.2f}%")
            print(f"Volatility: {vol*100:.2f}%")
            print(f"Sharpe Ratio: {sr:.2f}")
            print(f"Deviation from Optimal: {deviation:.2f}")

            # Decision Logic
            if ret < 0:
                action = "🔴 SELL"
            elif sr < 0.5:
                action = "🟠 REDUCE"
            elif deviation < -0.05:
                action = "🟢 INCREASE"
            elif deviation > 0.05:
                action = "🟠 REDUCE"
            else:
                action = "🟡 KEEP"

            print(f"Recommendation: {action}")

        print("\n===============================================\n")

    # ---------------------------------------------------
    # Visualization
    # ---------------------------------------------------
    def visualize(self, paths):

        plt.figure(figsize=(10,6))
        plt.plot(paths[:, :200], alpha=0.3)
        plt.title("Monte Carlo Simulation")
        plt.show()

        plt.figure(figsize=(8,6))
        sns.heatmap(self.returns.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.show()


# ==========================================================
# MAIN EXECUTION
# ==========================================================

if __name__ == "__main__":

    print("====== UNIVERSAL PORTFOLIO RISK ENGINE ======\n")

    user_assets = input("Enter assets (comma separated): ")
    assets = [a.strip().upper() for a in user_assets.split(",")]

    user_weights = input("Enter weights in %: ")
    weights = [float(w.strip())/100 for w in user_weights.split(",")]

    weights = np.array(weights)
    weights = weights / np.sum(weights)

    initial_investment = float(input("Enter initial investment amount: "))

    engine = UniversalPortfolioRiskEngine(
        assets=assets,
        weights=weights,
        initial_investment=initial_investment
    )

    engine.fetch_data()
    engine.calculate_statistics()

    paths = engine.monte_carlo()
    engine.risk_report(paths)

    engine.optimize_portfolio()
    engine.risk_attribution()
    engine.recommendation_engine()

    engine.visualize(paths)
