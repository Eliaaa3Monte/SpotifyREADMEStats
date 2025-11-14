# Simple API used to access stats via HTTP requests
from flask import Flask, jsonify
import sys

sys.path.append("..")
import statsCollector

app = Flask(__name__)


@app.route("/stats")  # Endpoint to get Spotify stats
def get_stats():
    stats = statsCollector.main()
    return jsonify(stats)


@app.route("/")  # Home endpoint
def home():
    return "<h1>Welcome to the Spotify Stats API</h1><p>Access your stats at <a href='/stats'>/stats</a></p>"


if __name__ == "__main__":
    pass  # For Vercel deployment
