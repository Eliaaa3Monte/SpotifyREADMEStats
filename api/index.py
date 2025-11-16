# Simple API used to access stats via HTTP requests
from flask import Flask, jsonify, redirect, send_file
from io import BytesIO
import sys

sys.path.append("..")
import statsCollector
import statsImageGenerator

app = Flask(__name__)


@app.route("/json")  # Endpoint to get Spotify stats as json
def get_stats():
    stats = statsCollector.main()
    return jsonify(stats)


@app.route("/stats")  # Endpoint to get infographics stats
def create_stats_image():
    stats = statsCollector.main()
    image = statsImageGenerator.create_spotify_infographic(stats)
    img_io = BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")


@app.route("/")  # Home endpoint
def home():
    return redirect("https://github.com/JohanVerne/SpotifyStats")


if __name__ == "__main__":
    pass  # For Vercel deployment
