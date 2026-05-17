import csv
import os
from datetime import datetime

# ── Hardcoded stock prices (USD) ───────────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  178,
    "MSFT":  420,
    "INFY":   18,
    "TCS":    38,
    "WIPRO":   5,
}

# ── Display available stocks ───────────────────────────────────────────────────
def show_available_stocks():
    print("\n📈  Available Stocks:")
    print("-" * 30)
    print(f"  {'Symbol':<8} {'Price (USD)':>12}")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price:>11}")
    print("-" * 30)

# ── Add stocks to portfolio ────────────────────────────────────────────────────
def build_portfolio():
    portfolio = {}
    print("\n➕  Enter stock symbol and quantity (type 'done' to finish):\n")

    while True:
        symbol = input("   Stock symbol : ").strip().upper()
        if symbol.lower() == "done":
            break
        if symbol not in STOCK_PRICES:
            print(f"   ⚠  '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}\n")
            continue

        qty_input = input("   Quantity      : ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("   ⚠  Please enter a valid positive number.\n")
            continue

        quantity = int(qty_input)
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        print(f"   ✅  Added {quantity} share(s) of {symbol}\n")

    return portfolio

# ── Calculate and display portfolio summary ────────────────────────────────────
def display_summary(portfolio):
    if not portfolio:
        print("\n⚠  No stocks in portfolio.\n")
        return 0

    total = 0
    print("\n" + "=" * 50)
    print("        📊  PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>5} {'Price':>10} {'Value':>12}")
    print("-" * 50)

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<8} {qty:>5} ${price:>9} ${value:>11,}")

    print("-" * 50)
    print(f"  {'TOTAL INVESTMENT':>34}  ${total:>11,}")
    print("=" * 50)
    return total

# ── Save results to CSV ────────────────────────────────────────────────────────
def save_to_csv(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price (USD)", "Total Value (USD)"])
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            writer.writerow([symbol, qty, price, price * qty])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", total])
    print(f"\n💾  Portfolio saved to '{filename}'")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print("\n" + "=" * 50)
    print("     💹  STOCK PORTFOLIO TRACKER  💹")
    print("=" * 50)

    show_available_stocks()
    portfolio = build_portfolio()
    total     = display_summary(portfolio)

    if portfolio:
        save = input("\n💾  Save portfolio to CSV? (yes / no): ").strip().lower()
        if save in ("yes", "y"):
            save_to_csv(portfolio, total)

    print("\nThank you for using Stock Portfolio Tracker! 👋\n")

if __name__ == "__main__":
    main()
