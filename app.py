from flask import Flask, jsonify
import random

app = Flask(__name__)

tracks = ["track1.mp3", "track2.mp3", "track3.mp3", "track4.mp3", "track5.mp3"]

@app.route('/next_track')
def next_track():
    # Get a random track name from the array
    random_track = random.choice(tracks)
    # Return the random track name as JSON
    return jsonify({"next_track": random_track})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
