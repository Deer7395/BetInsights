# BetInsights

BetInsights is a multi-sport betting analytics dashboard providing team and player stats, trends, and data-driven insights for bettors.  
Supports Soccer, NBA, and NFL with advanced statistics and probability-based parlay suggestions.

## Features
- Upcoming matches and games
- In-depth team stats (goals, points, shots, fouls, etc.)
- Player stats (goals, assists, rebounds, tackles, etc.)
- Insights and high-probability parlays
- Multi-sport support: Soccer, NBA, NFL

## Tech Stack
- Backend: Python + Flask
- Data: API-Football (Soccer), balldontlie.io (NBA), MySportsFeeds (NFL)
- Frontend: HTML, CSS, JS, Chart.js/Plotly
- Database: SQLite (MVP)

## Setup
1. Clone the repository
2. Install dependencies: `pip install flask requests`
3. Run: `python app.py`
4. Open browser at `http://127.0.0.1:5000/`
