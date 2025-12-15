#!/usr/bin/env python3
"""
Script de démonstration du Crypto Analyzer
Ce script montre les différentes fonctionnalités sans interaction
"""

from crypto_analyzer import CryptoAnalyzer, Portfolio
import time

def main():
    print("=" * 70)
    print("DÉMONSTRATION DU LOGICIEL D'ANALYSE DE CRYPTOMONNAIE")
    print("=" * 70)

    analyzer = CryptoAnalyzer()

    # Démo 1: Prix du Bitcoin
    print("\n📊 DÉMO 1: Prix actuel du Bitcoin")
    print("-" * 70)
    analyzer.display_price_info("bitcoin")
    time.sleep(2)

    # Démo 2: Prix de l'Ethereum
    print("\n📊 DÉMO 2: Prix actuel de l'Ethereum")
    print("-" * 70)
    analyzer.display_price_info("ethereum")
    time.sleep(2)

    # Démo 3: Top 5 cryptomonnaies
    print("\n🏆 DÉMO 3: Top 5 cryptomonnaies par capitalisation")
    print("-" * 70)
    analyzer.display_top_coins(5)
    time.sleep(2)

    # Démo 4: Analyse technique du Bitcoin
    print("\n📈 DÉMO 4: Analyse technique du Bitcoin (30 jours)")
    print("-" * 70)
    analyzer.technical_analysis("bitcoin", 30)
    time.sleep(2)

    # Démo 5: Portfolio exemple
    print("\n💼 DÉMO 5: Exemple de portefeuille")
    print("-" * 70)
    portfolio = Portfolio()
    portfolio.add_holding("bitcoin", 0.5, 40000)
    portfolio.add_holding("ethereum", 2.0, 2500)
    portfolio.display_portfolio()

    print("\n" + "=" * 70)
    print("✅ Démonstration terminée!")
    print("=" * 70)
    print("\n💡 Pour utiliser le mode interactif, lancez: python crypto_analyzer.py")
    print("   Vous pourrez alors choisir les options 1-7 du menu\n")

if __name__ == "__main__":
    main()
