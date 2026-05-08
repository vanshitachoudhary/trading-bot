# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot for Binance USDT-M Futures Testnet.

---

## Features

- MARKET and LIMIT order support
- BUY and SELL order support
- Binance Futures Testnet integration
- CLI-based order placement
- Input validation
- Logging system
- Error handling

---

## Project Structure

```text
trading-bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── trading.log
├── .env
```

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret
```

---

## Run MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## Run LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
```

---

## Logging

All API requests, responses, and errors are stored in:

```text
trading.log
```