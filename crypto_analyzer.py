#!/usr/bin/env python3
"""
Cryptocurrency Analysis Tool
A comprehensive tool for analyzing cryptocurrency prices, trends, and technical indicators
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time


class CryptoAnalyzer:
    """Main class for cryptocurrency analysis"""

    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.session = requests.Session()

    def get_price(self, crypto_id: str, vs_currency: str = "usd") -> Optional[Dict]:
        """
        Get current price of a cryptocurrency

        Args:
            crypto_id: Cryptocurrency ID (e.g., 'bitcoin', 'ethereum')
            vs_currency: Currency to compare against (default: 'usd')

        Returns:
            Dictionary with price information or None if error
        """
        try:
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': crypto_id,
                'vs_currencies': vs_currency,
                'include_24hr_change': 'true',
                'include_24hr_vol': 'true',
                'include_market_cap': 'true'
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None

    def get_historical_data(self, crypto_id: str, days: int = 30, vs_currency: str = "usd") -> Optional[Dict]:
        """
        Get historical market data

        Args:
            crypto_id: Cryptocurrency ID
            days: Number of days of historical data
            vs_currency: Currency to compare against

        Returns:
            Dictionary with historical data or None if error
        """
        try:
            url = f"{self.base_url}/coins/{crypto_id}/market_chart"
            params = {
                'vs_currency': vs_currency,
                'days': days
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return None

    def get_coin_info(self, crypto_id: str) -> Optional[Dict]:
        """
        Get detailed information about a cryptocurrency

        Args:
            crypto_id: Cryptocurrency ID

        Returns:
            Dictionary with coin information or None if error
        """
        try:
            url = f"{self.base_url}/coins/{crypto_id}"
            params = {
                'localization': 'false',
                'tickers': 'false',
                'community_data': 'true',
                'developer_data': 'true'
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching coin info: {e}")
            return None

    def get_top_coins(self, limit: int = 10, vs_currency: str = "usd") -> Optional[List[Dict]]:
        """
        Get top cryptocurrencies by market cap

        Args:
            limit: Number of coins to return
            vs_currency: Currency to compare against

        Returns:
            List of dictionaries with coin data or None if error
        """
        try:
            url = f"{self.base_url}/coins/markets"
            params = {
                'vs_currency': vs_currency,
                'order': 'market_cap_desc',
                'per_page': limit,
                'page': 1,
                'sparkline': 'false',
                'price_change_percentage': '24h,7d,30d'
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching top coins: {e}")
            return None

    def calculate_sma(self, prices: List[float], period: int) -> Optional[List[float]]:
        """
        Calculate Simple Moving Average

        Args:
            prices: List of prices
            period: Period for SMA calculation

        Returns:
            List of SMA values
        """
        if len(prices) < period:
            return None

        sma_values = []
        for i in range(len(prices) - period + 1):
            window = prices[i:i + period]
            sma_values.append(sum(window) / period)

        return sma_values

    def calculate_rsi(self, prices: List[float], period: int = 14) -> Optional[float]:
        """
        Calculate Relative Strength Index (RSI)

        Args:
            prices: List of prices
            period: Period for RSI calculation (default: 14)

        Returns:
            RSI value or None if insufficient data
        """
        if len(prices) < period + 1:
            return None

        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi

    def analyze_trend(self, prices: List[float]) -> str:
        """
        Analyze price trend

        Args:
            prices: List of prices

        Returns:
            Trend description
        """
        if len(prices) < 2:
            return "Insufficient data"

        recent_change = (prices[-1] - prices[0]) / prices[0] * 100

        if recent_change > 5:
            return f"Strong uptrend (+{recent_change:.2f}%)"
        elif recent_change > 1:
            return f"Uptrend (+{recent_change:.2f}%)"
        elif recent_change > -1:
            return f"Sideways ({recent_change:.2f}%)"
        elif recent_change > -5:
            return f"Downtrend ({recent_change:.2f}%)"
        else:
            return f"Strong downtrend ({recent_change:.2f}%)"

    def display_price_info(self, crypto_id: str):
        """Display current price information"""
        print(f"\n{'='*60}")
        print(f"Price Analysis for {crypto_id.upper()}")
        print(f"{'='*60}")

        price_data = self.get_price(crypto_id)
        if not price_data or crypto_id not in price_data:
            print("Unable to fetch price data")
            return

        data = price_data[crypto_id]
        print(f"Current Price: ${data.get('usd', 'N/A'):,.2f}")
        print(f"24h Change: {data.get('usd_24h_change', 0):.2f}%")
        print(f"24h Volume: ${data.get('usd_24h_vol', 0):,.0f}")
        print(f"Market Cap: ${data.get('usd_market_cap', 0):,.0f}")

    def display_top_coins(self, limit: int = 10):
        """Display top cryptocurrencies"""
        print(f"\n{'='*80}")
        print(f"Top {limit} Cryptocurrencies by Market Cap")
        print(f"{'='*80}")

        coins = self.get_top_coins(limit)
        if not coins:
            print("Unable to fetch top coins data")
            return

        print(f"{'Rank':<6}{'Name':<20}{'Price':<15}{'24h %':<12}{'7d %':<12}{'Market Cap':<20}")
        print("-" * 80)

        for coin in coins:
            rank = coin.get('market_cap_rank', 'N/A')
            name = coin.get('name', 'Unknown')
            symbol = coin.get('symbol', '').upper()
            price = coin.get('current_price', 0)
            change_24h = coin.get('price_change_percentage_24h', 0)
            change_7d = coin.get('price_change_percentage_7d_in_currency', 0)
            market_cap = coin.get('market_cap', 0)

            change_24h_str = f"{change_24h:+.2f}%" if change_24h else "N/A"
            change_7d_str = f"{change_7d:+.2f}%" if change_7d else "N/A"

            print(f"{rank:<6}{name[:15]} ({symbol})"[:20].ljust(20)
                  f"${price:,.2f}".ljust(15)
                  f"{change_24h_str}".ljust(12)
                  f"{change_7d_str}".ljust(12)
                  f"${market_cap:,.0f}")

    def technical_analysis(self, crypto_id: str, days: int = 30):
        """Perform technical analysis"""
        print(f"\n{'='*60}")
        print(f"Technical Analysis for {crypto_id.upper()} ({days} days)")
        print(f"{'='*60}")

        historical_data = self.get_historical_data(crypto_id, days)
        if not historical_data or 'prices' not in historical_data:
            print("Unable to fetch historical data")
            return

        prices = [p[1] for p in historical_data['prices']]

        print(f"\nCurrent Price: ${prices[-1]:,.2f}")
        print(f"Highest Price ({days}d): ${max(prices):,.2f}")
        print(f"Lowest Price ({days}d): ${min(prices):,.2f}")
        print(f"Average Price ({days}d): ${sum(prices)/len(prices):,.2f}")

        trend = self.analyze_trend(prices)
        print(f"\nTrend Analysis: {trend}")

        sma_7 = self.calculate_sma(prices, 7)
        if sma_7:
            print(f"7-day SMA: ${sma_7[-1]:,.2f}")

        sma_30 = self.calculate_sma(prices, 30)
        if sma_30:
            print(f"30-day SMA: ${sma_30[-1]:,.2f}")

        rsi = self.calculate_rsi(prices)
        if rsi:
            print(f"\nRSI (14): {rsi:.2f}")
            if rsi > 70:
                print("  → Overbought territory (potential sell signal)")
            elif rsi < 30:
                print("  → Oversold territory (potential buy signal)")
            else:
                print("  → Neutral")

        volatility = (max(prices) - min(prices)) / min(prices) * 100
        print(f"\nVolatility ({days}d): {volatility:.2f}%")


class Portfolio:
    """Simple portfolio tracker"""

    def __init__(self):
        self.holdings = {}
        self.analyzer = CryptoAnalyzer()

    def add_holding(self, crypto_id: str, amount: float, purchase_price: float):
        """Add cryptocurrency to portfolio"""
        self.holdings[crypto_id] = {
            'amount': amount,
            'purchase_price': purchase_price
        }
        print(f"Added {amount} {crypto_id} at ${purchase_price:,.2f} to portfolio")

    def remove_holding(self, crypto_id: str):
        """Remove cryptocurrency from portfolio"""
        if crypto_id in self.holdings:
            del self.holdings[crypto_id]
            print(f"Removed {crypto_id} from portfolio")
        else:
            print(f"{crypto_id} not found in portfolio")

    def display_portfolio(self):
        """Display portfolio with current values"""
        if not self.holdings:
            print("\nPortfolio is empty")
            return

        print(f"\n{'='*80}")
        print("Portfolio Summary")
        print(f"{'='*80}")
        print(f"{'Asset':<15}{'Amount':<15}{'Buy Price':<15}{'Current Price':<15}{'P/L %':<15}")
        print("-" * 80)

        total_value = 0
        total_cost = 0

        for crypto_id, holding in self.holdings.items():
            amount = holding['amount']
            purchase_price = holding['purchase_price']

            price_data = self.analyzer.get_price(crypto_id)
            if price_data and crypto_id in price_data:
                current_price = price_data[crypto_id].get('usd', 0)
                current_value = amount * current_price
                cost_basis = amount * purchase_price
                pnl_pct = ((current_price - purchase_price) / purchase_price * 100) if purchase_price > 0 else 0

                total_value += current_value
                total_cost += cost_basis

                pnl_str = f"{pnl_pct:+.2f}%"
                print(f"{crypto_id:<15}{amount:<15.4f}${purchase_price:<14,.2f}${current_price:<14,.2f}{pnl_str:<15}")

        print("-" * 80)
        total_pnl = ((total_value - total_cost) / total_cost * 100) if total_cost > 0 else 0
        print(f"Total Value: ${total_value:,.2f} | Cost Basis: ${total_cost:,.2f} | Total P/L: {total_pnl:+.2f}%")


def main():
    """Main function with interactive menu"""
    analyzer = CryptoAnalyzer()
    portfolio = Portfolio()

    while True:
        print("\n" + "="*60)
        print("Cryptocurrency Analysis Tool")
        print("="*60)
        print("1. View current price")
        print("2. View top cryptocurrencies")
        print("3. Technical analysis")
        print("4. Add to portfolio")
        print("5. View portfolio")
        print("6. Remove from portfolio")
        print("7. Exit")
        print("="*60)

        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "1":
            crypto_id = input("Enter cryptocurrency ID (e.g., bitcoin, ethereum): ").strip().lower()
            analyzer.display_price_info(crypto_id)

        elif choice == "2":
            try:
                limit = input("Number of top coins to display (default 10): ").strip()
                limit = int(limit) if limit else 10
                analyzer.display_top_coins(limit)
            except ValueError:
                print("Invalid number, showing top 10")
                analyzer.display_top_coins(10)

        elif choice == "3":
            crypto_id = input("Enter cryptocurrency ID: ").strip().lower()
            try:
                days = input("Number of days for analysis (default 30): ").strip()
                days = int(days) if days else 30
                analyzer.technical_analysis(crypto_id, days)
            except ValueError:
                print("Invalid number, using 30 days")
                analyzer.technical_analysis(crypto_id, 30)

        elif choice == "4":
            crypto_id = input("Enter cryptocurrency ID: ").strip().lower()
            try:
                amount = float(input("Enter amount: "))
                purchase_price = float(input("Enter purchase price (USD): "))
                portfolio.add_holding(crypto_id, amount, purchase_price)
            except ValueError:
                print("Invalid input")

        elif choice == "5":
            portfolio.display_portfolio()

        elif choice == "6":
            crypto_id = input("Enter cryptocurrency ID to remove: ").strip().lower()
            portfolio.remove_holding(crypto_id)

        elif choice == "7":
            print("\nThank you for using Cryptocurrency Analysis Tool!")
            break

        else:
            print("Invalid option, please try again")

        time.sleep(1)


if __name__ == "__main__":
    main()
