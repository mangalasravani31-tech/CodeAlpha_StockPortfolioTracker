💹 Stock Portfolio Tracker — CodeAlpha Internship Task 2
A simple console-based Stock Portfolio Tracker built with Python as part of the CodeAlpha Python Programming Internship.
📌 About the Project
The user enters stock symbols and quantities.
The app calculates the total investment value using hardcoded stock prices and optionally saves the result to a .csv file.
🚀 Features
8 predefined stocks with prices (AAPL, TSLA, GOOGL, AMZN, MSFT, INFY, TCS, WIPRO)
Input validation for stock symbols and quantities
Clean tabular portfolio summary in the console
Optional CSV export with timestamp in filename
Supports adding multiple quantities of the same stock
🛠 Concepts Used
Concept
Usage
dictionary
Storing stock prices & portfolio
input/output
User interaction
basic arithmetic
Calculating investment values
file handling
Saving results to CSV
functions
Modular, clean code structure
▶️ How to Run
# Clone the repository
git clone https://github.com/YOUR_USERNAME/CodeAlpha_StockPortfolioTracker.git

# Navigate into the folder
cd CodeAlpha_StockPortfolioTracker

# Run the tracker
python stock_portfolio_tracker.py
Bash
Requires Python 3.x — no external libraries needed!
🎮 Sample Output
==================================================
     💹  STOCK PORTFOLIO TRACKER  💹
==================================================

📈  Available Stocks:
------------------------------
  Symbol      Price (USD)
------------------------------
  AAPL               $180
  TSLA               $250
  ...

➕  Enter stock symbol and quantity (type 'done' to finish):

   Stock symbol : AAPL
   Quantity      : 5
   ✅  Added 5 share(s) of AAPL

==================================================
        📊  PORTFOLIO SUMMARY
==================================================
  Stock      Qty      Price        Value
--------------------------------------------------
  AAPL         5       $180          $900
  TSLA         2       $250          $500
--------------------------------------------------
  TOTAL INVESTMENT                  $1,400
==================================================
Code
📁 Project Structure
Code
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio_tracker.py   # Main application file
└── README.md                    # Project documentation
👩‍💻 Author
Mangala Sravani
Python Programming Intern — CodeAlpha
📅 May 2026 – June 2026
🏷️ Tags
#Python #StockTracker #CodeAlpha #Internship #PythonProgramming #FileHandling
