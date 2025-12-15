# Crypto Analyzer - Logiciel d'Analyse de Cryptomonnaie

## 🇫🇷 Description (Français)

Un outil complet d'analyse de cryptomonnaies en Python qui permet de:
- Consulter les prix en temps réel
- Analyser les tendances du marché
- Calculer des indicateurs techniques (SMA, RSI)
- Suivre un portefeuille personnel
- Visualiser les top cryptomonnaies par capitalisation

### Fonctionnalités

1. **Prix en temps réel**: Obtenez le prix actuel de n'importe quelle cryptomonnaie
2. **Top cryptomonnaies**: Consultez les meilleures cryptos par capitalisation boursière
3. **Analyse technique**:
   - Moyennes mobiles simples (SMA 7 et 30 jours)
   - Indice de force relative (RSI)
   - Analyse de tendance
   - Calcul de volatilité
4. **Gestion de portefeuille**: Suivez vos investissements et vos gains/pertes
5. **Données historiques**: Analysez les performances sur 30 jours ou plus

### Installation

```bash
# Cloner le dépôt
git clone <repository-url>
cd TEST

# Installer les dépendances
pip install -r requirements.txt
```

### Utilisation

```bash
python crypto_analyzer.py
```

Le programme affichera un menu interactif avec les options suivantes:

1. **Voir le prix actuel**: Entrez l'ID de la crypto (ex: bitcoin, ethereum, cardano)
2. **Voir les top cryptomonnaies**: Affiche les cryptos par capitalisation
3. **Analyse technique**: Analyse détaillée avec indicateurs techniques
4. **Ajouter au portefeuille**: Ajoutez vos investissements
5. **Voir le portefeuille**: Consultez vos gains/pertes
6. **Retirer du portefeuille**: Supprimez une position
7. **Quitter**: Fermer le programme

### Exemples d'utilisation

```python
# Exemple 1: Voir le prix du Bitcoin
Choisissez l'option 1
Entrez: bitcoin

# Exemple 2: Analyse technique de l'Ethereum sur 60 jours
Choisissez l'option 3
Entrez: ethereum
Nombre de jours: 60

# Exemple 3: Ajouter Bitcoin au portefeuille
Choisissez l'option 4
Crypto ID: bitcoin
Montant: 0.5
Prix d'achat: 40000
```

### IDs de Cryptomonnaies Populaires

- Bitcoin: `bitcoin`
- Ethereum: `ethereum`
- Binance Coin: `binancecoin`
- Cardano: `cardano`
- Solana: `solana`
- Polkadot: `polkadot`
- Dogecoin: `dogecoin`
- Ripple: `ripple`

---

## 🇬🇧 Description (English)

A comprehensive cryptocurrency analysis tool in Python that allows you to:
- Check real-time prices
- Analyze market trends
- Calculate technical indicators (SMA, RSI)
- Track a personal portfolio
- View top cryptocurrencies by market cap

### Features

1. **Real-time Prices**: Get the current price of any cryptocurrency
2. **Top Cryptocurrencies**: View the best cryptos by market capitalization
3. **Technical Analysis**:
   - Simple Moving Averages (7 and 30 days SMA)
   - Relative Strength Index (RSI)
   - Trend analysis
   - Volatility calculation
4. **Portfolio Management**: Track your investments and gains/losses
5. **Historical Data**: Analyze performance over 30 days or more

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd TEST

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python crypto_analyzer.py
```

The program will display an interactive menu with the following options:

1. **View current price**: Enter the crypto ID (e.g., bitcoin, ethereum, cardano)
2. **View top cryptocurrencies**: Display cryptos by market cap
3. **Technical analysis**: Detailed analysis with technical indicators
4. **Add to portfolio**: Add your investments
5. **View portfolio**: Check your gains/losses
6. **Remove from portfolio**: Delete a position
7. **Exit**: Close the program

### Usage Examples

```python
# Example 1: View Bitcoin price
Select option 1
Enter: bitcoin

# Example 2: Technical analysis of Ethereum over 60 days
Select option 3
Enter: ethereum
Number of days: 60

# Example 3: Add Bitcoin to portfolio
Select option 4
Crypto ID: bitcoin
Amount: 0.5
Purchase price: 40000
```

### Popular Cryptocurrency IDs

- Bitcoin: `bitcoin`
- Ethereum: `ethereum`
- Binance Coin: `binancecoin`
- Cardano: `cardano`
- Solana: `solana`
- Polkadot: `polkadot`
- Dogecoin: `dogecoin`
- Ripple: `ripple`

## 📊 Technical Indicators Explained

### RSI (Relative Strength Index)
- **Above 70**: Overbought (potential sell signal)
- **Below 30**: Oversold (potential buy signal)
- **Between 30-70**: Neutral

### SMA (Simple Moving Average)
- **7-day SMA**: Short-term trend
- **30-day SMA**: Long-term trend
- When price > SMA: Bullish signal
- When price < SMA: Bearish signal

## 🔧 API Source

This tool uses the free CoinGecko API. No API key required!

## 📝 License

Open source - Feel free to use and modify

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. Not financial advice. Always do your own research before investing in cryptocurrencies.
