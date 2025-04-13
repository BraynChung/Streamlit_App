# 📈 Simple Stock Price App

## Overview
A streamlined web application that visualizes historical stock data with interactive charts. Currently configured to display Apple (AAPL) stock closing prices and trading volumes from 2010 to present.

![image](https://github.com/user-attachments/assets/771c412e-597e-4b95-a9af-c4a4eb1e54b7)

## Features
- **Real-time Data**: Fetches up-to-date stock information using yfinance API
- **Interactive Visualizations**: Responsive charts for:
  - Historical closing prices
  - Trading volume over time
- **Customizable Timeframes**: Currently set from May 2010 to March 2025
- **Streamlit Integration**: Leverages Streamlit for an interactive web interface




## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/stock-price-app.git
   cd stock-price-app
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit runApp.py
   ```

2. Open your browser to view the app (typically http://localhost:8501)

## Customization Options

### Change the Stock Symbol
To track a different company, modify the `tickerSymbol` variable:
```python
# Change from AAPL to your preferred stock symbol
tickerSymbol = 'MSFT'  # Example: Microsoft
```

### Adjust the Time Period
Change the date range by modifying the start and end parameters:
```python
tickerDf = tickerData.history(period='1d', start='2015-1-1', end='2025-1-1')
```

### Add Technical Indicators
Enhance the visualization with technical indicators like moving averages:
```python
# Add a 50-day moving average
tickerDf['MA50'] = tickerDf['Close'].rolling(window=50).mean()
st.line_chart(tickerDf[['Close', 'MA50']])
```
