from flask import Flask, render_template
import requests

app = Flask(__name__)

# --- Soccer matches (demo free API) ---
def get_soccer_matches():
    try:
        response = requests.get("https://www.scorebat.com/video-api/v3/feed/?token=demo")
        data = response.json()
        matches = []
        for item in data.get("response", [])[:5]:
            matches.append({
                "home": item["title"].split(" - ")[0],
                "away": item["title"].split(" - ")[1],
                "date": item.get("date", "TBD")[:10]
            })
        return matches
    except:
        return []

# --- NBA games (balldontlie.io) ---
def get_nba_games():
    try:
        response = requests.get("https://www.balldontlie.io/api/v1/games?per_page=5")
        data = response.json()
        games = []
        for g in data["data"]:
            games.append({
                "home": g["home_team"]["full_name"],
                "away": g["visitor_team"]["full_name"],
                "date": g["date"][:10]
            })
        return games
    except:
        return []

# --- NFL games (demo static data) ---
def get_nfl_games():
    return [
        {"home": "Patriots", "away": "Dolphins", "date": "2025-12-20"},
        {"home": "Packers", "away": "Bears", "date": "2025-12-21"},
        {"home": "Cowboys", "away": "Giants", "date": "2025-12-22"},
        {"home": "Vikings", "away": "Seahawks", "date": "2025-12-23"},
        {"home": "Broncos", "away": "Raiders", "date": "2025-12-24"},
    ]

@app.route("/")
def index():
    soccer = get_soccer_matches()
    nba = get_nba_games()
    nfl = get_nfl_games()
    return render_template("index.html", soccer=soccer, nba=nba, nfl=nfl)

if __name__ == "__main__":
    app.run(debug=True)
